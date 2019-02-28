"""djosertest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include,re_path
from django.views.generic import TemplateView
# from rest_framework_simplejwt import views as jwt_views
from rest_auth.views import PasswordResetView,PasswordResetConfirmView,PasswordChangeView
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token,refresh_jwt_token,verify_jwt_token



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('djoser.urls')),
    # path('', include('mailtest.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('rest-auth/', include('rest_auth.urls')),
    url('api-token-auth/', obtain_jwt_token),
    url('api-token-refresh/', refresh_jwt_token),
    url('api-token-verify/', verify_jwt_token),

    re_path(r'^rest-auth/password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView,
        name='password_reset_confirm'),
    re_path(
        r'^rest-auth/password/reset/$',
        PasswordResetView,
        name='password_reset',
    ),

]
