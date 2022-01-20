from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

	return HttpResponse("<h1>This is the index page</h1>")

def staff(request):

	return HttpResponse("<h1>This is the staff page</h1>")