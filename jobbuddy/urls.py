from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register, name='register'),
    path('add', views.add, name='add'),
    path('jobs', views.jobs, name='jobs'),
    path('jobs/<int:id>', views.update, name='update'),
    path('job/<int:id>', views.details, name='details'),
]