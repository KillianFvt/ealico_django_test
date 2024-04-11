from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

USER_RIGHT = (
    ("", "---"),
    ("r", "Lecture"),
    ("w", "Ecriture"),
)


class Regulation(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    icon_name = models.CharField(max_length=200)


class Factory(models.Model):
    name = models.CharField(max_length=100)


class Building(models.Model):
    name = models.CharField(max_length=150, blank=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name="factory_building")


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    regulation_right = models.ManyToManyField(Regulation, through="UserProfile")
    building = models.ManyToManyField(Building)


class UserProfile(models.Model):
    regulation = models.ForeignKey(Regulation, on_delete=models.CASCADE)
    Profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    right = models.CharField(max_length=10, null=True, blank=True, choices=USER_RIGHT)


class ElementModel(models.Model):
    regulation = models.ForeignKey(Regulation, null=True, blank=True, on_delete=models.CASCADE)
    repere_1 = models.CharField(max_length=100)
    repere_2 = models.CharField(max_length=100)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.CASCADE)
    is_conforme = models.BooleanField(default=True)
    date = models.DateField(null=True, blank=True, auto_now_add=True)


class ElementModelTest1(models.Model):
    regulation = models.ForeignKey(Regulation, null=True, blank=True, on_delete=models.CASCADE)
    repere_1 = models.CharField(max_length=100)
    repere_2 = models.CharField(max_length=100)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.CASCADE)


class ElementModelTest2(models.Model):
    regulation = models.ForeignKey(Regulation, null=True, blank=True, on_delete=models.CASCADE)
    repere_1 = models.CharField(max_length=100)
    repere_2 = models.CharField(max_length=100)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, null=True, blank=True, on_delete=models.CASCADE)


class ObligationRegulation(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey(for_concrete_model=False)
