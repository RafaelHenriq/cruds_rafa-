from django.forms import ModelForm
from .models import Curso,Aluno, Professor

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'vagas']

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade']

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'disciplina']