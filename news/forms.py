from django.forms import ModelForm
from .models import Post, Author, Category
from django import forms

# Создаём модельную форму для создания, редактирования объектов (постов)
class PostForm(ModelForm):
    postCats = forms.ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Выберите категории поста'
    )
    postAuthor = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        widget=forms.Select,
        label='Выберите автора'
    )

# В класс мета, как обычно, надо написать модель, по которой будет строиться форма, и нужные нам поля.
# Мы уже делали что-то похожее с фильтрами
    class Meta:
        model = Post
        fields = ['post_type', 'postTitle', 'postText','postCats', 'postAuthor']
        widgets = {
            'post_type': forms.Select(attrs={
                'class': 'form-control',
            }),
            'postTitle' : forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите заголовок поста',
            }),
            'postText' : forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Введите текст поста',
            }),
        }
        labels = {
            'post_type': 'Выберите тип поста',
            'postTitle': 'Заголовок',
            'postText': 'Текст',
        }
