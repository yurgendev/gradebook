from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def events(request):
    return HttpResponse("<h1>this is events page</h1>")

def main_page(request):
    return HttpResponse("<h1>this is main page</h1>")
