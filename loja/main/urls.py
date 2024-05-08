from django.urls import path,include
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('category-list',views.category_list,name='category-list'),
    path('marca-list',views.marca_list,name='marca-list'),
    path('product-list',views.product_list,name='product-list'),
    path('category-product-list/<int:cat_id>',views.category_product_list,name='category-product-list'),
    path('marca-product-list/<int:marca_id>',views.marca_product_list,name='marca-product-list'),
    path('product/<str:slug>/<int:id>',views.product_detail,name='product-detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)