from django.contrib import admin

from .models import (Building, ElementModel, ElementModelTest1,
                     ElementModelTest2, Factory, ObligationRegulation,
                     Regulation, Profile, UserProfile)

admin.site.register(Regulation)
admin.site.register(Building)
admin.site.register(ElementModel)
admin.site.register(Factory)
admin.site.register(ElementModelTest1)
admin.site.register(ElementModelTest2)
admin.site.register(ObligationRegulation)
admin.site.register(Profile)
admin.site.register(UserProfile)
