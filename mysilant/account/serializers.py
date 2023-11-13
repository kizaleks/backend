from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Counterparty


class UserSerializer(serializers.ModelSerializer):
    '''Справочник Пользователии'''
    class Meta:
        model = User
        fields = ['id','username']

class CounterpartySerializer(serializers.ModelSerializer):
    '''Справочник Контрагенты'''
    class Meta:
        model = Counterparty
        fields = ['id','name',"telephone"]

class ProfileSerializer(serializers.Serializer):
    '''Справочник Профили пользователя'''
    id= serializers.CharField()
    id_user=serializers.CharField(source='user.id', max_length=200)
    user=serializers.CharField(source='user.username', max_length=200)
    сategory=serializers.CharField()
    id_company = serializers.CharField(source='company.id.id', max_length=200)
    company=serializers.CharField(source='company.name.name', max_length=200)

    class Meta:
        # model = Profile
        fields = ['id','id_user','user','сategory','id_company','company']
# class ProfileSerializer(serializers.ModelSerializer):
#     '''Справочник Модели техники'''
#     class Meta:
#         model = Profile
#         fields = ['user','сategory','company']
#
#     def to_representation(self, instance):
#         representation = super(ProfileSerializer, self).to_representation(instance)
#         representation['company'] = CounterpartySerializer(instance.company).data
#         representation['user'] = UserSerializer(instance.user).data
#         return representation