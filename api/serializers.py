from rest_framework import serializers
from .models import *


class Question1Serializer(serializers.ModelSerializer):
	class Meta:
		model = Question1
		fields = '__all__'


class Question2Serializer(serializers.ModelSerializer):
	class Meta:
		model = Question2
		fields = '__all__'

