from django.contrib import admin
from django.urls import path, include
from store.views import user_login, user_logout, product_list, add_to_cart, view_cart, place_order

urlpatterns = [
path('admin/', admin.site.urls),
path('login/', user_login, name='login'),
path('logout/', user_logout, name='logout'),
path('', product_list, name='product_list'),
path('add_to_cart//', add_to_cart, name='add_to_cart'),
path('cart/', view_cart, name='view_cart'),
path('place_order/', place_order, name='place_order'),
]