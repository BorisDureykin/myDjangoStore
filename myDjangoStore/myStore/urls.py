from django.urls import path

from myStore import views

app_name = 'myStore'

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('category/<int:id>/', views.categoryPage, name='categoryPage'),
    path('products/', views.productsPage, name='productsPage'),
    path('product/<int:id>/', views.productPage, name='productPage'),
    path('cart/', views.cartPage, name='cartPage'),


]
