from main.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, authenticate

class RegistrationForm(UserCreationForm):

    email = forms.EmailField(max_length=255, help_text="Required. Add a valid email address.")
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(f"Email {email} is already in use.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = user.email.replace("@gmail.com", "")
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        
        if commit:
            user.save()

        return user


class UserAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid Login")