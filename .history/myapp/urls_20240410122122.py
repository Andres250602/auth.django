from django.urls import path
from . import views
urlpatterns = [
    path ('signup/', views.signup, name='signup'),
    path ('', views.home, name='home'),
    path ('tasks/', views.tasks, name='tasks'),

]