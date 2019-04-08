from django.shortcuts import get_object_or_404,render
from .models import *
from django.urls import reverse
# Create your views here.
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect

# path('', views.login, name='login'),
def login(request):
    print("inlogin")
    return render(request, 'games/login.html')

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
    park = get_object_or_404(Park, pk = park_id)
    master = get_object_or_404(Master, pk = master_id)
    master_store = Store.objects.filter(master = master)
    park_wild = Wild.objects.filter(park = park)
    context = {'park': park, 'master_store': master_store, 'park_wild': park_wild}
    return render(request, 'games/park_detail.html', context)

# path('<int:master_id>/sites/', views.sites, name='sites'),
def sites(request,master_id):
    site_list = Site.objects.order_by('-name')[:5]
    master = get_object_or_404(Master, pk=master_id)
    context = {'site_list': site_list,'master':master}
    return render(request, 'games/sites.html', context)

# path('<int:master_id>/markets/', views.markets, name='markets'),
def markets(request,master_id):
    market_list = Market.objects.order_by('-name')[:5]
    master = get_object_or_404(Master, pk=master_id)
    context = {'market_list': market_list,'master':master}
    return render(request, 'games/markets.html',context)

def sign_up(request):
    #TODO
    return render(request, 'games/sign_up.html')

def register(request):
    print("inregister")
    return render(request, 'games/register.html')


def register_func(request):
    print("in register func")
    username=request.POST['username']
    password=request.POST['password']
    sex=request.POST['sex']
    master = Master.objects.create(name=username,password=password,sex=sex)
    master.save()
    print(sex)
    return render(request,'games/detail.html',{'master':master})


def login_func(request):
    username=request.POST['username']
    password=request.POST['password']
    print(username)
    master = Master.objects.get(name__exact=username,password__exact=password)
    # print(master.name)
    if master:
        return render(request,'games/detail.html',{'master':master})
    else:
        return render(request,'games/login.html')

def park_cat(request):
    pass

def cat_detail(request):
    pass

def site_cat(request):
    pass

def market_food(request):
    pass

def site_detail(request):
    pass