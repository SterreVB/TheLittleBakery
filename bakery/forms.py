from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from .models import Comments, Profile, ProfileComments, Recipes


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class CommentForm(forms.ModelForm):
    #Hidden value to get a child's parent
    parent = forms.CharField(max_length = 50, widget=forms.HiddenInput(attrs={'class': 'parent'}), required=False)

    class Meta:
        model = Comments
        fields = ['content']

class addRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ('title','caption','imageDir','bakeType','serve','prepTime','cookTime','kcal','fat','carbs','sugar','protein','salt','ingredients','recipe')


class ProfileCommentsForm(forms.ModelForm):

    class Meta:
        model = ProfileComments
        fields = ['comment']
