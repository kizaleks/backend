from django.urls import path
from .views import *

urlpatterns = [
    path('Technique_model/', Technique_modelViewSet.as_view({'get': 'list','post': 'create'})),
    path('Technique_model/<int:pk>/',Technique_modelViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Engine_model/', Engine_modelViewSet.as_view({'get': 'list','post': 'create'})),
    path('Engine_model/<int:pk>/',Engine_modelViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Transmission_model/', Transmission_modelViewSet.as_view({'get': 'list','post': 'create'})),
    path('Transmission_model/<int:pk>/',Transmission_modelViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Steerable_axle_model/', Steerable_axle_modelViewSet.as_view({'get': 'list','post': 'create'})),
    path('Steerable_axle_model/<int:pk>/',Steerable_axle_modelViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Drive_axle_model/', Drive_axle_modelViewSet.as_view({'get': 'list','post': 'create'})),
    path('Drive_axle_model/<int:pk>/',Drive_axle_modelViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Type_maintenance/', Type_maintenanceViewSet.as_view({'get': 'list','post': 'create'})),
    path('Type_maintenance/<int:pk>/',Type_maintenanceViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Description_failure/', Description_failureViewSet.as_view({'get': 'list','post': 'create'})),
    path('Description_failure/<int:pk>/',Description_failureViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Recovery_method/', Recovery_methodViewSet.as_view({'get': 'list','post': 'create'})),
    path('Recovery_method/<int:pk>/',Recovery_methodViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Machine_components/', Machine_componentsViewSet.as_view({'get': 'list','post': 'create'})),
    path('Machine_components/<int:pk>/',Machine_componentsViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Service_companyGet/', Service_companyGetViewSet.as_view({'get': 'list'})),
    path('Service_company/', Service_companyViewSet.as_view({'get': 'list','post': 'create'})),
    path('Service_company/<int:pk>/',Service_companyViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Base_Car/', Base_CarViewSet.as_view({'get': 'list'})),
    path('Full_Car/', Full_CarViewSet.as_view({'get': 'list'})),
    path('Full_Car_Get/', Full_CarGetViewSet.as_view({'get': 'list'})),
    path('Car_Info/', Car_InfoViewSet.as_view({'get': 'list','post': 'create'})),
    path('Car_Info/<int:pk>/',Car_InfoViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('ComplaintsGet/', ComplaintsGetViewSet.as_view({'get': 'list'})),
    path('Complaints/', ComplaintsViewSet.as_view({'get': 'list','post': 'create'})),
    path('Complaints/<int:pk>/',ComplaintsViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('Maintenance/', MaintenanceViewSet.as_view({'get': 'list','post': 'create'})),
    path('Maintenance/<int:pk>/',MaintenanceViewSet.as_view({
             'patch': 'partial_update', 'delete': 'destroy'})),
    path('MaintenanceGet/', MaintenanceGetViewSet.as_view({'get': 'list'})),

]
