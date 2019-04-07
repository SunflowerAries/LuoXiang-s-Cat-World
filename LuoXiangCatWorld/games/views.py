from django.shortcuts import get_object_or_404,render
from .models import *
from django.urls import reverse
# Create your views here.
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect


# path('', views.login, name='login'),
def login(request):
    master_list = Master.objects.order_by('-name')[:5]
    context = {'master_list': master_list}
    return render(request, 'games/login.html',context)

# path('<int:master_id>/', views.detail, name='detail'),
def detail(request,master_id):
    master = get_object_or_404(Master, pk=master_id)
    return render(request, 'games/detail.html',{'master':master})

# path('<int:master_id>/cats/', views.cats, name='cats'),
def cats(request,master_id):
    cat_list = Cat.objects.order_by('-name')[:5]
    master = get_object_or_404(Master, pk=master_id)
    context = {'cat_list': cat_list,'master':master}
    return render(request, 'games/cats.html',context)

# path('<int:master_id>/parks/', views.parks, name='parks'),
def parks(request,master_id):
    park_list = Park.objects.order_by('-name')[:5]
    master = get_object_or_404(Master, pk=master_id)
    context = {'park_list': park_list,'master':master}
    return render(request, 'games/parks.html',context)

# path('<int:master_id>/parks/<int:park_id>/', views.park_detail, name='park_detail'),
def park_detail(request,master_id,park_id):
    #TODO
    return render(request, 'games/park_detail.html')

# path('<int:master_id>/sites/', views.sites, name='sites'),
def sites(request,master_id):
    #TODO
    return render(request, 'games/sites.html')

# path('<int:master_id>/markets/', views.markets, name='markets'),
def markets(request,master_id):
    market_list = Market.objects.order_by('-name')[:5]
    master = get_object_or_404(Master, pk=master_id)
    context = {'market_list': market_list,'master':master}
    return render(request, 'games/markets.html',context)

def sign_up(request):
    #TODO
    return render(request, 'games/sign_up.html')