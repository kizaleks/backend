from django.db import models
from django.contrib.auth.models import User
from account.models import Counterparty

'''Справочники'''

class Technique_model(models.Model):
    '''Справочник Модели техники'''
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'


class Engine_model(models.Model):
    '''Справочник Модель двигателя'''
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'


class Transmission_model(models.Model):
    '''Справочник Модель трансмиссии'''
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'


class Drive_axle_model(models.Model):
    '''Справочник Модель ведущего моста'''
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущих мостов'


class Steerable_axle_model(models.Model):
    '''Справочник Модель управляемого моста'''
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемых мостов'

class Type_maintenance(models.Model):
    '''Справочник Вид ТО'''
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Вид ТО'

class Description_failure(models.Model):
    '''Справочник Характер отказа'''
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Характер отказа'


class Recovery_method(models.Model):
    '''Справочник Способ восстановления'''
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способ восстановления'

class Machine_components(models.Model):
    '''Справочник Узлы машины'''
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Узлы машины'
        verbose_name_plural = 'Узлы машины'

class Service_company(models.Model):
    '''Справочник Сервисные компании'''
    name = models.ForeignKey(Counterparty, on_delete=models.CASCADE)
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сервисные компании'
        verbose_name_plural = 'Сервисные компании'

class Car(models.Model):
    factory_number = models.TextField(max_length=17, unique=True, db_index=True, verbose_name='Заводской номер')
    technique_model = models.ForeignKey(Technique_model, on_delete=models.PROTECT , db_index=True, verbose_name='Модель техники')
    engine_model = models.ForeignKey(Engine_model, on_delete=models.PROTECT , db_index=True, verbose_name='Модель двигателя')
    engine_number = models.TextField(max_length=17, verbose_name='Номер двигателя')
    transmission_model = models.ForeignKey(Transmission_model, on_delete=models.PROTECT , db_index=True, verbose_name='Модель трансмиссии')
    transmission_number = models.TextField(max_length=50, verbose_name='Номер трансмиссии')
    drive_axle_model = models.ForeignKey(Drive_axle_model, on_delete=models.PROTECT , db_index=True, verbose_name='Модель ведущего моста')
    drive_axle_number = models.TextField(max_length=50, verbose_name='Номер ведущего моста')
    steerable_axle_model = models.ForeignKey(Steerable_axle_model, on_delete=models.PROTECT , db_index=True, verbose_name='Модель управляемого моста')
    steerable_axle_number = models.TextField(max_length=50, verbose_name='Номер управляемого моста')

    supply_contract = models.TextField(max_length=50, blank=True, verbose_name='Договор поставки №, дата.')
    date_of_shipment_from_the_factory = models.DateField(db_index=True, verbose_name='Дата отгрузки с завода')
    consignee = models.TextField(max_length=50, blank=True, verbose_name='Грузополучатель')
    delivery_address = models.TextField(max_length=300, blank=True, verbose_name='Адрес поставки (эксплуатации)')
    equipment = models.TextField(blank=True, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(Counterparty, on_delete=models.PROTECT , null=True, blank=True, verbose_name='Клиент')
    service_company = models.ForeignKey(Service_company, null=True, on_delete=models.PROTECT , blank=True, verbose_name='Сервисная организация')

    def __str__(self):
        return f'{self.factory_number}'

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'
        ordering = ['date_of_shipment_from_the_factory']

class Maintenance(models.Model):
    car = models.ForeignKey(Car, on_delete=models.PROTECT , verbose_name='Машина')
    service_company = models.ForeignKey(Service_company, on_delete=models.PROTECT , verbose_name='Сервисная организация')
    type_maintenance = models.ForeignKey(Type_maintenance, on_delete=models.PROTECT , verbose_name='Вид ТО')
    maintenance_date = models.DateField(verbose_name='Дата проведения ТО')
    operating_time = models.IntegerField(verbose_name='Наработка м/часов')
    order = models.TextField(max_length=50, verbose_name='Номер заказа-наряда')
    order_date = models.DateField(verbose_name='Дата заказа-наряда')
    company_executor = models.TextField(max_length=50, verbose_name='Компания исполнитель')

    def __str__(self):
        return f'{self.car, self.type_maintenance}'

    class Meta:
        verbose_name = 'ТО'
        verbose_name_plural = 'ТО'
        ordering = ['maintenance_date']

class Complaints(models.Model):
    date_of_refusal = models.DateField(verbose_name='Дата отказа')
    operating_time = models.IntegerField(verbose_name='Наработка м/час')
    Machine_components = models.ForeignKey(Machine_components, on_delete=models.PROTECT, verbose_name='Узел отказа')
    failure_node = models.TextField(verbose_name='Описание отказа ')
    recovery_method = models.ForeignKey(Recovery_method, on_delete=models.PROTECT , verbose_name='Способ восстановления')
    parts_used = models.TextField(blank=True, verbose_name='Используемые запасные части')
    date_of_restoration = models.DateField(verbose_name='Дата восстановления')
    equipment_downtime = models.TextField(verbose_name='Время простоя техники')
    car = models.ForeignKey(Car, on_delete=models.PROTECT, verbose_name='Машина')
    service_company = models.ForeignKey(Service_company, on_delete=models.PROTECT , verbose_name='Сервисная организация')
    def __str__(self):
        return f'{self.car, self.failure_node}'

    class Meta:
        verbose_name = 'Рекламации'
        verbose_name_plural = 'Рекламации'
        ordering = ['date_of_refusal']