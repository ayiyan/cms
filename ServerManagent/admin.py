from django.contrib import admin
from .models import *

# Register your models here.



class SMinformation(admin.ModelAdmin):
    list_display = ('id','classnum','provider','service','name','area','system','outside','inside','cpu','memory','disk','date',
                    'colored_status')
    search_fields = ('id','classnum','provider','service','name','area','system','outside','inside','cpu','memory','disk','date','status')
    list_filter = ('service','status')

class AMinformation(admin.ModelAdmin):
    list_display = ('category','name','address','style','account','password')
    search_fields = ('category','name','address','style','account','password')


class DAinformation(admin.ModelAdmin):
    list_display = ('category','style','name','account','password','address1','address2','address3')
    search_fields = ('category','style','name','account','password','address1','address2','address3')

class INinformation(admin.ModelAdmin):
    list_display = ('ip','mac','cpu','mem','disk','system','user','password')
    search_fields = ('ip','mac','cpu','mem','disk','system','user','password')


class MMinformation(admin.ModelAdmin):
    list_display = ('name','account','password')
    search_fields = ('name','account','password')



admin.site.register(ServerManagent, SMinformation)
admin.site.register(AccountManagent, AMinformation)
admin.site.register(DBAccount, DAinformation)
admin.site.register(InsideName, INinformation)
admin.site.register(MailManagent, MMinformation)
