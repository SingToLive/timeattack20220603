from django.contrib import admin
from .models import Drink, Allergy, Category, Nutrition

# Register your models here.
@admin.register(Drink)
class CustomDrink(admin.ModelAdmin):
    list_display = ('name', 'nut',)

@admin.register(Nutrition)
class CustomNutrition(admin.ModelAdmin):
    list_display = ('kcal', 'sodium', 'saturated_fat', 'sugar', 'protein', 'caffeine')

@admin.register(Category)
class CustomCategory(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Allergy)
class CustomAllergy(admin.ModelAdmin):
    list_display = ('name',)

