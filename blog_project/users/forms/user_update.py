from django import forms
from users.models.user_model import User


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField( )

    last_name = forms.CharField( )

    email = forms.EmailField()

    phone = forms.CharField()

    country = forms.ChoiceField()

    gender = forms.ChoiceField()

    birthday = forms.DateField()

    class Meta:
        # create a new user when form validate
        model = User

        # field to show on the forms
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'gender', 'birthday', 'country',]
