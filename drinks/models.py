from django.db import models

class Drink(models.Model):
    name_Korean = models.CharField(max_length=50)
    name_English = models.CharField(max_length=50)
    description_main = models.CharField(max_length=300)
    description_sub = models.CharField(max_length=300)
    nutrients = models.OneToOneField('Nutrients', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    allergens = models.ManyToManyField('Allergy', through='DrinkAllergen', related_name='containing_drinks')

    def __str__(self):
        return self.name_Korean

    class Meta:
        db_table = 'drinks'

class Nutrients(models.Model):
    serving = models.Integerfield()
    calorie = models.DecimalField(max_digits=5, decimal_places=1)
    fat = models.DecimalField(max_digits=5, decimal_places=1)
    protein = models.DecimalField(max_digits=5, decimal_places=1)
    sodium = models.DecimalField(max_digits=5, decimal_places=1)
    sugar = models.DecimalField(max_digits=5, decimal_places=1)
    caffeine = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return "Nutrients for " + self.drinks.name_Korean #accessing in more private way?

    class Meta:
        db_table = 'nutrients'

class Category(models.Model):
    category_name = models.CharField(max_length=45)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'
