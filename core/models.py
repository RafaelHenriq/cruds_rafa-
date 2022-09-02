from django.db import models

class Curso(models.Model):
    titulo = models.CharField('Título', max_length=100)
    vagas =models.IntegerField('Vagas')
    turno = models.CharField('Turno', max_length=100)
    foto = models.ImageField('Foto', upload_to='cursos', null=True)
class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    idade = models.IntegerField('Idade')
    cpf = models.IntegerField('CPF', max_length=11)
    foto = models.ImageField('Foto', upload_to='cursos', null=True)
class Professor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    disciplina = models.CharField('Disciplina', max_length=50)
    cpf = models.IntegerField('CPF', max_length=11)
    foto = models.ImageField('Foto', upload_to='cursos', null=True)
class Cursos(models.Model):



  