from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    # return HttpResponse("Hello, world! This is the home page of chaiaurDjango.")
    return render(request, 'website/index.html')
def About(request):
    return HttpResponse("This is the about page of chaiaurDjango. Here you can learn more about our project.")
def Contact(request):
    return HttpResponse("This is the contact page of chaiaurDjango. Feel free to reach out to us!")