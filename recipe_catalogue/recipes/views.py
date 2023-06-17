from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {'name':'jonny'}
    return render(request,'recipes/index.html',context=context)