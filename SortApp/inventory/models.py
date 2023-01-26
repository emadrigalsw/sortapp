from django.db import models
# from datetime import datetime

# Create your models here.

# Models of all the data that is going to be managed


class Ingredient(models.Model):
    """
    Stores all the ingredients to be displayed on the Pantry view,
    related to :view:`Pantry` and :view:`CreateIngredient`.
    """

    POUNDS = "PD"
    KILOGRAMS = "KG"
    GRAMS = "GR"
    MILLILITERS = "ML"
    LITERS = "LT"
    UNIT = "UN"
    SPOON = "SP"
    UNIT_CHOICES = [
        (POUNDS, "Pounds"),
        (KILOGRAMS, "Kilograms"),
        (GRAMS, "Grams"),
        (MILLILITERS, "Milliliters"),
        (LITERS, "Liters"),
        (UNIT, "Unit"),
        (SPOON, "Spoon"),
    ]

    name = models.CharField(max_length=30, unique=True)
    quantity = models.FloatField(default=0.0)
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES)
    price_per_unit = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/pantry"


class MenuItem(models.Model):
    """
    Stores all the Menus to be displayed to users
    related to :view:`` and :view:``.
    """
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/menu"


class Purchase(models.Model):
    """
    Stores all the Purchases to be displayed to users
    related to :view:`` and :view:``.
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    # The next is in the case we want to keep the registry of all Purchases associated to a menu,even if the menu_item is deleted
    # menu_item = models.ForeignKey(
    #     MenuItem, on_delete=models.SET_DEFAULT, default=set_deleted_message)

    # def set_deleted_message(MenuItem_title):
    #     now = datetime.now()
    #     return "Menú eliminado:{}_{}".format(MenuItem_title, now.strftime("%Y-%m-%d %H:%M:%S"))
    def __str__(self):
        return self.menu_item.title


class RecipeRequirement(models.Model):
    """
    Stores all the Recipes to be displayed to users
    related to :view:`` and :view:``.
    """
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return self.menu_item.title + " - " + self.ingredient.name
