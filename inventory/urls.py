from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("logout/", views.log_out, name="logout"),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('', views.Home.as_view(), name='home'),
    path('ingredients/', views.IngredientList.as_view(), name='ingredientlist'),
    path('ingredients/create', views.IngredientCreate.as_view(), name='ingredientcreate'),
    path('ingredients/update/<pk>', views.IngredientUpdate.as_view(), name='ingredientupdate'),
    path('menu/', views.MenuItemList.as_view(), name='menuitemlist'),
    path('menu/create', views.MenuItemCreate.as_view(), name='menuitemcreate'),
    #path('menuitem/update/<pk>', views.MenuItemUpdate.as_view(), name='menuitemupdate'),
    path('recipe/create', views.RecipeCreate.as_view(), name='recipecreate'),
    path('purchases/', views.PurchaseList.as_view(), name='purchaselist'), 
    path('purchases/new', views.PurchaseCreate.as_view(), name='purchasecreate'),
    path('reports', views.ReportView.as_view(), name="reports"),
    #path('menuitem/delete/<pk>', views.MenuItemDelete.as_view(), name='menuitemdelete'),
]
