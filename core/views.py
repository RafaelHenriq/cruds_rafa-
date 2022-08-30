from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm

def listar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        'todos_cursos': cursos
    }
    return render(request, 'cursos.html', contexto)

def cadastrar_curso(request):
    form = CursoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_cursos')

    contexto = {
        'form_curso': form
    }
    return render(request, 'curso_cadastrar.html', contexto)  

def editar_curso(request, id):
    curso = Curso.objects.get(pk=id)
    form = CursoForm(request.POST or None, instance=curso)

    if form.is_valid():
        form.save()
        return redirect('listar_cursos')

    contexto = {
        'form_curso': form
    }

    return render(request, 'curso_cadastrar.html', contexto)  

def remover_curso(request, id):
    curso = Curso.objects.get(pk=id)
    curso.delete()
    return redirect('listar_cursos')
