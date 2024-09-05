from django.contrib import admin
from .models import Spealization,Designation,AvailableTime,Doctor,Review
# Register your models here.



class spealization_mdl(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',),}
    list_display = ['name','slug']
    
admin.site.register(Spealization,spealization_mdl)

class designation_mdl(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display=['name','slug']  
    
admin.site.register(Designation,designation_mdl)

admin.site.register(AvailableTime)
admin.site.register(Doctor)

admin.site.register(Review)