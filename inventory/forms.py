from dataclasses import fields
from django import forms
from .models import MenuItem, Ingredient, Recipe, Purchase


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"
    
class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = "__all__"
        
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"
        
class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = "__all__"