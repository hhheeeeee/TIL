from rest_framework.serializers import ModelSerializer, ReadOnlyField
from .models import DepositProducts, DepositOptions


class DepositProductsSerializer(ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'

# https://medium.com/@heeee/til-drf-serializer%EC%97%90%EC%84%9C-%EC%99%B8%EB%9E%98%ED%82%A4-%ED%85%8C%EC%9D%B4%EB%B8%94%EC%9D%98-%ED%95%84%EB%93%9C-%EA%B0%80%EC%A0%B8%EC%98%A4%EA%B8%B0-242c06b25dc2
class DepositOptionsSerializer(ModelSerializer):
    product = ReadOnlyField(source='DepositOptions.product')
    
    class Meta:
        model = DepositOptions
        fields = '__all__'
        # read_only_fields = ('product', )


class NestedSerialzer(ModelSerializer):
    product = DepositProductsSerializer(read_only=True)
    
    class Meta:
        model = DepositOptions
        fields = '__all__'