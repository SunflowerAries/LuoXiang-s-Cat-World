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
    context = {'park': park, 'master': master,'master_store': master_store, 'park_wild': park_wild}
    return render(request, 'games/park_detail.html', context)

# path('<int:master_id>/sites/', views.sites, name='sites'),
#def sites(request,master_id):
#    site_list = Site.objects.order_by('-name')[:5]
#    master = get_object_or_404(Master, pk=master_id)
#    context = {'site_list': site_list,'master':master}
#    return render(request, 'games/sites.html', context)

# path('<int:master_id>/markets/', views.markets, name='markets'),
def markets(request,master_id):
    market_list = Market.objects.order_by('-name')[:5]
    master = get_object_or_404(Master, pk = master_id)
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

def park_cat(request, master_id, park_id, cat_id):
    park = get_object_or_404(Park, pk = park_id)
    master = get_object_or_404(Master, pk = master_id)
    park_cat = get_object_or_404(Cat, pk = cat_id)
    store = Store.objects.filter(master = master)
    context={'park': park, 'master': master, 'park_cat': park_cat, 'store': store}
    return render(request, 'games/park_cat.html', context)

def cat_detail(request, master_id, cat_id):
    master = get_object_or_404(Master, pk = master_id)
    cat = get_object_or_404(Cat, pk = cat_id)

    context={'master': master, 'cat': cat}
    return render(request, 'games/cat_detail.html', context)

def site_cat(request, master_id, site_id, cat_id):
    master = get_object_or_404(Master, pk = master_id)
    cat_list = get_object_or_404(Cat, pk = cat_id)
    site = get_object_or_404(Site, pk = site_id)
    context={'master': master, 'cat_list': cat_list, 'site': site}
    return render(request, 'games/site_cat.html', context)

def market_detail(request, master_id, market_id):
    master = get_object_or_404(Master, pk = master_id)
    market = get_object_or_404(Market, pk = market_id)
    market_food = Sell.objects.filter(market = market)
    context={'master': master, 'market': market, 'market_food': market_food}
    return render(request, 'games/market_detail.html', context)

def feed(request, master_id, park_id):
    print("in feed")
    food=request.POST['food']
    cat=request.POST['cat']
    print(food, cat)
    master = get_object_or_404(Master, pk = master_id)
    feed = Feed.objects.get_or_create(master = master, cat = cat)
    store = Store.objects.filter(master = master, food = food)
    if store.num == 1:
        store.delete()
    else:
        store.update(num = store.num - 1)

    feed.intimacy += 1
    feed.save()
    context={''}
    return
#def site_detail(request, master_id, site_id):
#    pass