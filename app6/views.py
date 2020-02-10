from django.shortcuts import render

# Create your views here.
def searchCriteria(request):
    return render(request,'userHome.html',{'title':'Click on required Option','link':' http://127.0.0.1:8000/'})