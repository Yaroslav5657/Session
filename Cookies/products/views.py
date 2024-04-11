from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Avg
from .models import Product, Rating 
from datetime import datetime 

def home(request):
    age_cookie = request.COOKIES.get('user_age')
    if age_cookie:
        age = int(age_cookie)
    else:
            age = None

    page_loads = request.session.get('page_loads', 0)
    page_loads += 1
    request.session['page_loads'] = page_loads
    
    color = 'pink' if page_loads % 2 == 0 else 'white'
    
    alternate_color = '#333' if page_loads % 3 == 0 else None

    products = Product.objects.annotate(average_rating=Avg('rating__rating'))

    rating_range = range(1, 11)

    return render(request, 'home.html', {'products': products, 'rating_range': rating_range, 'color': color, 'alternate_color': alternate_color})

def home_18plus(request):
    age_cookie = request.COOKIES.get('user_age')
    if age_cookie:
        age = int(age_cookie)
    else:
        age = None
    if age and age >= 18:
        return render(request, 'home_18plus.html',{'age': age})
    else: 
        return redirect('')

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def add_rating(request, product_id):
    if request.method == 'POST':
        rating_value = int(request.POST.get('rating'))
        product = Product.objects.get(pk=product_id)
        Rating.objects.create(product=product, rating=rating_value)
    return redirect('home')

def set_age(request):
    if request.method == 'POST':
        birth_date_str = request.POST.get('birth_date')
        birth_date = datetime.strptime(birth_date_str, '%Y-%m-%d')
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

        response = None
        if age >= 18:
            response = redirect('home_18plus')
        else:
            response = redirect('home')

        response.set_cookie('user_age', age, max_age=30*24*60*60)
        return response

    return render(request, 'set_age.html')

# Create your views here.
