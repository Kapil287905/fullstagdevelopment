from django.db import models

# Create your models here.
class Recipe(models.Model):
    name=models.CharField(max_length=255)
    ingredients=models.JSONField()
    instructions=models.JSONField()
    prepTimeMinutes=models.IntegerField()
    cookTimeMinutes=models.IntegerField()
    servings=models.IntegerField()
    difficulty=models.CharField()
    cuisine=models.CharField()
    caloriesPerServing=models.FloatField()
    tags=models.JSONField()
    image=models.URLField()
    rating=models.FloatField()
    reviewCount=models.IntegerField()
    mealType=models.JSONField()