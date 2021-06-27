from django.forms import ModelForm
from .models import *

class OrderForm(ModelForm):
    class Meta:
        model=order
        fields='__all__'