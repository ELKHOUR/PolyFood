from django import forms 
from theapp.models import Comments

field_attrs = {'class':'form-control'}

class FormAddComments(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['user','content']    
        widgets = {

            'user' : forms.TextInput(attrs=field_attrs),
            'content' : forms.Textarea(attrs=field_attrs),
            
        }
