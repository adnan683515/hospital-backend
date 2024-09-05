from django.urls import path, include
from rest_framework.routers import DefaultRouter
from doctor import views


router  = DefaultRouter()
router.register(r'designation',views.DesignationviewSet,basename='designation')
router.register(r'speacialization',views.SpeacializationtionviewSet,basename='speacilization')
router.register(r'list',views.DoctorviewSet,basename="doctor_List") 
router.register(r'availableTime',views.AvailableTimeviewSet)

urlpatterns = [
    path('', include(router.urls)),
]
