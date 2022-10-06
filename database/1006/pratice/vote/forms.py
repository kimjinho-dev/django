from .models import Vote, Comment
from django import forms

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ('question',)