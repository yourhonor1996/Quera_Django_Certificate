from django import forms

# Implement `UploadFileForm` form here

class UploadFileForm(forms.Form):
    file_name = forms.CharField(min_length=3, max_length= 30)
    file = forms.FileField()