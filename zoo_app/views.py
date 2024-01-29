from django.shortcuts import render
from .models import Animal
from rest_framework.response import Response as res
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
# from rest_framework.authentication import TokenAuthentication

# Create your views here.
class animalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        token['hey you'] = 'fuck off'
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["GET"])
def animals(req, id = -1):
    if id  > -1:
        temp_animal = Animal.objects.get(id = id)
        return res(animalSerializer(temp_animal).data)
    else:
        animals = animalSerializer(Animal.objects.all(),many=True).data
        return res(animals)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def add_animal(req):
    animal = animalSerializer(data = req.data)
    if animal.is_valid():
        animal.save()
        return res("somthing")
    else:
        return res("not valid")

    
