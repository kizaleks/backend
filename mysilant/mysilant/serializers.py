from rest_framework import serializers
from .models import Technique_model, Engine_model, Transmission_model, Drive_axle_model, Steerable_axle_model,\
    Type_maintenance,Description_failure, Recovery_method, Service_company, Machine_components, Car,\
    Maintenance, Complaints

class Technique_modelSerializer(serializers.ModelSerializer):
    '''Справочник Модели техники'''
    class Meta:
        model = Technique_model
        fields = ['id','name','description']


class Engine_modelSerializer(serializers.ModelSerializer):
    '''Справочник Модель двигателя'''
    class Meta:
        model = Engine_model
        fields = ['id','name','description']


class Transmission_modelSerializer(serializers.ModelSerializer):
    '''Справочник Модель трансмиссии'''
    class Meta:
        model = Transmission_model
        fields = ['id','name','description']


class Drive_axle_modelSerializer(serializers.ModelSerializer):
    '''Справочник Модель ведущего моста'''
    class Meta:
        model = Drive_axle_model
        fields = ['id','name','description']

class Steerable_axle_modelSerializer(serializers.ModelSerializer):
    '''Справочник Модель управляемого моста'''
    class Meta:
        model = Steerable_axle_model
        fields = ['id','name','description']


class Type_maintenanceSerializer(serializers.ModelSerializer):
    '''Справочник Вид ТО'''
    class Meta:
        model = Type_maintenance
        fields = ['id','name','description']


class Description_failureSerializer(serializers.ModelSerializer):
    '''Справочник Характер отказа'''
    class Meta:
        model = Description_failure
        fields = ['id','name','description']


class Recovery_methodSerializer(serializers.ModelSerializer):
    '''Справочник Способ восстановления'''
    class Meta:
        model = Recovery_method
        fields = ['id','name','description']

class Machine_componentsSerializer(serializers.ModelSerializer):
    '''Справочник Узлы машины'''
    class Meta:
        model = Machine_components
        fields = ['id','name','description']

class Service_companySerializer(serializers.ModelSerializer):
    '''Справочник Сервисные компании'''
    class Meta:
        model = Service_company
        fields = ['id','name','description']

class Service_companyGetSerializer(serializers.Serializer):
    '''Справочник Сервисные компании'''
    id = serializers.CharField()
    name = serializers.CharField(source='name.name', max_length=200)
    description = serializers.CharField()
    class Meta:
        fields = ['id','name','description']

class Base_CarSerializer(serializers.Serializer):
    '''Базовая информация о машине'''
    # id = serializers.CharField()
    factory_number = serializers.CharField()
    technique_model = serializers.CharField()
    engine_model = serializers.CharField(source='engine_model.name', max_length=200)
    engine_number = serializers.CharField()
    transmission_model = serializers.CharField(source='transmission_model.name', max_length=200)
    transmission_number = serializers.CharField()
    drive_axle_model = serializers.CharField(source='drive_axle_model.name', max_length=200)
    drive_axle_number = serializers.CharField()
    steerable_axle_model= serializers.CharField(source='steerable_axle_model.name', max_length=200)
    steerable_axle_number=serializers.CharField()
    class Meta:
        fields = ['factory_number','technique_model','engine_model','engine_number','transmission_model',
                  'transmission_number','drive_axle_model','drive_axle_number','steerable_axle_model',
                  'steerable_axle_number']


class Full_CarSerializer(serializers.ModelSerializer):
    '''Полная информация о машине'''
    class Meta:
        model = Car
        fields = ['id','factory_number','technique_model','engine_model','engine_number','transmission_model',
                  'transmission_number','drive_axle_model','drive_axle_number','steerable_axle_model',
                  'steerable_axle_number','supply_contract','date_of_shipment_from_the_factory','consignee'
                  ,'delivery_address','equipment','client','service_company']

class Car_InfoSerializer(serializers.ModelSerializer):
    '''Полная информация о машине'''
    class Meta:
        model = Car
        fields = ['id','factory_number','technique_model','engine_model','engine_number','transmission_model',
                  'transmission_number','drive_axle_model','drive_axle_number','steerable_axle_model',
                  'steerable_axle_number','supply_contract','date_of_shipment_from_the_factory','consignee'
                  ,'delivery_address','equipment','client','service_company']

class Car_InfoGetSerializer(serializers.Serializer):
    '''Справочник Модели техники'''
    id= serializers.CharField()
    factory_number=serializers.CharField()
    date_of_shipment_from_the_factory=serializers.DateField()
    technique_model=serializers.CharField(source='technique_model.name', max_length=200)
    engine_model = serializers.CharField(source='engine_model.name', max_length=200)
    transmission_model=serializers.CharField(source='transmission_model.name', max_length=200)
    drive_axle_model=serializers.CharField(source='drive_axle_model.name', max_length=200)
    steerable_axle_model=serializers.CharField(source='steerable_axle_model.name', max_length=200)
    service_company=serializers.CharField(source='service_company.name.name', max_length=200)

    class Meta:
        # model = Profile
        fields = ['id','factory_number','date_of_shipment_from_the_factory','technique_model','engine_model',
                  'transmission_model','drive_axle_model','steerable_axle_model','service_company']

class MaintenanceGetSerializer(serializers.Serializer):
    '''Информация о ТО'''
    id = serializers.CharField()
    car = serializers.CharField(source='car.factory_number', max_length=200)
    service_company =serializers.CharField(source='service_company.name.name', max_length=200)
    type_maintenance = serializers.CharField(source='type_maintenance.name', max_length=200)
    maintenance_date = serializers.DateField()

    class Meta:
        fields = ['id','car','service_company','type_maintenance','maintenance_date']


class MaintenanceSerializer(serializers.ModelSerializer):
    '''Информация о ТО'''
    class Meta:
        model = Maintenance
        fields = ['id','car','service_company','type_maintenance','maintenance_date',
                  'operating_time','order','order_date','company_executor']


class ComplaintsSerializer(serializers.ModelSerializer):
    '''Рекламации'''
    class Meta:
        model = Complaints
        fields = ['id','date_of_refusal','operating_time','Machine_components','failure_node',
                  'recovery_method','parts_used','date_of_restoration','equipment_downtime','car','service_company']

class ComplaintsGetSerializer(serializers.Serializer):
    '''Рекламации'''
    id = serializers.CharField()
    date_of_refusal=serializers.DateField();
    car = serializers.CharField(source='car.factory_number', max_length=200)
    service_company = serializers.CharField(source='service_company.name.name', max_length=200)
    Machine_components = serializers.CharField(source='Machine_components.name', max_length=200)
    recovery_method = serializers.CharField(source='recovery_method.name', max_length=200)

    class Meta:

        fields = ['id','date_of_refusal','Machine_components','recovery_method','car','service_company']