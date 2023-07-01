from django.db import models

# class Usuario(models.Model):
#     nombre_usuario = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(unique=True)
#     contraseña = models.CharField(max_length=8)

#     class Meta:
#         db_table = "tblUsuario"

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    email = models.EmailField()
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_usuario

class Tabla1(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=100)
    campo3 = models.CharField(max_length=100)

    def __str__(self):
        return self.campo1

class Tabla2(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=100)
    campo3 = models.CharField(max_length=100)

    def __str__(self):
        return self.campo1

class Tabla3(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.CharField(max_length=100)
    campo3 = models.CharField(max_length=100)

    def __str__(self):
        return self.campo1
# class Tabla1(models.Model):
#     campo1 = models.CharField(max_length=100)
#     campo2 = models.IntegerField()
#     campo3 = models.DateTimeField(auto_now_add=True)
#     class Meta:
#         db_table ='tbTabla1'

# class Tabla2(models.Model):
#     campo1 = models.CharField(max_length=50)
#     campo2 = models.TextField()
#     campo3 = models.BooleanField(default=False)
#     class Meta:
#         db_table ='tbTabla2'

# class Tabla3(models.Model):
#     campo1 = models.CharField(max_length=200)
#     campo2 = models.DecimalField(max_digits=5, decimal_places=2)
#     campo3 = models.BooleanField(default=False)
#     class Meta:
#         db_table ='tbTabla3'