from django.urls import path
from . import views


# urlpatterns = [
#     path('', views.home),
# ]

urlpatterns = [
    path('home/', views.home),
    path('dishes/<str:dish>', views.menuitems)
]