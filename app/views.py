# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def cookie_form(request):
    return render(request, 'app/cookie_form.html')

@csrf_exempt
def set_cookies(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Default Name')
        age = request.POST.get('age', 'Default Age')
        city = request.POST.get('city', 'Default City')
        
        response = HttpResponse("Cookies are set.")
        response.set_cookie('name', name, max_age=3600)  # 1 hour
        response.set_cookie('age', age, max_age=3600)    # 1 hour
        response.set_cookie('city', city, max_age=3600)  # 1 hour
        return response
    else:
        return HttpResponse("Invalid request method.")

def get_cookies(request):
    name = request.COOKIES.get('name', 'Not Set')
    age = request.COOKIES.get('age', 'Not Set')
    city = request.COOKIES.get('city', 'Not Set')
    
    return HttpResponse(f'Name: {name}, Age: {age}, City: {city}')

@csrf_exempt
def delete_cookies(request):
    if request.method == 'POST':
        response = HttpResponse("Cookies are deleted.")
        response.delete_cookie('name')
        response.delete_cookie('age')
        response.delete_cookie('city')
        return response
    else:
        return HttpResponse("Invalid request method.")
