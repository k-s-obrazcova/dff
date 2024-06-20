from django.urls import path, include
from .views import *

urlpatterns = [
    path('index/',home, name='home_page' ),
    path('suppliers/', supplier_list, name='catalog_supplier_page'),
    path('suppliers/details/<int:id>/', supplier_details, name='details_supplier_page'),
    path('suppliers/create/', supplier_create, name='create_supplier_page'),
    path('product/', product_list, name='catalog_product_page'),

    path('registration/', user_registration, name='regis'),
    path('login/', user_login, name = 'log in'),
    path('logout/', user_logout, name= 'log out'),

    path('anon/', anon, name='anon'),
    path('auth/', auth, name='auth'),
    path('can_add/', can_add_supplier, name='add'),
    path('can_add_change/', can_add_change_supplier, name='add_change'),
    path('change_address/', can_change_address, name='change_address'),




]