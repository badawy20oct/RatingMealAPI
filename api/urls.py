
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import RatingViewSets , MealViewSets

router = routers.DefaultRouter()
router.register('meals' , MealViewSets)
router.register('ratings' , RatingViewSets)

urlpatterns = [
    path('' , include(router.urls)),
]
