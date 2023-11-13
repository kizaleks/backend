from django.contrib.auth.models import User
from django.db import models


class Counterparty(models.Model):
    '''Класс Контрагенты'''
    name=models.CharField(max_length=128)
    adress=models.CharField(max_length=128)
    telephone=models.CharField(max_length=12)

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    '''К модели User добавлено поле код активации '''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Сlient = 'Клиент'
    Service_organization = 'Сервисная организация'
    Manager = 'Менеджер'
    CATEGORY_CHOICES = (
        (Сlient, 'Клиент'),
        (Service_organization, 'Сервисная организация'),
        (Manager, 'Менеджер'),
    )
    сategory = models.CharField(max_length=21, choices=CATEGORY_CHOICES, default=Сlient)
    company=models.ForeignKey(Counterparty, on_delete=models.CASCADE)

