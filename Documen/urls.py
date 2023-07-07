from django.urls import path
from .views import Login,Home,Registrar,Envio,Suscripcion,Identidad,Contacto,Productos,Fragmentos,Perfil,Pago,Prueba,Desuscripcion,userDel,agregar_producto,eliminar_producto,restar_producto,limpiar_carrito,Carrito #,Comprar
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
    path("userDel/",userDel,name="userDel"),


    path('add/<int:ID>/', agregar_producto, name= "Add"),                 
    path('remove/<int:ID>/', eliminar_producto, name= "Del"),             
    path('decrement/<int:ID>/', restar_producto, name= "Sub"),  
    path('clear/', limpiar_carrito, name= "CLS"),
    path('Carrito/',Carrito,name="Carrito"),



    path('Prueba/',Prueba,name="Prueba"),                                     #Pagina de ventas a los usuarios


    #path('Comprar/',Comprar,name="Comprar"),                              
    path('Desuscripcion/<str:pk>',Desuscripcion,name="Desuscripcion")

    

]

