from django.shortcuts import render
from pages.descriptions import home_description
from portfolio.models import Projeto


def home(request):
    projects = Projeto.objects.all().order_by('-id',)[:3]

    context = {
        'page_settings': {
            'title': 'Home',
            'description': home_description,
            'disable_base_style': False,
            'disable_base_icons': False,
            'disable_base_mask': False,
            
        },
        'projects': projects,
    }

    if request.method == 'POST':
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        assunto = request.POST.get('assunto')
        mensagem = request.POST.get('mensagem')

        if len(nome) < 2 or len(sobrenome) < 2 or\
            not email or not telefone or not assunto or not mensagem:
            messages.error(
                request,
                'Erro de formulario, por favor insira todos os dados solitados corretamente'
            )

        if not User.objects.filter(email=email):
            user  = User(
                first_name=nome,
                last_name=sobrenome,
                username=f"{nome}_{sobrenome}_{random_letters()}",
                email=email,
                telefone=telefone,
                password=random_letters(8)
            )

            print(user.username)
            print(user.password)

            user.save()

            trabalho = Trabalho(
                user=user,
                assunto=Assunto.objects.get(slug=assunto),
                mensagem=mensagem,
            )
            trabalho.save()
            messages.success(request, 'Pedido recebido com sucesso!')

        else:
            messages.error(request, 'Ops! email em usor, tente novamente com outro email ou entre na sua conta para realizar novos pedidos ou atualizações.')
            context.update({
                "conteudo_form": {
                    'nome': nome,
                    'sobrenome': sobrenome,
                    'telefone': telefone,
                    'assunto': assunto,
                    'mensagem':mensagem,
                }
            })

    return render(request, 'pages/home.html', context)