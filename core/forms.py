from django.forms import ModelForm
from .models import Curso, Aluno, Professor

class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'vagas', 'turno']

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'idade', 'cpf']

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'disciplina', 'cpf']