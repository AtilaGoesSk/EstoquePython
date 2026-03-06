from django.contrib import admin

#Register your models here.
from django.contrib import admin
from .models import Produto, Fornecedor

admin.site.register(Produto)
admin.site.register(Fornecedor)#testepra add pelo admin