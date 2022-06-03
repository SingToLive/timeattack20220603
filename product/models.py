from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Nutrition(models.Model):
    class Meta:
        db_table = 'nutrition'

    kcal = models.IntegerField(validators=[MinValueValidator(0)])
    sodium = models.IntegerField(validators=[MinValueValidator(0)])
    saturated_fat = models.IntegerField(validators=[MinValueValidator(0)])
    sugar = models.IntegerField(validators=[MinValueValidator(0)])
    protein = models.IntegerField(validators=[MinValueValidator(0)])
    caffeine = models.IntegerField(validators=[MinValueValidator(0)])

class Category(models.Model):
    class Meta:
        db_table = 'drink_category'

    name = models.CharField(max_length=50)

class Allergy(models.Model):
    class Meta:
        db_table = 'allergy'

    name = models.CharField(max_length=50)

class Drink(models.Model):
    class Meta:
        db_table = 'drink'

    name = models.CharField(max_length=50)
    cat = models.ManyToManyField(Category, related_name='category_name')
    nut = models.ForeignKey(Nutrition, on_delete=models.CASCADE)
    alle = models.ManyToManyField(Allergy, related_name='allergy_name')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE)
