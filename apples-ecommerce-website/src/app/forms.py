# File: forms.py (Python)

from django import forms
from .models import Apple

class AppleForm(forms.ModelForm):
    class Meta:
        model = Apple
        fields = ['name', 'origin', 'taste', 'nutritional_info', 'price', 'image']

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than 0.")
        return price

    def clean_image(self):
        image = self.cleaned_data['image']
        # Add validation logic for image file type and size if needed
        return image