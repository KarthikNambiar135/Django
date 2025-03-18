from django.shortcuts import render

# Create your views here.
def menu(request):
    menuItems ={'mains': [
        {'name': 'Greek Salad', 'price': '15'},
        {'name': 'Chai', 'price': '12'},
        {'name': 'Coffee', 'price': '21'},
        ]}
    return render(request, 'menu.html', menuItems)