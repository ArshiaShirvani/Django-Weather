import requests
from django.shortcuts import render

def weather_view(request):
    city = '' 
    temperature = None
    description = ''
    icon = ''

    if request.method == 'POST': 
        city = request.POST.get('city', 'Tehran')  
        api_key = "YOUR API KEY"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:  
            data = response.json()
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']
        else:
            description = 'شهر مورد نظر پیدا نشد!'

    return render(request, 'index.html', {
        'city': city,
        'temperature': temperature,
        'description': description,
        'icon': icon,
    })
