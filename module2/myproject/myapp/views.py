from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(response):
#     return HttpResponse("Welcome to the homnepage of LittleLemons!")

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    
    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Method: {method}
        <br>Scheme: {scheme}
        <br>User Agent: {user_agent}
        <br>Path Info: {path_info}
        <br><br>
    """
    # response = HttpResponse("This showcases a success result, 200!")
    return HttpResponse(msg, content_type = 'text/html', charset='utf-8')
    # return response

def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a noodle.',
        'samosa': 'Samosa is a very famous Indian Snack.',
        'chai': "Never call it Chai-Tea!"
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description)