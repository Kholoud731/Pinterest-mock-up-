from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes,authentication_classes
from .serializers import PinSerializer, PinCreateSerializer, UserSerializer, PinSaveSerializer
from .models import Pin
from accounts.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


@api_view(['GET'])
def home(request):
    pins = Pin.objects.all()
    serializer = PinSerializer(pins, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_pin(request):
    if request.method == 'GET':
        user = request.user
        seralizer = UserSerializer(instance=user)
        return Response(data=seralizer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        data = {
            'title': request.data.get('title'),
            'description': request.data.get('description'),
            'image': request.data.get('image'),
            'creator': request.user.id,
            'website': request.data.get('website'),
        }
        new_pin = PinCreateSerializer(data=data)
        if new_pin.is_valid():
            new_pin.save()
            return Response(new_pin.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=new_pin.errors)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def save_pin(request):

    if request.method == 'POST':
        data = {
            'pin_id': request.data.get('pin'),
            'user_id': request.user.id,
        }
        saved_pin = PinSaveSerializer(data=data)
        if saved_pin.is_valid():
            saved_pin.save()
            return Response(saved_pin.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=saved_pin.errors)