from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_page, name="register_page"),
    path('send-code-to-email/', views.send_code_to_email, name="send_code_to_email"),
    path('login/', views.register_user, name="register_user"),
    path('login-user/', views.login_user, name="login"),
    path('logout/', views.logout_page, name="logout"),
]