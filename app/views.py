from django.shortcuts import render
from django.http import HttpResponse

def set_cookies(request):
    response = HttpResponse("Cookies are set.")
    response.set_cookie('name', 'John Doe', max_age=3600)  # 1 hour
    response.set_cookie('age', '30', max_age=3600)         # 1 hour
    response.set_cookie('city', 'New York', max_age=3600)  # 1 hour
    return response

def get_cookies(request):
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')
    city = request.COOKIES.get('city')

    return HttpResponse(f'Name: {name}, Age: {age}, City: {city}')

def delete_cookies(request):
    response = HttpResponse("Cookies are deleted.")
    response.delete_cookie('name')
    response.delete_cookie('age')
    response.delete_cookie('city')
    return response
