from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Technique_model, Engine_model, Transmission_model, Drive_axle_model, Steerable_axle_model,\
    Type_maintenance,Description_failure, Recovery_method, Service_company, Machine_components, Car, Maintenance,Complaints
from .serializers import Technique_modelSerializer, Engine_modelSerializer, Transmission_modelSerializer, \
    Drive_axle_modelSerializer,Type_maintenanceSerializer,Description_failureSerializer, Recovery_methodSerializer, \
    Service_companySerializer, Machine_componentsSerializer,Base_CarSerializer, Full_CarSerializer, MaintenanceSerializer, \
    ComplaintsSerializer, Car_InfoSerializer,Car_InfoGetSerializer, MaintenanceGetSerializer, Service_companyGetSerializer,\
    ComplaintsGetSerializer
from itertools import chain
from .permissions import IsUserAuthenticated


class Technique_modelViewSet(viewsets.ModelViewSet):
    '''Справочник Модели техники'''
    queryset = Technique_model.objects.all()
    serializer_class = Technique_modelSerializer
    permission_classes = (IsUserAuthenticated,)


class Engine_modelViewSet(viewsets.ModelViewSet):
    '''Справочник Модель двигателя'''
    queryset = Engine_model.objects.all()
    serializer_class = Engine_modelSerializer


class Transmission_modelViewSet(viewsets.ModelViewSet):
    '''Справочник Модель трансмиссии'''
    queryset = Transmission_model.objects.all()
    serializer_class = Transmission_modelSerializer


class Steerable_axle_modelViewSet(viewsets.ModelViewSet):
    '''Справочник Модель ведущего моста'''
    queryset = Steerable_axle_model.objects.all()
    serializer_class = Drive_axle_modelSerializer


class Drive_axle_modelViewSet(viewsets.ModelViewSet):
    '''Справочник Модель управляемого моста'''
    queryset = Drive_axle_model.objects.all()
    serializer_class = Drive_axle_modelSerializer


class Type_maintenanceViewSet(viewsets.ModelViewSet):
    '''Справочник Вид ТО'''
    queryset = Type_maintenance.objects.all()
    serializer_class = Type_maintenanceSerializer


class Description_failureViewSet(viewsets.ModelViewSet):
    '''Справочник Характер отказа'''
    queryset = Description_failure.objects.all()
    serializer_class = Description_failureSerializer


class Recovery_methodViewSet(viewsets.ModelViewSet):
    '''Справочник Способ восстановления'''
    queryset = Recovery_method.objects.all()
    serializer_class = Recovery_methodSerializer


class Machine_componentsViewSet(viewsets.ModelViewSet):
    '''Справочник Узлы машины'''
    queryset = Machine_components.objects.all()
    serializer_class = Machine_componentsSerializer


class Service_companyViewSet(viewsets.ModelViewSet):
    '''Справочник Сервисные компании'''
    queryset = Service_company.objects.all()
    serializer_class = Service_companySerializer


class Service_companyGetViewSet(viewsets.ModelViewSet):
    '''Справочник Сервисные компании'''
    queryset = Service_company.objects.all()
    serializer_class = Service_companyGetSerializer


class Base_CarViewSet(viewsets.ModelViewSet):
    '''Полная информация о машине'''
    queryset = Car.objects.all()
    serializer_class = Base_CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        Factory_number = self.request.query_params.get('factory_number', None)
        if Factory_number is not None:
            queryset = queryset.filter(factory_number=Factory_number)
            return queryset
        return 'None'


class Full_CarViewSet(viewsets.ModelViewSet):
    '''Базовая информация о машине'''
    queryset = Car.objects.all()
    serializer_class = Full_CarSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        Type_company = self.request.query_params.get('type_company', None)
        if Type_company=='manufacturer':
            return queryset
        if Type_company=='service_company':
            Service_company = self.request.query_params.get('id_company', None)
            if Service_company is not None:
                queryset = queryset.filter(service_company__name=Service_company)
                return queryset
        if Type_company=='client':
            Client = self.request.query_params.get('id_company', None)
            if Client is not None:
                queryset = queryset.filter(client=Client)
                return queryset
        return 'None'


