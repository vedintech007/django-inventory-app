from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def error_404(request, exception):

    return render(request, 'dashboard/404.html')


def index(request):

    context = {}

    return render(request, 'dashboard/index.html', context)


def staff(request):

    context = {}

    return render(request, 'dashboard/staff.html', context)


def product(request):

    context = {}

    return render(request, 'dashboard/product.html', context)


def order(request):

    context = {}

    return render(request, 'dashboard/order.html', context)
