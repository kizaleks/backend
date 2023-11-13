from django.contrib import admin
from .models import Technique_model, Engine_model, Transmission_model, Drive_axle_model, Steerable_axle_model,\
    Type_maintenance,Description_failure, Recovery_method, Service_company, Machine_components , Car,\
    Complaints, Maintenance

class ViewsAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_filter = ('name','description')
    search_fields = ('name','description')

'''Справочники'''
admin.site.register(Technique_model,ViewsAdmin)
admin.site.register(Engine_model,ViewsAdmin)
admin.site.register(Transmission_model,ViewsAdmin)
admin.site.register(Drive_axle_model,ViewsAdmin)
admin.site.register(Steerable_axle_model,ViewsAdmin)
admin.site.register(Type_maintenance,ViewsAdmin)
admin.site.register(Description_failure,ViewsAdmin)
admin.site.register(Recovery_method,ViewsAdmin)
admin.site.register(Machine_components,ViewsAdmin)
admin.site.register(Service_company,ViewsAdmin)

admin.site.register(Car)
admin.site.register(Maintenance)
admin.site.register(Complaints)
