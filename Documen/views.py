from django.shortcuts import render,redirect
from .forms import RegistroForm
from .models import Registro,Suscrito,Producto,Login 
from Documen.Carrito import Cart


# Create your views here.

def Login(request):  #Aqui funciona para todos en base de datos
    context = {}
    if request.method != "POST":
        return render(request, 'pages/Login.html')
    else:
        nombre= request.POST["nombre"]
        clave = request.POST["clave"]
        user = Registro.objects.get(nombre=nombre , clave=clave)
        if user is not None:
            request.session["nombreUsuario"] = nombre
            nombre = Registro.objects.get(nombre=nombre)
            context={"nombre":nombre}
            return render(request, 'pages/Home.html',context)
        else:
            context = {"mensaje": "Usuario y/o Contraseña incorrecta"}
            return render(request, "pages/Login.html",context) 

    

def Home(request):
    return render(request,'pages/Home.html')

def Envio(request):
    return render(request,'pages/Envio.html')

def Suscripcion(request):  #Aqui funciono pero solo con el usuario Luis
    if request.method != 'POST':
        return render(request, 'pages/Suscripcion.html') #Revisar
    else:
        monto=request.POST["Donativo"]
        metodo=request.POST["optMetodoP"]
        mensaje=request.POST["mensaje"]
        nombre1 = "Luis"
        clave1 = "12345678"

        user = Registro.objects.get(nombre=nombre1 , clave=clave1)
        if user is not None:

            Objsuscrito =  Registro.objects.get(nombre=nombre1)
            Nsuscrito = Suscrito.objects.create(

                nombre = Objsuscrito,
                monto=monto,
                metodo_pago=metodo,
                mensaje=mensaje,
            )
            Nsuscrito.save()
            context = {"mensaje" : "Exito"}
            return render(request, 'pages/Home.html',context)
        

def Desuscripcion(request,pk):  #No funciona la desuscripcion
    try:
        lista= Suscrito.objects.all()
        context= {"suscritos":lista}
        suscrito = Suscrito.objects.get(nombre=pk)
        suscrito.delete()
        return render(request,'pages/Suscripcion.html',context)
    except:
        return render(request,'pages/Suscripcion.html',context)



    
#Necesito agregar un desuscribir



def Identidad(request):
    return render(request, 'pages/Identidad.html')

def Contacto(request):
    return render(request, 'pages/Contacto.html')

def Productos(request):
    return render(request, 'pages/Productos.html')

def Fragmentos(request): #Este era el modelo antiguo/ Ahora se llama prueba donde use for y ahorre codigo
    fragmento = Producto.objects.all()
    context = {"producto":fragmento}
    return render(request, 'pages/Fragmentos.html',context)



#Necesito crear una pagina que donde se pueda cancelar el producto, se reflejen los descuentos y se borre del stock


def Perfil(request):
    return render(request, 'pages/Perfil.html')  #Necesito que se liste el historial de compras y estado pedido


def Registrar(request):
    if request.method != "POST":
        return render(request,'pages/Registrar.html')
    else:
        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        edad = request.POST["edad"]
        email = request.POST["email"]
        telefono = request.POST["telefono"]
        genero = request.POST["genero"]
        clave = request.POST["clave"]
        clave1 = request.POST["clave1"]
        nickname = request.POST["nickname"]
        equipo = request.POST["equipo"]

        NRegistro = Registro.objects.create(
            nombre=nombre,
            apellido=apellido,
            edad=edad,
            email=email,
            telefono=telefono,
            genero=genero,
            clave=clave,
            clave1=clave1,
            nickname=nickname,
            equipo=equipo,
        )
        NRegistro.save()
        context = {"mensaje": "FINALMENTE"}
        return render(request,'pages/Registrar.html',context)
    
def Pago(request):
    return render(request, 'pages/Pago.html')

def Carrito(request):
    return render(request, 'pages/Carrito.html')

#TAREAS
#Restringir segun el acceso segun el tipo de usuario 
#Enlazar el Login

def agregar_producto(request, ID):
    carrito = Cart(request)
    producto = Producto.objects.get(id_producto = ID)   #Estos eran crud que aprendi de videos pero no pude aplicarlos
    carrito.add(producto)                               #Al carrito en una ventana modal 
    return redirect("Fragmentos")

def eliminar_producto(request,ID):
    carrito = Cart(request)
    producto = Producto.objects.get(id_producto = ID)
    carrito.remove(producto)
    return redirect("Fragmentos")

def restar_producto(request, ID):
    carrito = Cart(request)
    producto = Producto.objects.get(id_producto = ID)
    carrito.decrement(producto)
    return redirect("Fragmentos")

def limpiar_carrito(request):
    carrito = Cart(request)
    carrito.clear()
    return redirect("Fragmentos")





def Prueba(request):                          #Este tiene como proposito descontar el stock al dar boton comprar
    if request.method == "POST":
        nombre = request.POST["nombreP"]
        stock = request.POST["stock"]
        Analisis = Producto.objects.get(nombre = nombre)  #Aqui intento que identifique el nombre del producto
        if Analisis is not None:
            compra = Producto()
            compra.stock= stock - 1
            compra.save()
            context={"compra1":compra}
            return render(request,'pages/Envio.html',context)
    else:
        Lista=Producto.objects.all()
        context ={"productos":Lista}
        return render(request,'pages/Prueba.html',context)







#Pruebas de crud

