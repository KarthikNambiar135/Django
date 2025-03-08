from django.shortcuts import render

# Create your views here.
def about(request):
    about_content = {'about': 'Based in Chicago, Illinois, Little Lemon is a very calm restaurant.'}
    return render(request, "about.html", about_content)