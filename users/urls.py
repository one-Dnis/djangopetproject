from django.urls import path
from . import views

urlpatterns = [
    path('login', views.LoginUser.as_view(), name='login'),
    path('registration', views.RegistrationUser.as_view(), name='registration'),
    path('logout', views.logout_user, name='logout')
]
