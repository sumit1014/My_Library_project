from django.forms import ModelForm
from.models import Book
from django import forms

class Bookform(forms.ModelForm):
    class Meta:
        model=Book
        fields='__all__'    


class Updatebookform(forms.ModelForm):
    class Meta:
        model=Book
        fields = ["book_name","author","price","category","book_num"]
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_box'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_box'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'id': 'input_box'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'id': 'input_box'}),
            'book_num': forms.NumberInput(attrs={'class': 'form-control', 'id': 'input_box'}),
        }   

