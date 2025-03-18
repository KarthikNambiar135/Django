from django.shortcuts import render
from .models import Menu

# Create your views here.
def menu_by_id(request):
    newMenu = Menu.objects.all()
    dict = {'menu': newMenu}
    return render(request, 'menu_card.html', dict)