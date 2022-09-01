from django.db import models

class Curso(models.Model):
    titulo = models.CharField('Título', max_length=100)
    vagas =models.IntegerField('Vagas')
    turno = models.CharField('Turno', max_length=100)

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    idade =models.IntegerField('Idade')
    cpf = models.InterField('CPF', max_length=11)

class Professor(models.Model):
    nome = models.CharField('Nome', max_length=100)
    disciplina =models.IntegerField('Disciplina')
