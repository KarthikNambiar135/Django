from django.shortcuts import render
from .models import Menu
from .forms import BookingForm

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all().order_by('name')
    main_data = {'menu': menu_data}
    return render(request, 'menu.html', main_data)

def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''
    menu_dict = {'menu_item': menu_item}
    return render(request, 'menu_item.html', menu_dict)