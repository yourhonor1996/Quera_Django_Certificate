from django import forms


class PersonalInformation(forms.Form):
    GENDERS = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = forms.ChoiceField(choices=GENDERS)
    full_name = forms.CharField(min_length= 5, max_length= 60)  # 5 <= fullname's length <= 60
    height = forms.IntegerField(min_value= 70, max_value= 250)
    age = forms.IntegerField(min_value= 14, max_value= 99)

    def clean_full_name(self):
        full_name = self.cleaned_data['full_name']
        if not full_name.istitle():
            raise forms.ValidationError('error message')
        return full_name