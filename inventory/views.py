from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
#from django.http import Http404

from .models import Ingredient, MenuItem, Recipe, Purchase

class Home(TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        return context

# LIST
class IngredientList(ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
    
class MenuItemList(ListView):
    model = MenuItem
    template_name = 'inventory/menuitem_list.html'
    
# Class RecipeList(ListView):
#     model = Recipe
#     template_name = 'inventory/recipe_list.html'
    
class PurchaseList(ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'

# DELETE  
 
class IngredientDelete(DeleteView):
    model = Ingredient
    template_name = 'inventory/ingredient_delete.html'
    
class MenuItemDelete(DeleteView):
    model = MenuItem
    template_name = 'inventory/menuitem_delete.html'

# CREATE  
class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create.html'
    fields = ['name', 'quantity', 'unit_price', 'unit']
    
class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'inventory/menuitem_create.html'
    fields = ['price', 'title']
    
class RecipeCreate(CreateView):
    model = Recipe
    template_name = 'inventory/recipe_create.html'
    fields = ['menuitem', 'ingredient', 'quantity']
    
# UPDATE

class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update.html'
    fields = ['name', 'quantity', 'unit_price', 'unit']
    
class MenuItemUpdate(UpdateView):
    model = MenuItem
    template_name = 'inventory/menuitem_update.html'
    fields = ['price', 'title']