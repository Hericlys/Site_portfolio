from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('create/', create, name="create"),
    path('login/', login, name="login"),
    path('update/<int:pk>/', update, name="update"),
    path('logout/', logout, name="logout"),
    path('validated_email/<slug:activation_token>', validated_email, name="validated_email"),
]