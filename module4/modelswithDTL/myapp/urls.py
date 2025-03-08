from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_by_id),
]
