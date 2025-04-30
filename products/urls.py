from django.urls import path

from products import views

urlpatterns = [
    path('products/',views.showProducts),
    path('allProducts/',views.get_allProducts),
    path('product/<int:product_id>',views.get_product),
    path('insertproduct/',views.insertProduct),
    path('createcategory/',views.createcategory),
]