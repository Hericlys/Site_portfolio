from django.shortcuts import render
from portfolio.models import CategoriaProjeto, Projeto
from django.db.models import Q
from django.core.paginator import Paginator


def home(request):
    projetos = Projeto.objects.filter(visivel=True).order_by('-id')[:6]
    categorias = CategoriaProjeto.objects.all()
    context = {
        'projetos': projetos,
        'categorias': categorias,
        'page_title': 'Home',
        'all': True,
    }

    if 'opcao' in request.GET and request.GET.get('opcao') != '':
        opcao_selecionada = request.GET.get('opcao')
        categoria = CategoriaProjeto.objects.get(slug=opcao_selecionada)
        projetos = Projeto.objects.filter(categoria=categoria.id, visivel=True).order_by('-id')[:6]
        context.update({
            'opcao_selecionada': opcao_selecionada,
            'projetos': projetos,
        })

    return render(request, 'portfolio/my_page.html', context)


def projetos(request):
    projetos = Projeto.objects.filter(visivel=True).order_by('-id')
    categorias = CategoriaProjeto.objects.all()
    context = {
        'projetos': projetos,
        'categorias': categorias,
        'page_title': 'Home',
        'search_value': '',
    }

    if 'opcao' in request.GET:
        opcao_selecionada = request.GET.get('opcao')
        search_value = request.GET.get('search')

        try:
            categoria = CategoriaProjeto.objects.get(slug=opcao_selecionada)
            projetos = Projeto.objects.filter(categoria=categoria.id).filter(
                Q(descricao__icontains=search_value) |
                Q(nome__icontains=search_value) |
                Q(conteudo__icontains=search_value) |
                Q(status__icontains=search_value)
            ).filter(visivel=True).order_by('-id')

            context.update({
                'projetos': projetos,
                'opcao_selecionada': opcao_selecionada,
                'search_value': search_value,
            })

        except:
            projetos = Projeto.objects.filter(
                Q(descricao__icontains=search_value) |
                Q(nome__icontains=search_value) |
                Q(conteudo__icontains=search_value) |
                Q(status__icontains=search_value)
            ).filter(visivel=True).order_by('-id')

            context.update({
                'projetos': projetos,
                'opcao_selecionada': opcao_selecionada,
                'search_value': search_value,
            })

    paginator = Paginator(projetos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'page_obj': page_obj,
    })

    return render(request, 'portfolio/projetos.html', context)


def projeto(request, slug):
    projeto = Projeto.objects.get(slug=slug)
    context = {
        'page_title': 'projeto',
        'projeto': projeto,
    }
    return render(request, 'portfolio/my_page.html', context)
