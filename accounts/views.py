from django.shortcuts import render, redirect
from accounts.models import User
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from utils.rands import random_letters


def login(request):
    context = {
        'page_title': 'Entrar'
    }
    if request.method == "POST":
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        context.update({
            'conteudo_form': {
                'email': email
            }
        })
    
        try:
            validate_email(email)
        except:
            messages.error(request, 'E-mail invalido')

        try:
            usuario = User.objects.get(email=email)
            user = auth.authenticate(request, username=usuario.username, password=senha)
            if not user:
                messages.error(request, 'E-mail ou senha invalido')
            else:
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Bem vindo! {user.first_name} { user.last_name }')
                return redirect('portfolio:home')
        except:
            messages.error(
                request,
                'Parece que não existe uma conta registrada para esse E-mail'
            )
    return render(request, 'accounts\login.html', context)


@login_required(redirect_field_name='accounts:login')
def logoff(request):
    auth.logout(request)
    return redirect('accounts:login')


def create(request):
    context = {
        'page_title': 'Cadastro'
    }

    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('nome')
        last_name = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        context.update({
            'conteudo_form': {
                    'username': username,
                    'first_name': first_name,
                    'last_name': last_name,
                    'telefone': telefone,
                    'email': email,
                }
        })

        try:
            validate_email(email)
            try:
                email_exist = User.objects.get(email=email)
                messages.error(request, 'E-mail em uso, faça login em sua conta')
                return render(request, 'accounts\cadastro.html', context)
            except:
                pass
        except:
            messages.error(request, 'Esse E-mail não é valido, tente outro')
            return render(request, 'accounts\cadastro.html', context)

        try:
            User.objects.get(telefone=telefone)
            messages.error(request, 'Numero de telefone em uso, faça login em sua conta')
            context.update(
                {'telefone': ''}
            )
            return render(request, 'accounts\cadastro.html', context)
        except:
            pass

        try:
            User.objects.get(username=username)
            messages.error(request, 'Nome de usuario em uso, faça login em sua conta')
            context.update ({
                'username': ''
            })
            return render(request, 'accounts\cadastro.html', context)
        except:
            pass

        if senha != senha2:
            messages.error(request, 'As senhas não conferem, tente novamente.')
            return render(request, 'accounts\cadastro.html', context)

        new_user = User(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=senha,
            telefone=telefone,
        )

        new_user.save()

        messages.success(request, 'Perfil criado com sucesso! agora faça login')
        html_content = render_to_string(r'accounts\email\validate_email.html', {
            'user': new_user,
            'code': random_letters(6)
        })
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives('Validação de E-mail', text_content, settings.DEFAULT_FROM_EMAIL, [new_user.email,])
        email.attach_alternative(html_content, 'text/html')
        email.send()

        return redirect('accounts:login')

    return render(request, 'accounts\cadastro.html', context)


@login_required(redirect_field_name='accounts:login')
def update(request):
    return render(request, r'accounts\update.html')
