from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(response):
    return HttpResponse("Welcome to the homnepage of LittleLemons!")