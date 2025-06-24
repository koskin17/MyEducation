from django import forms
# from .models import Order
from book.models import Book
from authentication.models import CustomUser

class OrderForm(forms.Form):
    user = forms.ModelChoiceField(queryset=CustomUser.objects.all(), label='User')
    book = forms.ModelChoiceField(queryset=Book.objects.all(), label='Book')
    plated_end_at = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        label='Planned return date'
    )