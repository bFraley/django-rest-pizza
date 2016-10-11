from django.conf.urls import include, url
from rest_framework.routers import DefaultRouters

urlpatterns = [
    url('r^', include(router.urls))
]
