from django.contrib import admin
from .models import Login,Registro,Producto,Suscrito,Envio,Pago,Historial

# Register your models here.

class LoginUsuario(admin.ModelAdmin):
    list_display = ["nombre", "clave"]
    search_fields = ["nombre"]


admin.site.register(Login, LoginUsuario)
admin.site.register(Registro)
admin.site.register(Producto)
admin.site.register(Suscrito)
admin.site.register(Envio)
admin.site.register(Pago)
admin.site.register(Historial)

