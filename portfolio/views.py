from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/my_page.html')
