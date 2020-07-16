from django import forms
from basic_app.models import Post,Comment
from django.contrib.auth.models import User
from django.forms import ModelForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'blogger_name','blog_pic_1','text_1','blog_pic_2', 'text_2', 'blog_pic_3','text_3',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text_1': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'text_2': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'text_3': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
# class SubscriptionForm(forms.ModelForm):
#     class Meta:
#         model=Subscription
#         fields=('mail_id',)
