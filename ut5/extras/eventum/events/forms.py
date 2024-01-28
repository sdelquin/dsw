from django import forms

from .models import Event


class AddEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'description', 'important')
        widgets = {'date': forms.widgets.DateInput(attrs={'type': 'date'})}