class Full_CarGetViewSet(viewsets.ModelViewSet):
    '''Базовая информация о машине'''
    queryset = Car.objects.all()
    serializer_class = Car_InfoGetSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        Type_company = self.request.query_params.get('type_company', None)
        if Type_company=='manufacturer':
            return queryset
        if Type_company=='service_company':
            Service_company = self.request.query_params.get('id_company', None)
            if Service_company is not None:
                queryset = queryset.filter(service_company__name=Service_company)
                return queryset
        if Type_company=='client':
            Client = self.request.query_params.get('id_company', None)
            if Client is not None:
                queryset = queryset.filter(client=Client)
                return queryset
        return 'None'


class Car_InfoViewSet(viewsets.ModelViewSet):
    '''Базовая информация о машине'''
    queryset = Car.objects.all()
    serializer_class = Car_InfoSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        Id = self.request.query_params.get('id', None)
        if Id is not None:
            queryset = queryset.filter(id=Id)
        return queryset


class MaintenanceViewSet(viewsets.ModelViewSet):
    '''Информация о ТО'''
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

    def get_queryset(self):
        queryset = Maintenance.objects.all()
        Id = self.request.query_params.get('id', None)
        car = self.request.query_params.get('car', None)
        if Id is not None:
            queryset = queryset.filter(id=Id)
        if car is not None:
            queryset = queryset.filter(car=car)
        return queryset


class MaintenanceGetViewSet(viewsets.ModelViewSet):
    '''Информация о ТО'''
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceGetSerializer

    def get_queryset(self):
        queryset = Maintenance.objects.all()
        Id = self.request.query_params.get('id', None)
        car = self.request.query_params.get('car', None)
        typecompany = self.request.query_params.get('typecompany', None)
        company = self.request.query_params.get('company', None)
        if Id is not None:
            queryset = queryset.filter(id=Id)
        if car is not None:
            queryset = queryset.filter(car=car)
        if typecompany is not None:
            if typecompany == "manufacturer":
                return queryset
            if typecompany == "service_company":
                queryset = queryset.filter(service_company__name__name=company)
                return queryset
            if typecompany == "client":
                carqueryset = Car.objects.all()
                carqueryset = carqueryset.filter(client=company)
                result_list = []
                for car in carqueryset:
                    querysetfull = queryset.filter(car=car.id)
                    result_list = list(chain(result_list, querysetfull))
                return result_list
        return queryset


class ComplaintsViewSet(viewsets.ModelViewSet):
    '''Рекламации'''
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsSerializer

    def get_queryset(self):
        queryset = Complaints.objects.all()
        Id = self.request.query_params.get('id', None)
        car = self.request.query_params.get('car', None)
        if Id is not None:
            queryset = queryset.filter(id=Id)
        if car is not None:
            queryset = queryset.filter(car=car)
        return queryset


class ComplaintsGetViewSet(viewsets.ModelViewSet):
    '''Рекламации'''
    queryset = Complaints.objects.all()
    serializer_class = ComplaintsGetSerializer

    def get_queryset(self):
        queryset = Complaints.objects.all()
        Id = self.request.query_params.get('id', None)
        car = self.request.query_params.get('car', None)
        typecompany=self.request.query_params.get('typecompany', None)
        company=self.request.query_params.get('company', None)
        if Id is not None:
            queryset = queryset.filter(id=Id)
        if car is not None:
            queryset = queryset.filter(car=car)
        if typecompany is not None:
            if typecompany=="manufacturer":
                return queryset
            if typecompany=="service_company":
                queryset = queryset.filter(service_company__name__name=company)
                return queryset
            if typecompany=="client":
                carqueryset=Car.objects.all()
                carqueryset=carqueryset.filter(client=company)
                result_list=[]
                for car in carqueryset:
                    querysetfull = queryset.filter(car=car.id)
                    result_list = list(chain(result_list, querysetfull))
                return result_list
        return queryset