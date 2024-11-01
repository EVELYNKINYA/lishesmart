from rest_framework import serializers
from .models import User, MealPlan, Recipe, CoachingSession

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'dietary_preferences', 'health_goals', 'is_coach']

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = '__all__'

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class CoachingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachingSession
        fields = '__all__'
