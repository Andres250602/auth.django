from django.urls import path
from . import views
urlpatterns = [
    path ('', views.signup),
    path ('home/', views.home),

]