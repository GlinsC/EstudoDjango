from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Usuario


@csrf_exempt
def usuario_list(request):
    usuarios = Usuario.objects.all()
    dados_json = [
        {
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'cpf': usuario.cpf,
        }
        for usuario in usuarios
    ]
    return JsonResponse(dados_json, safe=False)


def usuario_render(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario/index.html', {'usuarios': usuarios})


@csrf_exempt
def adicionar_usuario(request):
    print(request.body)
    if request.method == 'POST':
        data = json.loads(request.body)
        nome = data.get('nome')
        email = data.get('email')
        senha = data.get('senha')
        cpf = data.get('cpf')

        # Cria um novo objeto Usuario e salva no banco de dados
        usuario1 = Usuario(nome=nome, email=email, senha=senha, cpf=cpf)
        usuario1.save()

        return JsonResponse({'message': 'Usuário adicionado com sucesso!'})
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)

def adicionar_render(request):
    print(request.POST)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        cpf = request.POST.get('cpf')

        # Cria um novo objeto Usuario e salva no banco de dados
        usuario1 = Usuario(nome=nome, email=email, senha=senha, cpf=cpf)
        usuario1.save()

        return redirect('usuario_render')
    else:
        return redirect('usuario_render')


def buscar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        dados_json = {
            'id': usuario.id,
            'nome': usuario.nome,
            'email': usuario.email,
            'cpf': usuario.cpf,
        }
        return JsonResponse(dados_json)
    except Usuario.DoesNotExist:
        return JsonResponse({'error': 'Usuário não encontrado'},status=404)


@csrf_exempt
def editar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        if request.method == 'PUT':
            data = json.loads(request.body)
            usuario.nome = data.get('nome', usuario.nome)
            usuario.email = data.get('email', usuario.email)
            usuario.senha = data.get('senha', usuario.senha)
            usuario.cpf = data.get('cpf', usuario.cpf)
            usuario.save()
            return JsonResponse({'message': 'Usuário atualizado com sucesso!'})
    except Usuario.DoesNotExist:
        return JsonResponse({'error': 'Usuário não encontrado'}, status=404)

@csrf_exempt    
def deletar_usuario(request, usuario_id):
    try:
        usuario = Usuario.objects.get(id=usuario_id)
        usuario.delete()
        return JsonResponse({'message': 'Usuário deletado com sucesso!'})
    except Usuario.DoesNotExist:
        return JsonResponse({'error': 'Usuário não encontrado'}, status=404)

def buscar_usuario_por_email(request):
    email = request.GET.get('email')
    if email:
        try:
            usuario = Usuario.objects.get(email=email)
            dados_json = {
                'id': usuario.id,
                'nome': usuario.nome,
                'email': usuario.email,
                'cpf': usuario.cpf,
            }
            return JsonResponse(dados_json)
        except Usuario.DoesNotExist:
            return JsonResponse({'error': 'Usuário não encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Parâmetro de email não fornecido'}, status=400)