from django.shortcuts import render
from django.http import JsonResponse
import requests
from .models import Recipe

# Create your views here.

def fetchrecipe(req):
    url = "https://dummyjson.com/recipes"
    response = requests.get(url)
    print(response)

    if response.status_code==200:
        data=response.json()
        count=0

        for item in data.get("recipes",[]):
            if not Recipe.objects.filter(name=item['name']).exists():
                Recipe.objects.create(
                    name=item['name'],
                    ingredients=item['ingredients'],
                    instructions=item['instructions'],
                    prepTimeMinutes=item['prepTimeMinutes'],
                    cookTimeMinutes=item['cookTimeMinutes'],
                    servings=item['servings'],
                    difficulty=item['difficulty'],
                    cuisine=item['cuisine'],
                    caloriesPerServing=item['caloriesPerServing'],
                    tags=item['tags'],
                    image=item['image'],
                    rating=item['rating'],
                    reviewCount=item['reviewCount'],
                    mealType=item['mealType'],
                )
                count += 1



        return JsonResponse({'message':f"Total {count} Recipes fetched successfully"})
    else:
        return JsonResponse({"error":"Failed to fetch recepes"},status=500)

