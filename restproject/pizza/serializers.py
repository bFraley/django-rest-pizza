from rest_framework import serializers
from .models import Pizza, Topping

class PizzaSerializer(serializers.ModelSerializer):
    pizza_count = serializers.SerializerMethodField()

    class Meta:
        model = Pizza
        fields = ('name', 'price', 'pizza_count')

    def get_pizza_count(self, pizza):
        return pizza.pizza_set.count()

class ToppingSerializer(serializers.ModelSerializer):
    topping_count = serializers.SerializerMethodField()

    class Meta:
        model = Topping
        fields = ('name', 'price', 'topping_count')

    def get_topping_count(self, topping):
        return topping.topping_set.count()

