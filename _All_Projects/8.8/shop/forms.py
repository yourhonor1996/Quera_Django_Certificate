from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDERS)
    full_name = forms.CharField()
    height = forms.IntegerField()
    age = forms.IntegerField()
