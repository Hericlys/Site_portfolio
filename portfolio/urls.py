from django.urls import path
from portfolio import views as v

app_name = 'portfolio'

urlpatterns = [
    path('', v.home, name='home'),
]