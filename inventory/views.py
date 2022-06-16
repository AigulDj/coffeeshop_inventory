from django.shortcuts import redirect

from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from .models import Ingredient, MenuItem, Recipe, Purchase
from .forms import IngredientForm, MenuItemForm, RecipeForm

import git
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Automatic deployments to a Django Web-App hosted on PythonAnywhere
@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo("aiguldj.eu.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
    
    
class Home(LoginRequiredMixin, TemplateView):
    template_name = "inventory/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ingredients"] = Ingredient.objects.all()
        context["menu_items"] = MenuItem.objects.all()
        context["purchases"] = Purchase.objects.all()
        return context

# INGREDIENT

class IngredientList(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'inventory/ingredient_list.html'
   
    
class IngredientCreate(CreateView):
    model = Ingredient
    template_name = 'inventory/ingredient_create.html'
    form_class = IngredientForm
   
    
class IngredientUpdate(UpdateView):
    model = Ingredient
    template_name = 'inventory/ingredient_update.html'
    form_class = IngredientForm
      
# MENUITEM 

class MenuItemList(ListView):
    model = MenuItem
    template_name = 'inventory/menuitem_list.html'

    
class MenuItemCreate(CreateView):
    model = MenuItem
    template_name = 'inventory/menuitem_create.html'
    form_class = MenuItemForm
            
# RECIPE 

class RecipeCreate(CreateView):
    model = Recipe
    template_name = 'inventory/recipe_create.html'
    form_class = RecipeForm
   
# PURCHASE

class PurchaseList(ListView):
    model = Purchase
    template_name = 'inventory/purchase_list.html'
    
    
class PurchaseCreate(TemplateView):
    template_name = 'inventory/purchase_create.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu_items'] = [x for x in MenuItem.objects.all() if x.available()]
        return context
    
    def post(self, request):
        menu_item_id = request.POST['menu_item']
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        requirements = menu_item.recipe_set.all()
        purchase = Purchase(menu_item=menu_item)

        for requirement in requirements.all():
            ingredient = requirement.ingredient
            ingredient.quantity -= requirement.quantity
            ingredient.save()

        purchase.save()
        return redirect("/purchases")
   
# REPORT

class ReportView(LoginRequiredMixin, TemplateView):
    template_name = "inventory/reports.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["purchases"] = Purchase.objects.all()
        revenue = Purchase.objects.aggregate(revenue=Sum("menu_item__price"))["revenue"]
        total_cost = 0
        items_count = {}
        
        for purchase in context["purchases"]:
            items_count[purchase.menu_item.title] = items_count.get(purchase.menu_item.title, 0)+1
            for recipe_requirement in purchase.menu_item.recipe_set.all():
                total_cost += recipe_requirement.ingredient.unit_price * recipe_requirement.quantity
        
        context['item_total'] = items_count
        context["revenue"] = revenue
        context["total_cost"] = total_cost
        if revenue:
            context["profit"] = revenue - total_cost

        return context
    
    
def log_out(request):
    logout(request)
    return redirect("/")