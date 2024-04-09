from django.http import HttpResponse

from .models import ObligationRegulation, ElementModel


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def optimize_me(request):
    list_elements = {
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
