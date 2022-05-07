from django.db import models
from django.utils import timezone
import datetime


class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('kg', 'kg'),
        ('gr', 'gr'),
        ('ltr', 'liter'),
        ('tbs', 'tbs'),
        ('tsp', 'tsp'),
    ]
    name = models.CharField(max_length=15)
    quantity = models.FloatField(null=True)
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES, default='gr')
    unit_price = models.FloatField()
    
    def __str__(self):
        return self.name or ' '


class MenuItem(models.Model):
    title = models.CharField(max_length=15)
    price = models.FloatField()
    
    # class Meta:
    #     ordering = ['title']
    #     verbose_name = 'menu item'
    
    def __str__(self):
        return self.title or ' '

class Recipe(models.Model):
    UNIT_CHOICES = [
        ('kg', 'kg'),
        ('gr', 'gr'),
        ('ltr', 'liter'),
        ('tbs', 'tbs'),
        ('tsp', 'tsp'),
    ]
    
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE) # Delete item in menu too
    ingredient = models.ForeignKey('Ingredient', on_delete=models.PROTECT) # Won't delete item in ingredient
    quantity = models.FloatField(null=True)
    #name = models.CharField(max_length=15, null=True) # if new recipe, but if old then menu item, How to make it 
    
    def __str__(self):
        return str(self.menu_item) #-- {self.ingredient}"
    
    
class Purchase(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['timestamp']
        
    def __str__(self):
        return f'{self.menu_item} --- {self.timestamp}' # self.timestamp >= timezone.now() - datetime.timedelta(days=1)