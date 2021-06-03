from django.forms import ModelForm, DateInput
from cal.models import Leave

class EventForm(ModelForm):
  class Meta:
    model = Leave
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'From': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      'To': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
    }
    fields = ('leave_type','Reason','From','To')

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats parses HTML5 datetime-local input to datetime field
    self.fields['From'].input_formats = ('%Y-%m-%d',)
    self.fields['To'].input_formats = ('%Y-%m-%d',)
