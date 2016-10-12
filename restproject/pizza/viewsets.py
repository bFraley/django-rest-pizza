from rest_framework import viewsets
from django.db.models import Q

from .models import Pizza, Topping
from .serializers import PizzaSerializer, ToppingSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    serializer_class = PizzaSerializer
    queryset = Pizza.objects.all()

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            self.queryset = self.queryset.filter(title__icontains = query)
        return self.queryset


class ToppingViewSet(viewsets.ModelViewSet):
    serializer_class = ToppingSerializer
    queryset = Topping.objects.all()
