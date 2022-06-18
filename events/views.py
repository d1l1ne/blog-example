from django.shortcuts import render
from .models import Event #импортируем класс

# Create your views here.
def home(request): #home функция
    events = Event.objects #получаем объекты модели
    return render(request, 'events/home.html', {'events':events}) #передаем объекты модели