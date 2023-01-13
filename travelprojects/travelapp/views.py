from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from . models import package

# Create your views here.
def demo (request):
    obj = place.objects.all()
    x = package.objects.all()

    return render(request,"index.html",{'results': obj,'key':x})
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x+y
#     sub = x-y
#     mul = x*y
#     div = x/y
#     return render(request,"result.html",{'addition':add,'subst':sub,'mult':mul,'divi':div})
# def subst(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     sub = x-y
#     return render(request,"result.html",{'subst':sub})
# def mult(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     mul = x * y
#     return render(request, "result.html", {'mult': mul})
# def divi(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     div = x / y
#     return render(request, "result.html", {'divi': div})
