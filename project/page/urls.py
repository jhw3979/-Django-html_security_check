from django.urls import path
from . import views

app_name = 'project'
urlpatterns = [
    path('<int:User_id>/home/', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
    path('login/', views.login, name='login'),
    path('html/', views.show_html, name='show_html')
]

