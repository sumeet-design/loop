from rest_framework import serializers
from .models import *

class StoreStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = store_status
        fields = '__all__'

class BusinessHoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = bussiness_hour
        fields = '__all__'

class StoreTimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = store_data
        fields = '__all__'
