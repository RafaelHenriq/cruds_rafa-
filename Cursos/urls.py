"""Cursos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import listar_cursos, cadastrar_curso, editar_curso, remover_curso, home
from core.views import listar_alunos, cadastrar_alunos, editar_aluno, remover_aluno
from core.views import listar_professores, cadastrar_professor, editar_professor, remover_professor
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', home,name='home'),
    path('cursos/', listar_cursos, name='listar_cursos'),
    path('curso_cadastrar/', cadastrar_curso, name='cadastrar_curso'),
    path('curso_editar/<int:id>/', editar_curso, name='editar_curso'),
    path('curso_remover/<int:id>/', remover_curso, name='remover_curso'),

    path('usuario/', listar_alunos, name='listar_alunos'),
    path('usuario_cadastrar/', cadastrar_alunos, name='cadastrar_aluno'),
    path('usuario_editar/<int:id>/', editar_aluno, name='editar_aluno'),
    path('usuario_remover/<int:id>/', remover_aluno, name='remover_aluno'),

    path('professor/', listar_professores, name='listar_professor'),
    path('professor_cadastrar/', cadastrar_professor, name='cadastrar_professor'),
    path('professor_editar/<int:id>/', editar_professor, name='editar_professor'),
    path('professor_remover/<int:id>/', remover_professor, name='remover_professor'),

    path('admin/', admin.site.urls),


]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

