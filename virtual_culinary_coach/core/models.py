# models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    # Setting unique related names for groups and permissions to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_groups',
        blank=True,
        help_text=('The groups this user belongs to.'),
        verbose_name=('groups'),
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions'),
    )
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

class MealPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    sustainable_alternative = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    meal_plan = models.ForeignKey(MealPlan, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient)
    instructions = models.TextField()
    nutritional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class CoachingSession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_sessions')
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='coach_sessions')
    session_type = models.CharField(max_length=20, choices=[('video', 'Video Call'), ('chat', 'Chat'), ('voice', 'Voice Call')])
    date_time = models.DateTimeField()
    duration = models.IntegerField(help_text="Duration in minutes")

    def __str__(self):
        return f"{self.session_type} session on {self.date_time} for {self.duration} minutes"
