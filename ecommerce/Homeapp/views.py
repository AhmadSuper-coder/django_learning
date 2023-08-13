from django.shortcuts import render

# Create your views here.

def Home_view(request):
    return render(request, "index.html")


def Shop_view(request):
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
    return render(request, 'loing.html')

def register_veiw(request):
    return render(request,"register.html")