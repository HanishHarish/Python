from django import forms
from . models import employee

class employeeform(forms.ModelForm):
    class Meta: # dout 
        model = employee

        fields = ('name','mobile','address','email','designation')        
        

        widgets = { 
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),
            'mobile':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter mobile number'}),
            'address':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter address'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your email'}),
            'designation':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your designation'}),
        }
