from django.urls import path
from . import views

app_name = 'games'
urlpatterns = [
    path('', views.login, name='login'),
    path('<int:master_id>/', views.detail, name='detail'),
    path('<int:master_id>/cats/', views.cats, name='cats'),
    path('<int:master_id>/parks/', views.parks, name='parks'),
    path('<int:master_id>/parks/<int:park_id>/', views.park_detail, name='park_detail'),
    path('<int:master_id>/sites/', views.sites, name='sites'),
    path('<int:master_id>/markets/', views.markets, name='markets'),
    path('<int:master_id>/parks/<int:park_id>/<int:cat_id>/', views.park_cats, name='park_cats'),
    path('<int:master_id>/cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),
]