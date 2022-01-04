from django import forms 
class StudentForm(forms.Form):
    name=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
