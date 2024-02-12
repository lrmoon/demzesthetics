from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index-03.html')

def index2(request):
    return render(request, 'index.html')

def demi(request):
    return render(request, './pages/demi.html')

def yaz(request):
    return render(request, './pages/yaz.html')

def services(request):
    return render(request, './pages/service.html')
