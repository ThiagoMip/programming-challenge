from django.urls import path

from .views import cadastrar_grupo, listar_grupos, editar_grupo, excluir_grupo

urlpatterns = [
    path('grupos/cadastrar/', cadastrar_grupo, name='cadastrar_grupo'),
    path('grupos/listar/', listar_grupos, name='listar_grupos'),
    path('grupos/editar/<int:grupo_id>/', editar_grupo, name='editar_grupo'),
    path('grupos/excluir/<int:grupo_id>/', excluir_grupo, name='excluir_grupo'),
]
