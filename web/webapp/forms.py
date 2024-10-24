from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    phone_number = forms.CharField(max_length=15, required=True, label='Phone Number')

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.profile.phone_number = self.cleaned_data['phone_number']  # จะอธิบายส่วนนี้ต่อไป
        if commit:
            user.save()
        return user
