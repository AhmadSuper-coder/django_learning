from django.urls import path
from . import views


urlpatterns = [
  path("",views.Home_view,name="home"),
  path("shop",views.Shop_view,name="shop"),
  path('detail/', views.detail_view, name='detail'),
  path('cart/', views.cart_view, name='cart'),
  path('checkout/', views.checkout_view, name='checkout'),
  path('contact/', views.contact_view, name='contact'),
  path('user_login/', views.login_view, name='user_login'),
  path('user_register/', views.register_veiw, name='user_register'),
  path('user_profile/', views.user_profile_view, name='user_profile')

]

