from django.urls import path
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    # CRUD
    path('create/', create, name="create"),
    path('update/<int:pk>/', update, name="update"),

    # Auth
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path(
        'validated_email/<slug:authentication_token>',
        validated_email,
        name="validated_email"
    ),

    # password
    path(
        'password_recovery_request/',
        password_recovery_request,
        name='password_recovery_request'
    )

]