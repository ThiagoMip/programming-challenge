from django.db import models

class Grupo(models.Model):
    identificador = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.BooleanField(default=True)
    data_criacao = models.DateField(auto_now_add=True)

class Usuario(models.Model):
    identificador = models.AutoField(primary_key=True)
    nome_completo = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(max_length=100)
    logradouro = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)