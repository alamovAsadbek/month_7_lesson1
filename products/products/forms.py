from django import forms

from products.models import ColorModel


class ColorPickerForm(forms.ModelForm):
    class Meta:
        model = ColorModel
        fields = ['name', 'code']
        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }