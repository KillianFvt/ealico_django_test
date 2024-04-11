from django.http import HttpResponse
from rest_framework.decorators import api_view
from .models import ObligationRegulation, ElementModel, UserProfile


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def optimize_me(request):
    list_elements = {
        # ces modèles ont été désactivés car ils semblaient être du code dupliqué
        # "elementmodeltest1": ElementModelTest1.objects.all().values_list('id', flat=True),
        # "elementmodeltest2": ElementModelTest2.objects.all().values_list('id', flat=True),
        "elementmodeltest": ElementModel.objects.all().values_list('id', flat=True),
    }
    for model_name, list_ids in list_elements.items():
        OR = ObligationRegulation.objects.filter(
            content_type__model=model_name,
            object_id__in=list_ids
        )
        print(OR)
    return HttpResponse("Hello, world. You're at the optimize_me.")


# Ceci est la vue de la première partie du test
@api_view(['POST'])
def get_conformity_percentage_monthly(request):
    """
    This method gets the conformity percentage of the ElementModels that have been created in the given month and year
    So it has to be called multiple times for each month and year
    required data: month, year
    """
    # Get the user Profile
    profile = request.user.user_profile
    # Get the user UserProfiles
    user_profiles = UserProfile.objects.filter(Profile=profile, right='r')
    # Get the regulations the user has read access to
    regulations = [user_profile.regulation for user_profile in user_profiles]
    # Get the ElementModels that are associated with these regulations
    elements = ElementModel.objects.filter(regulation__in=regulations)
    # Get the user buildings
    user_buildings = profile.building.all()
    # Get the ElementModels that are associated with these buildings
    elements = elements.filter(building__in=user_buildings)

    # Get the total number of ElementModels
    total = elements.count()

    post_data = request.data
    # Get the month and year from the post data
    month = post_data.get('month')
    year = post_data.get('year')

    # Get the ElementModels that have been created in the given month and year
    elements = elements.filter(date__month=month, date__year=year)