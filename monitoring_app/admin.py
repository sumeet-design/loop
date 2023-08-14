from django.contrib import admin

# Register your models here.
from monitoring_app.models import *
admin.site.register(store_data)
admin.site.register(store_status)
admin.site.register(bussiness_hour)
admin.site.register(Report)