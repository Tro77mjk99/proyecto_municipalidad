from django.db import models

class Ingreso_notas (models.Model):
    fecha_ingreso=models.IntegerField()
    Institucion_env=models.CharField(max_length=100)

class Institucion_env (models.Model):
    hospital!=models.BooleanField("hospital")
    policia!=models.BooleanField("policia")
    escuela==models.BooleanField("escuela")

class Expediente(models.Model):
    fecha_E=models.IntegerField()
    Numero_ex=models.IntegerField(max_length=1000) 




class Victima (models.Model):
    nombre =models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    documento = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    codigo_postal = models.IntegerField(max_length=1000)
    fecha_nacimiento = models.DateField(max_length=100)

class hijos(models.Model):
    nombre =models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    documento = models.IntegerField()
    fecha_nacimiento = models.DateField(max_length=100) 

class Agresor (models.Model):
    nombre =models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    documento = models.IntegerField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=100)
    codigo_postal = models.IntegerField(max_length=1000)
    fecha_nacimiento = models.DateField(max_length=100)

 
class Medidas(models.Model):
    id_caratula=models.CharField(max_length=1000)
    Numero_ex=models.CharField(max_length=100)
    documento_Victima=models.IntegerField()
    documento_Agresor=models.IntegerField()
    Resolucion=models.CharField(max_length=100)
    Alcance=models.CharField(max_length=100)
   