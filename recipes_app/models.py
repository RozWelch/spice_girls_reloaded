from django.db import models

# Create your models here.

from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=30, null=False,
                            blank=False)

    def __str__(self):
        return self.name


class Subcategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subcategories'

    name = models.CharField(max_length=30, null=False,
                            blank=False)

    def __str__(self):
        return self.name


class Recipe(models.Model):

    type_cooking = [('Stir Fry', 'Stir Fry'),
                    ('Oven', 'Oven'),
                    ('Stew', 'Stew'),
                    ('Grill', 'Grill',)
                    ]

    title = models.CharField(max_length=60, null=False,
                             blank=False)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,
                                    default='subcategory')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 default='category')
    image = models.URLField(null=False, blank=False)
    preparation = models.TextField(null=False,
                                   blank=False)
    preparation_time = models.IntegerField(null=False,
                                           blank=False)
    type_cooking = models.CharField(max_length=20, choices=type_cooking,
                                    null=False, blank=False)
    oven_time = models.IntegerField(null=False, blank=False)
    temperature = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    measure = [
        ('Teaspoon', 'Teaspoon'),
        ('Spoon', 'Spoon'),
        ('Cup', 'Cup'),
        ('Kilo', 'Kilo'),
    ]

    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                               default='recipe')
    product = models.CharField(max_length=50, null=True, blank=True)  # This
    # field will be replace with the product if its sell by the shop
    name = models.CharField(max_length=30, null=False, blank=False)
    quantity = models.FloatField(null=False, blank=False)
    measure = models.CharField(
        max_length=10, choices=measure, null=False, blank=False)

    def __str__(self):
        return self.name
