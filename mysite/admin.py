from django.contrib import admin

# Register your models here.


from .models import Cliente, Endereco

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome','cpf')

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('cliente','endereco', 'numero', 'cidade')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Endereco)