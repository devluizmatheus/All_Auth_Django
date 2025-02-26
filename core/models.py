from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class Interesses(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome

class Usuarios(AbstractUser):
    nome = models.CharField(max_length=25)
    sobrenome = models.CharField(max_length=25)
    data_nascimento = models.DateField('Data Nascimento')
    telefone = models.CharField(max_length=150)
    CPF = models.CharField(max_length=150)
    interesses = models.ManyToManyField(Interesses, related_name="usuarios")

    groups = models.ManyToManyField(
        Group,
        related_name="usuarios_groups",  # Nome único para evitar conflitos
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="usuarios_permissions",  # Nome único para evitar conflitos
        blank=True
    )   

    def __str__(self):
        return self.username