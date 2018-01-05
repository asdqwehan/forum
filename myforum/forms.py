from django import forms
from myforum.models import Comments

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']