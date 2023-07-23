from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, "index.html")


def Shop(request):
    return render(request, "shop.html")


def Test(request):
    return render(request,"test.html")