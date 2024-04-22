from django.urls import path
from . import views
urlpatterns = [
    path ('', views.signup, name=s'signup'),
    path ('home/', views.home, name='home'),

]