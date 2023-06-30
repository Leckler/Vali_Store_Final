from django.urls import path
from .views import Login,Home,Registrar,Envio,Suscripcion,Identidad,Contacto,Productos,Fragmentos,Perfil,Pago,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito,Carrito,Prueba,Desuscripcion #,Comprar
urlpatterns = [
    path('Login/',Login,name="Login"),
    path('Home/',Home,name="Home"),
    path('Registrar/',Registrar,name="Registrar"),
    path('Envio/',Envio,name="Envio"),
    path('Suscripcion/' ,Suscripcion,name="Suscripcion"),
    path('Identidad/',Identidad,name="Identidad"),
    path('Contacto/',Contacto, name="Contacto"),
    path('Productos/',Productos, name="Productos"),
    path('Fragmentos/',Fragmentos,name="Fragmentos"),
    path('Perfil/',Perfil, name="Perfil"),
    path('Pago/',Pago, name="Pago"),


    path('add/<int:ID>/', agregar_producto, name= "Add"),                 #De aqui hacia abajo son intentos de CRUD
    path('remove/<int:ID>/', eliminar_producto, name= "Del"),             #Tal vez mi problema es que no supe aplicarlos
    path('decrement/<int:ID>/', restar_producto, name= "Sub"),  
    path('clear/', limpiar_carrito, name= "CLS"),
    path('Carrito/',Carrito,name="Carrito"),



    path('Prueba/',Prueba,name="Prueba"), #Pagina de ventas a los usuarios


    #path('Comprar/',Comprar,name="Comprar")                                #Son url que no supe aplicar
    path('Desuscripcion/<str:pk>',Desuscripcion,name="Desuscripcion")

    

]

