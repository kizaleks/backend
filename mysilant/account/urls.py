from rest_framework import permissions
from rest_framework.authtoken import views
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from .views import ProfileViewSet, CustomAuthToken, CounterpartyViewSet

urlpatterns = [
    # path('token-auth/', views.obtain_auth_token),
    path('token-auth/', CustomAuthToken.as_view()),
    path('Profile/', ProfileViewSet.as_view({'get': 'list','post': 'create'})),
    path('Profile/<int:pk>/',ProfileViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Counterparty/', CounterpartyViewSet.as_view({'get': 'list','post': 'create'})),
    path('Counterparty/<int:pk>/',CounterpartyViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
]