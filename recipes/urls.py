
from django.urls import path
from . import views

urlpatterns = [
    path('', views.recipe_list),
    path('<int:pk>/', views.recipe_detail),
]