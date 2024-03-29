from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import CustomUser, Ticket, Comment

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser 
        fields = ('username', 'email','role','password1', 'password2')  

class ProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','gender','age','date_of_birth','address','username','email','role']


class LoginForm(AuthenticationForm):
    pass

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # fields = '__all__'
        fields = ['status_code','priority','company_name','ticket_ref','assigned_to','resolved_by','code','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']