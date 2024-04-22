from django.forms import ModelForm
from .models import tarea
class TaskForm(ModelForm):
    class Meta:
        Model = tarea
        fields = ['title', 'description', 'important']
        
    

