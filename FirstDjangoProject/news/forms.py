from .models import New_post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class New_postForm(ModelForm):
	class Meta:
		model = New_post
		fields = ['title', 'short_desc', 'text', 'pub_date', 'name']
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Заголовок новости'}),
            'short_desc': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание новости'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Текст новости'}),
            'pub_date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
            'name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя автора'}),
		}

