from django.urls import path
from portfolio import views as v

app_name = 'portfolio'

urlpatterns = [
    path('', v.home, name='home'),
    path('projetos/', v.projetos, name='projetos'),
    path('projeto/<slug:slug>', v.projeto, name='projeto'),
]