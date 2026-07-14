from django.db import models


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100,  null=False)
    email = models.EmailField(null=False, unique=True)
    senha = models.CharField(max_length=100, null=False)
    cpf = models.CharField(max_length=11, null=False, unique=True)

    def __str__(self):
        return self.nome