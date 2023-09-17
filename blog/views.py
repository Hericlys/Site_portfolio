from django.shortcuts import render

def posts_views(request):
    context = {
        'page_title': 'Home - Blog'
    }
    return render(request, 'blog/posts.html', context)


def post_views(request, slug):
    pass

