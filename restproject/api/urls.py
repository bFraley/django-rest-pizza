from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

#router.register(r'pizzas', PizzaViewSet)
#router.register(r'toppings', ToppingViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
