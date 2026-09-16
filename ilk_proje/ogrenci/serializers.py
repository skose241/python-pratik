from rest_framework import serializers
from .models import Ogrenci

class OgrenciSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ogrenci
        fields="__all__"    