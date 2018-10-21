from django.contrib import admin
from .models import *

# Register your models here.



class information(admin.ModelAdmin):
    list_display = ('id','classnum','provider','service','name','area','system','outside','inside','cpu','memory','disk','date','status')
    search_fields = ('id','classnum','provider','service','name','area','system','outside','inside','cpu','memory','disk','date','status')
    list_filter = ('service','status')

admin.site.register(ServerManagent, information)

