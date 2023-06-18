from django.http import HttpRequest, HttpResponse
from django.template import loader 
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .forms import DemoForm
from .models import Menu
# Create your views here.

def home(request):
    return render(request, 'index.html') 
def about(request):
    return render(request, 'about.html') 
def menu(request):
    return render(request, 'menu.html') 

def nav(request):
    context={} 
    return  render( request,'navigation.html',context)
     
def profile(request):
    return HttpResponse(
        "<center><h1><b>Welcome To Vortex_Tinker Profile</b><h1></center>"
    )
def forms(request):
    # name = forms.CharField()
    return HttpRequest(DemoForm)

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


def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {'menu':newmenu}
    return render(request,'menu_cards.html', newmenu_dict)
