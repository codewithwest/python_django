from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse(
        "<center><h1><b>Welcome To Vortex_Tinker</b><h1></center>"
    )


def profile(request):
    return HttpResponse(
        "<center><h1><b>Welcome To Vortex_Tinker Profile</b><h1></center>"
    )


def method(request):
    path = request.path
    method = request.method
    scheme = request.scheme
    address = request.META['REMOTE_ADDR']
    agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    content = ''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p> 
<p>Request Scheme :{}</p>  
<p>Request Address :{}</p> 
<p>Request Agent :{}</p> 
<p>Request PAth Info :{}</p></center> 
'''.format(path, method, scheme, address, agent, path_info)
    return HttpResponse(content)


# Create your views here.


def drinks(request, drink_name):
    drink = {
        'mocha': 'type of coffee',
        'tea': 'type of beverage',
        'lemonade': 'type of refreshment',
    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)
