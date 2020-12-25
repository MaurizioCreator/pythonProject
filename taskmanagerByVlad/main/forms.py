from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "myTask"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title'
            }),
            "myTask": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the description'
            }),
        }