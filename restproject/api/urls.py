from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from pizza.viewsets import PizzaViewSet
from pizza.viewsets import ToppingViewSet

router = DefaultRouter()

router.register(r'pizzas', PizzaViewSet)
router.register(r'toppings', ToppingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
