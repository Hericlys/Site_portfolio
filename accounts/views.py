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
from secrets import token_urlsafe

# auth
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
                if user.validated_email:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, f'Bem vindo! {user.first_name} { user.last_name }')
                    return redirect('portfolio:home')
                else:
                    messages.error(request, 'Ative sua conta para fazer login')
        except:
            messages.error(
                request,
                'Parece que não existe uma conta registrada para esse E-mail'
            )
    return render(request, 'accounts\login.html', context)


@login_required(redirect_field_name='accounts:login')
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


def validated_email(request, authentication_token):

    user = User.objects.get(authentication_token=authentication_token)
    if not user.validated_email:
        user.validated_email = True
        user.save()
        messages.success(request, f'E-mail validado com sucesso! Agora faça login')
        return redirect('accounts:login')
    else:
        return redirect('portfolio:home')


def password_recovery_request(request):
    context = {
        'page_title': 'Recuperação de senha',
    }

    if request.method == "POST":
        email = request.POST.get('email')

        context = {
            'conteudo_form': {
                'email': email,
            }
        }

        try:
            user = User.objects.get(email=email)

            user.authentication_token= str(token_urlsafe())
            user.save()

            html_content = render_to_string(r'accounts\email\password_recovery.html', {
                'code': f"http://127.0.0.1:8000/accounts/password_recovery/{user.authentication_token}"
            })
            text_content = strip_tags(html_content)
            email = EmailMultiAlternatives('Validação de E-mail', text_content, settings.DEFAULT_FROM_EMAIL, [user.email,])
            email.attach_alternative(html_content, 'text/html')
            email.send()
            messages.success(request, 'Solicitação enviada com sucesso! Verifique seu E-mail')
        except:
            messages.error(request, 'Não existe um conta vinculada a esse E-mail')


    return render(request, 'accounts\password_recovery_request.html', context)


def password_recovery(request, authentication_token):
    try:
        user = User.objects.get(authentication_token=authentication_token)

        context = {
            'page_title': 'Redefinição de senha',
            'authentication_token': authentication_token,
        }

        if request.method == "POST":
            senha = request.POST.get('senha')
            senha2 = request.POST.get('senha2')
            if senha != senha2:
                messages.error(request, 'A confirmação de senha falhou, tente novamente.')
            else:
                user.set_password(senha)
                user.authentication_token= str(token_urlsafe())
                user.save()
                messages.success(request, 'senha alterada com sucesso! Agora faça login.')
                return redirect('accounts:login')

        return render(request, "accounts\password_recovery.html", context)

    except:
        context = {
            'page_title': 'Page 404'
        }
        return render(request, 'accounts/page_404.html', context)



# CRUD
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
            telefone=telefone,
        )
        new_user.set_password(senha)

        new_user.save()

        messages.success(request, 'Perfil criado com sucesso! agora faça login')
        html_content = render_to_string(r'accounts\email\validate_email.html', {
            'user': new_user,
            'code': f"http://127.0.0.1:8000/accounts/validated_email/{new_user.authentication_token}"
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
