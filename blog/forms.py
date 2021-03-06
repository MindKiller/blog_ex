from django import forms
from blog.models import Page,Category, UserProfile, Comment


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=256,help_text="Категория:")
    class Meta:
        model = Category
        fields = ('name',)
        exclude = ('note_number',)
    def __str__(self):
        return self.name

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,help_text="Название статьи")
    #author = forms.CharField(max_length=128)
    content = forms.CharField(widget=forms.Textarea,help_text="Содержание")
    class Meta:
        model = Page
        exclude = ('date_print','author','category','views','likes','id','dislikes','favorite')
    def __str__(self):
        return self.title


class UserProfileForm(forms.ModelForm):
    picture =  forms.ImageField(required=False,)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = forms.ChoiceField(initial='M',choices=GENDER_CHOICES,)
    class Meta:
        model = UserProfile
        exclude = ('username','pages','authors','subscribers','feed')



class CommentForm(forms.ModelForm):
    #author = forms.CharField(max_length=128)
    content = forms.CharField(widget=forms.Textarea, help_text="Содержание")
    class Meta:
        model = Comment
        exclude = ('date_print','author','owner','avatar')










