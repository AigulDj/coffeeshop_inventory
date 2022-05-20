from django.db import models

# MenuItem, Ingredient, Recipe, Purchase

class MenuItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.FloatField(default=0.00)
    
    def get_absolute_url(self):
        return '/menu'
    
    def available(self):
        return all(x.enough() for x in self.recipe_set.all())
    
    # class Meta:
    #     ordering = ['title']
    #     verbose_name = 'menu item'
    
    def __str__(self):
        return f'{self.title}; {self.price}'
    
    
class Ingredient(models.Model):
    UNIT_CHOICES = [
        ('kg', 'kg'),
        ('gr', 'gr'),
        ('ltr', 'liter'),
        ('tbs', 'tbs'),
        ('tsp', 'tsp'),
    ]
    name = models.CharField(max_length=100, unique=True)
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=4, choices=UNIT_CHOICES, default='gr')
    unit_price = models.FloatField(default=0)
    
    def get_absolute_url(self):
        return '/ingredients'
    
    
    def __str__(self):
        return f'{self.name}; {self.quantity}; {self.unit}; {self.unit_price}'


class Recipe(models.Model):
    UNIT_CHOICES = [
        ('kg', 'kg'),
        ('gr', 'gr'),
        ('ltr', 'liter'),
        ('tbs', 'tbs'),
        ('tsp', 'tsp'),
    ]
    
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE) # Delete item in menu too
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE) # models.PROTECT Won't delete item in ingredient
    quantity = models.FloatField(default=0)
       
    def __str__(self):
        return f'[{self.menu_item.__str__()}]; {self.ingredient.name}; {self.quantity}'
    
    def get_absolute_url(self):
        return '/menu'
    
    def enough(self):
        return self.quantity <= self.ingredient.quantity
    
    
class Purchase(models.Model):
    menu_item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     ordering = ['timestamp']
        
    def __str__(self):
        return f'[{self.menu_item.__str__()}]; {self.timestamp}'
    
    def get_absolute_url(self):
        return '/purchase'