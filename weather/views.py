import requests
from django.shortcuts import render

def weather_view(request):
    city = ''  # پیش‌فرض نام شهری انتخاب نشده
    temperature = None
    description = ''
    icon = ''

    if request.method == 'POST':  # اگر فرم ارسال شده باشد
        city = request.POST.get('city', 'Tehran')  # مقدار پیش‌فرض: تهران
        api_key = '0642217953ecf5f2cc625a73bbb46cb1'  # کلید API خودتان از OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}"
        response = requests.get(url)
        if response.status_code == 200:  # درخواست موفقیت‌آمیز
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
