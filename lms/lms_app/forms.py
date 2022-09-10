from django import forms
from .models import *
class Categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields = [
            'name'
             ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
             }

class Bookform(forms.ModelForm):
    class Meta:
        model=Books
        fields = [
            'title',
            'author',
            'photo_book',
            'photo_author',
            'pages',
            'price',
            'retal_price_day',
            'retal_period',
            'total_price_of_retal',
            'status',
            'category'

               ]

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'photo_book': forms.FileInput(attrs={'class':'form-control'}),
            'photo_author': forms.FileInput(attrs={'class':'form-control'}),
            'pages': forms.NumberInput(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'retal_price_day': forms.NumberInput(attrs={'class':'form-control', 'id':'retal_price_day'}),
            'retal_period': forms.NumberInput(attrs={'class':'form-control','id':'retal_period'}),
            'total_price_of_retal': forms.NumberInput(attrs={'class':'form-control','id':'total_price_of_retal'}),
            'status': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'})
          }