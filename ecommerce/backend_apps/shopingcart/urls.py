from django.urls import path
from backend_apps.shopingcart import views


urlpatterns = [
  path('getcart/', views.CartDetails.as_view(), name='cart')

]
