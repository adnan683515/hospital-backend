from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()
router.register('list', views.petaintViewSet)


urlpatterns = [
    path('patient/', include(router.urls)),
    path("signup/",views.RegisterViewSet.as_view(),name='register'),
    path('active/<uid64>/<token>/',views.activate,name='email_active'),
    path("login/",views.LoginViews.as_view(),name='login'),
    path("logout/",views.logoutView.as_view(),name='logout')
]