from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def Home_view(request):
    return render(request, "index.html")


def Shop_view(request):
    permission_classes = (IsAuthenticated,)
    return render(request, "shop.html")

def detail_view(request):
    return render(request, 'detail.html')

def cart_view(request):
    return render(request, 'cart.html')

def checkout_view(request):
    return render(request, 'checkout.html')

def contact_view(request):
    return render(request, 'contact.html')

def login_view(request):
    return render(request, 'login.html')

def register_veiw(request):
    return render(request,"register.html")


def user_profile_view(request):
    permission_classes = (IsAuthenticated,)
    return render(request,"user_profile.html")