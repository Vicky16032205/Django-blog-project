from django.urls import path
from . import views

app_name = 'Users'

urlpatterns = [
    path('register/', views.register_page, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]
