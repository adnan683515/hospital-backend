from django.urls import path, include
from rest_framework.routers import DefaultRouter
from service import views

router = DefaultRouter()
router.register('',views.ServiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]