# # filepath: /f:/DigiREC/regis/webapp/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('login/', views.login, name='login'),
#     path('logout/', views.logout, name='logout'),
#     path('register/', views.register_user, name='register_user'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register_user'),
]