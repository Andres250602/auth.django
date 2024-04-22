from django.forms import ModelForm
from .models import tarea

class TaskForm(ModelForm):
    class Meta:
        model = tarea  # Aquí estaba el error, Model debería ser model
        fields = ['title', 'description', 'important']
