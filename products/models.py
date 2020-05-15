from django.db import models


class Drink(models.Model):
    name_Korean = models.CharField(max_length=50)
    name_English = models.CharField(max_length=50)
    description_main = models.CharField(max_length=300)
    description_sub = models.CharField(max_length=300)
    size = models.ForeignKey(
        'Size', on_delete=models.SET_NULL, null=True)
    nutrients = models.OneToOneField(
        'Nutrients', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, null=True)
    allergenes = models.ManyToManyField(
        'Allergy', through='DrinkAllergen', related_name='containing_drinks')

    def __str__(self):
        return self.name_Korean

    class Meta:
        db_table = 'drinks'


class Size(models.Model):
    size_name = models.CharField(max_length=50)
    size_ml = models.DecimalField(max_digits=5, decimal_places=1)
    size_fluid_ounce = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return self.size_name

    class Meta:
        db_table = 'sizes'


class Nutrients(models.Model):
    calorie = models.DecimalField(max_digits=5, decimal_places=1)
    fat = models.DecimalField(max_digits=5, decimal_places=1)
    protein = models.DecimalField(max_digits=5, decimal_places=1)
    sodium = models.DecimalField(max_digits=5, decimal_places=1)
    sugar = models.DecimalField(max_digits=5, decimal_places=1)
    caffeine = models.DecimalField(max_digits=5, decimal_places=1)

    def __str__(self):
        return "Nutrients for " + self.drinks.name_Korean

    class Meta:
        db_table = 'nutrients'


class Category(models.Model):
    category_name = models.CharField(max_length=45)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table = 'categories'


class Allergy(models.Model):
    allergene = models.CharField(max_length=20)

    def __str__(self):
        return self.allergene

    class Meta:
        db_table = 'allergies'


# middle table: many to many relationship between Allergy and Drink
class DrinkAllergen(models.Model):
    drink = models.ForeignKey('Drink', on_delete=models.SET_NULL, null=True)
    allergy = models.ForeignKey(
        'Allergy', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'drinks_allergies'


class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "image of " + self.drink.name_Korean

    class Meta:
        db_table = 'images'
