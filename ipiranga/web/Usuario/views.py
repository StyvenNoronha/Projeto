from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import format_html

from .models import Usuario
from django.shortcuts import redirect
from hashlib import sha256


# Create your views here.

def login(request):
    return render(request, 'Usuario/Login.html')


def cadastro(request):
    status = request.GET.get('status')

    return render(request, 'Usuario/cadastro.html')


def valida_cadastro(request):
    Nome = request.POST.get('Nome')
    Email = request.POST.get('Email')
    Senha = request.POST.get('Senha')

    usuario = Usuario.objects.filter(email=Email)

    if len(Nome.strip()) == 0 or len(Email.strip()) == 0:
        msg = format_html('<div class="alert alert-danger alert-dismissible"> '
                          'NOME OU EMAIL NÃO PODEM ESTAR VAZIOS'
                          '<br>'
                          ' ERRO '
                          '</div>')
        return render(request, 'Usuario/cadastro.html', {'mensagem': msg})
    if len(Senha) < 0:
        msg = format_html('<div class="alert alert-danger alert-dismissible"> '
                          'SENHA MUITO PEQUENA'
                          '<br>'
                          ' ERRO '
                          '</div>')
        return render(request, 'Usuario/cadastro.html', {'mensagem': msg})

    if len(usuario) > 0:
        msg = format_html('<div class="alert alert-danger alert-dismissible"> '
                          'USUÁRIO JÁ EXISTE NO SISTEMA'
                          '<br>'
                          ' ERRO '
                          '</div>')
        return render(request, 'Usuario/cadastro.html', {'mensagem': msg})
    try:
        Senha = sha256(Senha.encode()).hexdigest()
        usuario = Usuario(nome=Nome,
                          email=Email,
                          senha=Senha)
        usuario.save()
        msg = format_html('<div class="alert alert-success alert-dismissible"> '
                          'USUÁRIO CADASTRADO '
                          '<br>'
                          ' BEM  VINDO '
                          '</div>')
        return render(request, 'Usuario/cadastro.html', {'mensagem': msg})
    except:
        msg = format_html('<div class="alert alert-danger alert-dismissible"> '
                          'ERRO NO BANCO DE DADOS '
                          '<br>'
                          'SORRY '
                          '</div>')
        return render(request, 'Usuario/cadastro.html', {'mensagem': msg})


def valida_login(request):
    Email = request.POST.get('Email')
    Senha = request.POST.get('Senha')
    Senha = sha256(Senha.encode()).hexdigest()

    usuario = Usuario.objects.filter(email=Email).filter(senha=Senha)


    if len(usuario) > 0:
        msg = format_html('<div class="alert alert-danger alert-dismissible"> '
                          'ERRO SENHA OU EMAIL INCORRETO'
                          '<br>'
                          'SORRY '
                          '</div>')
        return render(request, 'Usuario/Login.html', {'mensagem': msg})

    elif len(usuario) > 0:
        request.session['usuario'] = usuario[0].id

    return render(request,'pagpri/index.html')