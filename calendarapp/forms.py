from django.forms import ModelForm, DateInput
from calendarapp.models import Event, EventMember
from django import forms
from django.forms.widgets import Select, TextInput, Textarea

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    
    widgets = {
      'title' : TextInput(
          attrs={
            'class' : 'form-control'
          }
      ),
      'description' : Textarea(
          attrs={
            'class' : 'form-control'
          }
      ),
      'start_time': DateInput(
          attrs={
            'type': 'datetime-local',
            'class' : 'form-control'
            }, 
          format='%Y-%m-%dT%H:%M'
      ),
      
      'end_time': DateInput(
          attrs={
            'type': 'datetime-local',
            'class' : 'form-control'
          }, 
          format='%Y-%m-%dT%H:%M',
      )
    }
    
    exclude = ['user']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['title'].label="Judul Agenda"
    self.fields['description'].label="Deskripsi"
    self.fields['start_time'].label="Waktu Mulai"
    self.fields['end_time'].label="Waktu Selesai"


class SignupForm(forms.Form):
  username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class AddMemberForm(forms.ModelForm):
  class Meta:
    model = EventMember
    fields = ['user']
