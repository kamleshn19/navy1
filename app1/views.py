from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
    return render(request,'a.html',{'title':'MariLog for Irish Navy','link':' http://127.0.0.1:8000/'})