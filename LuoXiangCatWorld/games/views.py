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
    catname=request.POST.get('catname')
    catsex=request.POST.get('catsex')
    cathealth=request.POST.get('cathealth')
    catage=request.POST.get('catage')
    cat_list=Adopt.objects.filter(master__name=master.name)
    food_list=Store.objects.filter(master__name=master.name)
    print("yes!")
    for cat_all in cat_list:
        print(cat_all.cat.name)
    
    if catname:
        print("in catname")
        cat_list = cat_list.filter(cat__name=catname)
    
    if catname and catsex!='All':
        print("in catsex")
        cat_list = cat_list.filter(cat__sex=catsex)
    
    if cathealth and cathealth!='All':
        print("in cathealth")
        cat_list = cat_list.filter(cat__health=cathealth)

    if catage:
        print("in catage")
        cat_list = cat_list.filter(cat__age=catage)
    
    cat_list_in=[]

    for cat_all in cat_list:
        print(cat_all.cat.name)
        cat_list_in.append(cat_all.cat)

    context={'master':master,'cat_list':cat_list_in,'food_list':food_list}
    return render(request, 'games/detail.html',context)

# path('<int:master_id>/cats/', views.cats, name='cats'),
def cats(request,master_id):
    catname=request.POST.get('catname')
    catsex=request.POST.get('catsex')
    cathealth=request.POST.get('cathealth')
    catage=request.POST.get('catage')
    if catname:
        cat_list = Cat.objects.filter(name=catname)
    else:
        cat_list = Cat.objects.order_by('-name')
    
    if catsex and catsex!='All':
        cat_list = cat_list.filter(sex=catsex)
    
    if cathealth and cathealth!='All':
        cat_list = cat_list.filter(health=cathealth)

    if catage:
        cat_list = cat_list.filter(age=catage)
    master = get_object_or_404(Master, pk=master_id)

    food_list=Store.objects.filter(master__id=master_id)
    context = {'cat_list': cat_list,'master':master,'food_list':food_list}
    return render(request, 'games/cats.html',context)

# path('<int:master_id>/parks/', views.parks, name='parks'),
def parks(request,master_id):
    park_list = Park.objects.order_by('-name')[:5]
    master = get_object_or_404(Master, pk=master_id)
    context = {'park_list': park_list,'master':master}
    return render(request, 'games/parks.html',context)

# path('<int:master_id>/parks/<int:park_id>/', views.park_detail, name='park_detail'),
def park_detail(request,master_id,park_id):
    master = get_object_or_404(Master, pk = master_id)

    food = request.POST.get('food')
    cat = request.POST.get('cat')

    print(food, cat)
    if cat and food:
        #print(cat, food)
        food = Food.objects.get(name = food)
        cat = Cat.objects.get(id = cat)
        feed, created = Feed.objects.get_or_create(master = master, cat = cat)
        store = Store.objects.get(master = master, food = food)
        if store.num == 1:
            store.delete()
        else:
            store.num = store.num - 1
            store.save()

        feed.intimacy += 1
        feed.save()

    park = get_object_or_404(Park, pk = park_id)
    master_store = Store.objects.filter(master = master)
    park_wild = Wild.objects.filter(park = park)
    context = {'park': park, 'master': master,'master_store': master_store, 'park_wild': park_wild}
    return render(request, 'games/park_detail.html', context)

def markets(request,master_id):
    market_list = Market.objects.order_by('-name')[:5]
    master = get_object_or_404(Master, pk = master_id)
    context = {'market_list': market_list,'master':master}
    return render(request, 'games/markets.html',context)

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
    master = Master.objects.get(name__exact=username,password__exact=password)

    catname=request.POST.get('catname')
    catsex=request.POST.get('catsex')
    cathealth=request.POST.get('cathealth')
    catage=request.POST.get('catage')
    
    cat_list=Adopt.objects.filter(master__name=master.name)
    food_list=Store.objects.filter(master__name=master.name)

    for cat_all in cat_list:
        print(cat_all.cat.name)
    
    if catname:
        print("in catname")
        cat_list = cat_list.filter(cat__name=catname)
    
    if catname and catsex!='All':
        print("in catsex")
        cat_list = cat_list.filter(cat__sex=catsex)
    
    if cathealth and cathealth!='All':
        print("in cathealth")
        cat_list = cat_list.filter(cat__health=cathealth)

    if catage:
        print("in catage")
        cat_list = cat_list.filter(cat__age=catage)
    
    cat_list_in=[]
    food_list_in=[]

    for cat_all in cat_list:
        print(cat_all.cat.name)
        cat_list_in.append(cat_all.cat)
    
    for food_all in food_list:
        print(food_all.food.name)
        food_list_in.append(food_all.food)
    
    context={'master':master,'cat_list':cat_list_in,'food_list':food_list_in}
    if master:
        return render(request,'games/detail.html',context)
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

def market_detail(request, master_id, market_id):
    master = get_object_or_404(Master, pk = master_id)
    market = get_object_or_404(Market, pk = market_id)
    act = request.POST.get('action')
    food = request.POST.getlist('food')
    num = request.POST.getlist('num')
    #food_list =
    print(food, num)
    if act and food and num:
        if act == 'buy':#buy
            for i in range(len(food)):
                if food[i] and num[i]:
                    myfood = Food.objects.get(id = int(food[i]))
                    buy = Sell.objects.get(market = market, food = myfood)
                    Num = int(num[i])
                    if Num > buy.num:
                        market_food = Sell.objects.filter(market = market)
                        myfood = myfood.name
                        context={'master': master, 'market': market, 'market_food': market_food, 'msg': "We can't offer so much " + myfood}
                        return render(request, 'games/market_detail.html', context)
                    elif master.money < Num * buy.price:
                        market_food = Sell.objects.filter(market = market)
                        context={'master': master, 'market': market, 'market_food': market_food, 'msg': "You don't have enough money"}
                        return render(request, 'games/market_detail.html', context)
                    else:
                        store, created = Store.objects.get_or_create(master = master, food = myfood)
                        master.money -= Num * buy.price
                        master.save()
                        if buy.num == Num:
                            buy.delete()
                        else:
                            buy.num -= Num
                            buy.save()
                        store.num += Num
                        store.save()
        else:#sell
            for i in range(len(food)):
                if food[i] and num[i]:
                    myfood = Food.objects.get(id = int(food[i]))
                    sell = Store.objects.get(master = master, food = myfood)
                    Num = int(num[i])
                    offer = Sell.objects.get(market = market, food = myfood)
                    if offer:
                        if Num > sell.num:
                            market_food = Sell.objects.filter(market = market)
                            myfood = myfood.name
                            context={'master': master, 'market': market, 'market_food': market_food, 'msg': "You don't have enough " + myfood}
                            return render(request, 'games/market_detail.html', context)
                        else:
                            master.money += Num * offer.price
                            master.save()
                            if sell.num == Num:
                                sell.delete()
                            else:
                                sell.num -= Num
                                sell.save()
                            offer.num += Num
                            offer.save()
                    else:
                        market_food = Sell.objects.filter(market = market)
                        myfood = myfood.name
                        context={'master': master, 'market': market, 'market_food': market_food, 'msg': "Sorry, We don't buy" + myfood}
                        return render(request, 'games/market_detail.html', context)


    market_food = Sell.objects.filter(market = market)
    context={'master': master, 'market': market, 'market_food': market_food}
    return render(request, 'games/market_detail.html', context)
