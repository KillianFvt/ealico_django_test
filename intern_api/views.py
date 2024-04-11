from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from app.models import ElementModel, UserProfile, Regulation
from app.serializers import ElementModelSerializer


class ElementViewSet(viewsets.ViewSet):
    # filtre avec les champs repere_1
    # exemple : /api/element/?repere_1=[nombre]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['repere_1']

    def list(self, request):

        user_profile = request.user.user_profile
        user_buildings = user_profile.building.all()
        regulation_rights = user_profile.regulation_right.all()

        queryset = ElementModel.objects.filter(building__in=user_buildings, regulation__in=regulation_rights)

        queryset = ElementModel.objects.all()
        return Response({"data": queryset.values()})

    def retrieve(self, request, pk=None):
        queryset = ElementModel.objects.all()
        element = get_object_or_404(queryset, pk=pk)
        serializer = ElementModelSerializer(element)
        return Response(serializer.data)

    def update(self, request, pk=None):

        forbidden_response = Response({"status": "error"}, status=status.HTTP_403_FORBIDDEN)

        # Get the user profile
        profile = request.user.user_profile
        # Get the user UserProfiles
        user_profiles = UserProfile.objects.filter(Profile=profile)
        element = ElementModel.objects.get(pk=pk)

        # Check if the user has the right of the building
        if element.building not in profile.building.all():
            return forbidden_response

        # Check if the user has the right of the regulation
        element_regulation = element.regulation

        has_regulation_match = False

        # loop through the user profiles to check if the user has the right of the regulation
        for profile in user_profiles:
            profile_regulation = Regulation.objects.get(pk=profile.regulation.id)

            if element_regulation.id == profile_regulation.id:
                has_regulation_match = True
                if profile.right != 'w':
                    print("forbidden")
                    return forbidden_response
                break

        # if the regulation is not found in the user profiles
        # return forbidden response
        if not has_regulation_match:
            return forbidden_response

        for key, value in request.data.items():
            if key in ['repere_1', 'repere_2']:
                setattr(element, key, value)
        element.save()
        return Response({"status": "success"}, status=status.HTTP_200_OK)


