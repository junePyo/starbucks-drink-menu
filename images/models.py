from django.db import models

class Image(models.Model):
    image_url = models.URLField(max_length=2000)
    drink = models.ForeignKey('Drink', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "image of " + self.drink.name_Korean
    class Meta:
        db_table = 'images'
