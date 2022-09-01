from django.shortcuts import render, redirect
from .models import Curso, Aluno, Professor
from .forms import CursoForm, ProfessorForm, AlunoForm

def home(request):
    return render(request, 'index.html')
#cursos
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


#alunos
def listar_alunos(request):
    aluno = Aluno.objects.all()
    contexto = {
        'todos_alunos': aluno
    }
    return render(request, 'usuario.html', contexto)

def cadastrar_alunos(request):
    form = AlunoForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_alunos')

    contexto = {
        'form_aluno': form
    }
    return render(request, 'usuario_cadastrar.html', contexto)  

def editar_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    form = AlunoForm(request.POST or None, instance=aluno)

    if form.is_valid():
        form.save()
        return redirect('listar_alunos')

    contexto = {
        'form_aluno': form
    }

    return render(request, 'usuario_cadastrar.html', contexto)  

def remover_aluno(request, id):
    aluno = Aluno.objects.get(pk=id)
    aluno.delete()
    return redirect('listar_alunos')


#professores
def listar_professores(request):
    professores = Professor.objects.all()
    contexto = {
        'todos_professores': professores
    }
    return render(request, 'professor.html', contexto)

def cadastrar_professor(request):
    form = ProfessorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_professor')

    contexto = {
        'form_professor': form
    }
    return render(request, 'professor_cadastrar.html', contexto)  

def editar_professor(request, id):
    professor = Professor.objects.get(pk=id)
    form = ProfessorForm(request.POST or None, instance=professor)

    if form.is_valid():
        form.save()
        return redirect('listar_professor')

    contexto = {
        'form_professor': form
    }

    return render(request, 'professor_cadastrar.html', contexto)  

def remover_professor(request, id):
    professor = Professor.objects.get(pk=id)
    professor.delete()
    return redirect('listar_professor')
