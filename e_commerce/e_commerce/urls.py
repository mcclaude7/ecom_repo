"""
URL configuration for e_commerce project.

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

from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/products/', include('products.urls')), 
    path('api/users/', include('users.urls')),
    path('auth/', include('rest_framework.urls')),  # For basic login/logout
    path('auth/token/', obtain_auth_token),  # For token-based auth (DRF Token)
    path('auth/jwt/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Auth
    path('auth/jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
