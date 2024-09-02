from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.

class Usuario (models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.EmailField(unique = True)
    password = models.CharField(max_length = 128)

    def save(self,*args,**kwargs):
        #Ciframos la contraseña antes de guardarla
        self.password = make_password(self.password)
        super().save(**args,**kwargs)