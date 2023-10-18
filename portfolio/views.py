from django.shortcuts import render
from portfolio.models import CategoriaProjeto, Projeto, Assunto, Trabalho
from django.db.models import Q
from django.core.paginator import Paginator
from accounts.models import User
from utils.rands import random_letters
from django.contrib import messages


def projetos(request):
    projetos = Projeto.objects.filter(visivel=True).order_by('-id')
    categorias = CategoriaProjeto.objects.all()
    context = {
        'projetos': projetos,
        'categorias': categorias,
        'page_title': 'Projetos',
        'search_value': '',
    }

    if 'opcao' in request.GET:
        opcao_selecionada = request.GET.get('opcao')
        search_value = str(request.GET.get('search')).strip()

        try:
            categoria = CategoriaProjeto.objects.get(slug=opcao_selecionada)
            projetos = Projeto.objects.filter(categoria=categoria.id).filter(
                Q(descricao__icontains=search_value) |
                Q(nome__icontains=search_value) |
                Q(conteudo__icontains=search_value) |
                Q(status__icontains=search_value)
            ).filter(visivel=True).order_by('-id')

            context.update({
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
                'opcao_selecionada': opcao_selecionada,
                'search_value': search_value,
            })

    paginator = Paginator(projetos, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'projetos': '',
        'page_obj': page_obj,
    })

    return render(request, 'portfolio/projetos.html', context)


def projeto(request, slug):
    try:
        projeto = Projeto.objects.get(slug=slug, visivel=True)
    except:
        context = {
            'slug': slug,
        }
        return render(request, 'portfolio/page_404.html', context)
    context = {
        'page_title': 'projeto',
        'projeto': projeto,
    }
    return render(request, 'portfolio/projeto.html', context)
