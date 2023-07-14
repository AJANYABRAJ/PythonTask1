from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import Login, Complaints, Notification

class StudentForm(UserCreationForm):
    class Meta:
        model=Login
        fields=('username','password1','password2','name','phone','email','address','image',)

class DateInput(forms.DateInput):
    input_type='date'

class ComplaintsForm(forms.ModelForm):
    date=forms.DateField(widget=DateInput)
    class Meta:
        model = Complaints
        fields=('title','complaint','date',)

class NotificationForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)
    class Meta:
        model=Notification
        fields=('subject','description','date',)