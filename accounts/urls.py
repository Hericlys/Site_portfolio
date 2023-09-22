from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('create/', create, name="create"),
    path('login/', login, name="login"),
    path('update/<int:pk>/', update, name="update"),
    path('logoff/', logoff, name="logoff"),
]