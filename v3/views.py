from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def index_zh(request):
    return render(request, 'index_zh.html')

def search(request):
    return render(request, 'search.html')

def search_zh(request):
    return render(request, 'search_zh.html')

def Update(request):
    return render(request, 'Update.html')

def Update_zh(request):
    return render(request, 'Update_zh.html')

