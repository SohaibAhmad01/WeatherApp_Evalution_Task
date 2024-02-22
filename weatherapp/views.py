import asyncio
import aiohttp
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
from django.conf import settings
from .models import *
# Create your views here.

@csrf_exempt
def login(request):
    if request.method=="POST":
        username= request.POST.get('username')
        password= request.POST.get('password')
        # Authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            # Login user
            auth_login(request, user)
            return redirect('dashboard')  # Redirect to dashboard on successful login
        else:
            # Display error message or handle invalid credentials
            return render(request, 'weatherapp/login.html', {'error_message': 'Invalid username or password'})

    return render(request, 'weatherapp/login.html')

@login_required(login_url='login') #redirect when user is not logged in
def dashboard(request):
    fav=Favorate.objects.filter(user=request.user)
    return render(request, 'weatherapp/dashboard.html', context={"fav":fav})

'''
    Below function will use weather api to get weather data 
'''

async def get_weather_async(city):
    API_Key = settings.API_KEY
    Base_url = "http://api.openweathermap.org/data/2.5/weather"
    request_url = f"{Base_url}?appid={API_Key}&q={city}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(request_url) as response:
            data = await response.json()
            return {
                "city": data['name'],
                "temperature": data['main']['temp'],
                "humidity": data['main']['humidity'],
                "wind_speed": data['wind']['speed'],
                "weather_conditions": data['weather'][0]['description'],
            }
        

async def getweather(request):
    if request.method == "GET":
        city = request.GET.get('cityname')
        data = await get_weather_async(city)
        return JsonResponse(data)
    
'''
    Fav will be add with the user instance
'''
@login_required(login_url='login') #redirect when user is not logged in
def add_favorate(request):
    if request.method== "POST":
        # import pdb; pdb.set_trace()
        city=request.POST.get('cityvalue')
        if city:
            user=request.user
            fav=Favorate.objects.create(cityname=city,user=user)
            fav.save()
            return redirect('dashboard')
        return redirect('dashboard')
        