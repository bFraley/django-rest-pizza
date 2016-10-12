from rest_framework import serializers
from .models import Pizza, Topping

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ('name', 'price',)

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('name', 'price',)
        