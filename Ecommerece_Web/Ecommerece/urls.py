from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [

path("",Home,name='Home'),
path('login/',Login,name='Login'),
path('logout/',Logout,name='Logout'),
path('sign-in/',Sign_in,name='Sign-in'),
path('add-product/',Add_Products,name='Add-product'),
path('add-category/',Add_Category,name='Add-category'),
path('product/<str:product_id>/',Products,name='Product'),
path('edit-product/<str:product_id>/',Edit_Product,name='Edit-Product'),
path('edit-category/<str:cat_id>/',Edit_Category,name='Edit-Category'),
path('delete-category/<str:cat_id>/',Delete_Category,name='Delete-Category'),
path('delete-product/<str:product_id>/',Delete_Product,name='Delete-Product'),
path('product-by-catogery/<str:cat_id>/',Products_by_categories,name='Products-by-category'),
path('Cart/',Cart_page,name='Cart'),
path('Add_cart/',Add_cart,name='Add_cart'),
path('edit-cart-product/',Edit_cart_product,name='Edit-cart_product'),
path('delete-cart-product/',Delete_cart_product,name='Delete-cart_product'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)