from django.shortcuts import render
from accounts.models import User
from blog.models import Category, Post
from django.db.models import Q
from django.core.paginator import Paginator


def posts_views(request):
    posts = Post.objects.filter(is_published=True).order_by('-id')
    categorias = Category.objects.all()
    context = {
        'page_title': 'Home - Blog',
        'categorias': categorias,
        'search_value': '',
    }

    if 'opcao' in request.GET:
        opcao_selecionada = request.GET.get('opcao')
        search_value = str(request.GET.get('search')).strip()

        try:
            categoria = CategoriaProjeto.objects.get(slug=opcao_selecionada)
            posts = Post.objects.filter(category=categoria.id).filter(
                Q(title__icontains=search_value) |
                Q(content__icontains=search_value) |
                Q(excerpt__icontains=search_value)
            ).filter(is_published=True).order_by('-id')

            context.update({
                'opcao_selecionada': opcao_selecionada,
                'search_value': search_value,
            })
        except:
            posts = Post.objects.filter(
                Q(title__icontains=search_value) |
                Q(content__icontains=search_value) |
                Q(excerpt__icontains=search_value)
            ).filter(is_published=True).order_by('-id')

            context.update({
                'opcao_selecionada': opcao_selecionada,
                'search_value': search_value,
            })

    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context.update({
        'page_obj': page_obj,
    })

    return render(request, 'blog/posts.html', context)


def post_views(request, slug):
    try:
        post = Post.objects.get(slug=slug, is_published=True)
    except:
        context = {
            'slug': slug,
        }
        return render(request, 'blog/page_404.html', context)

    context = {
        'page_title': f'post: {post.title}',
        'post': post,
    }

    return render(request, 'blog/post_views.html', context)
