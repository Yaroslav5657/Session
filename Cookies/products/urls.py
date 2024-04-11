from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home_18plus/', views.home_18plus, name='home_18plus'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('add_rating/<int:product_id>/', views.add_rating, name='add_rating'),
    path('set_age/', views.set_age, name='set_age'),
]