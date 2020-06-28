from django import forms
from .models import Employee


class EForm (forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Name', 'empid','email','Mobile' ,'position']

    def __init__(self, *args, **kwargs):
          super (EForm,self).__init__(*args, **kwargs)
          self.fields['position'].empty_label='Select '