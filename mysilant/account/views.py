from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Profile, Counterparty
from .serializers import ProfileSerializer, CounterpartySerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        queryset = Profile.objects.get(user=user.pk)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'user_name': user.username,
            'сategory': queryset.сategory,
            'company_id': queryset.company.id,
            'company_name': queryset.company.name

        })


class ProfileViewSet(viewsets.ModelViewSet):
    '''Справочник Профили пользователей'''
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CounterpartyViewSet(viewsets.ModelViewSet):
    '''Справочник Контрагенты'''
    queryset = Counterparty.objects.all()
    serializer_class = CounterpartySerializer