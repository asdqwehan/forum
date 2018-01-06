from django import forms
from myforum.models import Comments, Bbs

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['content']

class BbsForm(forms.ModelForm):
    class Meta:
        model = Bbs
        fields = ('title', 'content')
