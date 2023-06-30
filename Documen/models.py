from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class Login(models.Model):
    nombre = models.CharField(max_length=12,blank=False, null=False)
    clave = models.CharField(max_length= 10, blank= False, null= False)
    
    def __str__(self):
        return self.nombre


Registro_genero = [(0,'Seleccione'),(1,'Masculino'),(2,'Femenino'),(3,'Otro')]
Registro_equipo = [(0,'Seleccione'),(1,'Administrativo'),(2,'Usuario'),(3,'Desarrollador')]
Registro_metodo = [(0,'Seleccione'),(1,'Visa'),(2,'Mastercard'),(3,'Pay pay'),(4,'Mach'),(4,'Tenpo'),(5,'Otro')]


class Registro(models.Model):
    nombre = models.CharField(max_length=12,blank=False, null=False, primary_key= True, db_column='idNombre', verbose_name='ID_Nombre')
    apellido = models.CharField(max_length=12,blank=False, null=False)
    edad = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=False, null = False, default=0)
    email = models.EmailField(max_length=30,blank=False, null=False, unique=True)
    telefono = models.CharField(max_length=9,blank=False, null=False)
    genero = models.CharField(max_length=12, blank = False, null = False, choices= Registro_genero, default=0)
    clave = models.CharField(max_length=12,blank=False, null=False,)
    clave1 = models.CharField(max_length=12,blank=False, null=False)
    nickname = models.CharField(max_length=12,blank=True, null=True)
    equipo = models.CharField(max_length=12, blank=False, null=False,choices= Registro_equipo,default=0)

    def __str__(self):
        return self.nombre
    


#Si aparece un error de migraciones faltantes es debido a que intente borrar id_producto y asignar como primary key
#A la variable nombre y no pude regresarla a la normalidad, ademas de que me impide seguir migrando datos

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True, db_column='idProducto', verbose_name='ID_Producto')
    nombre= models.CharField(max_length=20, blank= False, null= False)
    descripcion = models.TextField(max_length=100, blank= False, null= False)
    color= models.CharField(max_length=20, blank=False, null= False)
    material= models.CharField(max_length=20,blank= False, null= False)
    longitud= models.CharField(max_length=15, blank=False, null= False)
    precio = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=False, null = False, default=0)
    stock = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=False, null = False, default=0)

    def __str__(self):
        return str(self.nombre)
    


class Suscrito(models.Model):
    id_suscrito = models.AutoField(primary_key=True, db_column='idSuscrito', verbose_name='ID_Suscrito')    
    nombre = models.ForeignKey(Registro, on_delete=models.CASCADE, db_column='idNombre')
    monto = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=False, null = False, default=0)
    metodo_pago = models.CharField(max_length=12, blank = False, null = False, choices= Registro_metodo, default=0)
    mensaje = models.TextField(max_length=200,blank= True,null= True)

    def __str__(self):
        return str(self.nombre)
    

class Envio(models.Model):
    nombre = models.ForeignKey(Registro, on_delete=models.CASCADE, db_column='idNombre')
    apellido = models.CharField(max_length=20,blank= False, null= False)
    email = models.EmailField(max_length=30,blank=False, null=False, unique=True)
    telefono = models.CharField(max_length=9,blank=False, null=False)
    direccion = models.CharField(max_length=30,blank=False,null=False)
    region = models.CharField(max_length=20,blank= False, null= False)
    comuna = models.CharField(max_length=20,blank= False, null= False)
    info = models.TextField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)


class Pago(models.Model):
    precio = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=False, null = False, default=0)
    metodo_pago = models.CharField(max_length=12, blank = False, null = False, choices= Registro_metodo, default=0)

    def __str__(self):
        return str(self.precio)

class Historial(models.Model):
    nombre = models.ForeignKey(Registro, on_delete=models.CASCADE, db_column='idNombre')
    cantidad_total = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=False, null = False, default=0)
    valor_total = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)],blank=False, null = False, default=0)
    fecha_registro = models.DateField(blank=False, null=False)
    estado = models.CharField(max_length=12,blank=True, null=True)

    def __str__(self):
        return str(self.nombre)







    
    