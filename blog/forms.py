# -*- coding: utf-8 -*-
from django import forms


class CommentForm(forms.Form):
    author = forms.CharField(widget=forms.TextInput(attrs={'id': 'author',
                                                           'class': 'comment_input',
                                                           'size': '25',
                                                           'tabindex': '1'}),
                             max_length=50, required=True, error_messages={'required': 'username不能为空'})
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email',
                                                           'class': 'comment_input',
                                                            'size': '25',
                                                            'tabindex': '2'}),
                             max_length=50, required=True, error_messages={'required': 'email不能为空'})
    url = forms.URLField(widget=forms.URLInput(attrs={'id': 'url',
                                                      'class': 'comment_input',
                                                      'size': '25',
                                                      'tabindex': '3',
                                                      'required': 'required'}),
                         max_length=50, required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={'id': 'comment',
                                                           'class': 'message_input',
                                                           'cols': '25',
                                                           'rows': '5',
                                                           'tabindex': '4'}),
                              required=True, error_messages={'required': '评论不能为空'})
    article = forms.CharField(widget=forms.HiddenInput)


class RegForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               max_length=50, required=True, error_messages={'required': 'username不能为空'})
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
                             max_length=50, required=True, error_messages={'required': 'email不能为空'})
    url = forms.URLField(widget=forms.URLInput(attrs={'placeholder': 'URL'}),
                         max_length=50, required=False)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               max_length=50, required=True, error_messages={'required': 'password不能为空'})


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}),
                               max_length=50, required=True, error_messages={'required': 'username不能为空'})
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
                               max_length=50, required=True, error_messages={'required': 'password不能为空'})