from django import forms

from .models import Post


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {'title': forms.widgets.TextInput(attrs={'class': 'form-control'})}
