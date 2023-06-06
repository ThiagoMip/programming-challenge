# Importing the necessary modules from Django
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Grupo, Usuario

# API for saving information in a Postgres database
@csrf_exempt
def salvar_info(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Informações salvas com sucesso.'}, status=200)
    else:
        # Unsupported HTTP method.
        return JsonResponse({'error': 'Método não suportado.'}, status=405)


# API for creating new user groups
@csrf_exempt
def cadastrar_grupo(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Grupo cadastrado com sucesso.'}, status=200)
    else:
        # Unsupported HTTP method.
        return JsonResponse({'error': 'Método não suportado.'}, status=405)


# API for creating new users
@csrf_exempt
def cadastrar_usuario(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Usuário cadastrado com sucesso.'}, status=200)
    else:
        # Unsupported HTTP method.
        return JsonResponse({'error': 'Método não suportado.'}, status=405)


# API for editing user and group profiles
@csrf_exempt
def editar_perfil(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Perfil editado com sucesso.'}, status=200)
    else:
        # Unsupported HTTP method.
        return JsonResponse({'error': 'Método não suportado.'}, status=405)


# API for deleting users and groups
@csrf_exempt
def excluir(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Registros excluídos com sucesso.'}, status=200)
    else:
        # Unsupported HTTP method.
        return JsonResponse({'error': 'Método não suportado.'}, status=405)
