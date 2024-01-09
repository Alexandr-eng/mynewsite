"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from api.views import UserRegistrationView, UserLoginView, WarehouseCreateView, ProductCreateView, SupplyProductView, RetrieveProductView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('warehouse/create/', WarehouseCreateView.as_view(), name='create_warehouse'),
    path('product/create/', ProductCreateView.as_view(), name='create_product'),
    path('product/supply//', SupplyProductView.as_view(), name='supply_product'),
    path('product/retrieve//', RetrieveProductView.as_view(), name='retrieve_product'),
]

