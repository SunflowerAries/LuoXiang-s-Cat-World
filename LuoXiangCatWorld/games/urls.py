from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('register_func/', views.register_func, name='register_func'),
    path('login_func/', views.login_func, name='login_func'),
    path('<int:master_id>/', views.detail, name='detail'),
    path('<int:master_id>/cats/', views.cats, name='cats'),
    path('<int:master_id>/parks/', views.parks, name='parks'),
    path('<int:master_id>/parks/<int:park_id>/', views.park_detail, name='park_detail'),
    #path('<int:master_id>/sites/', views.sites, name='sites'),
    path('<int:master_id>/markets/', views.markets, name='markets'),
    path('<int:master_id>/parks/<int:park_id>/<int:cat_id>/', views.park_cat, name='park_cat'),
    path('<int:master_id>/cats/<int:cat_id>/', views.cat_detail, name='cat_detail'),
    path('<int:master_id>/sites/<int:site_id>/<int:cat_id>/', views.site_cat, name='site_cat'),
    path('<int:master_id>/markets/<int:market_id>/', views.market_detail, name='market_detail'),
    #path('<int:master_id>/sites/<int:site_id>/', views.site_detail, name='site_detail'),
]