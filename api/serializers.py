from rest_framework import serializers
from .models import Meal , Rating



class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['id', 'title', 'description' , 'Number_of_Rating','Average_of_Rating']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id','user','meal' , 'stars']