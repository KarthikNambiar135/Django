from django.shortcuts import render
from .forms import DemoForm

# Create your views here.
def home(request):
    form = DemoForm()
    return render(request, "myapp/home.html", {"form": form})