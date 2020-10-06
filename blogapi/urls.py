from django.urls import path, include
from rest_framework import routers
from .views import BlogDetailsData

route = routers.DefaultRouter()
route.register('', BlogDetailsData)

urlpatterns = [
    path('', include(route.urls))
]
