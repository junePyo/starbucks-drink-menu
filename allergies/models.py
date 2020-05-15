from django.db import models

class Allergy(models.Model):
    allergen = models.CharField(max_length=20)

    def __str__(self):
        return allergen

    class Meta:
        db_table = 'allergies'

class DrinkAllergen(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.SET_NULL, null=True)
    allergy = models.ForeignKey('Allergy', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'drinks_allergies'



