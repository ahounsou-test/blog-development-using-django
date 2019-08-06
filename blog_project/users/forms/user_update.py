from django import forms
from users.models.user_model import User

from xlib.django.models import COUNTRIES_TUPLES
from xlib.enums import Gender



class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField( )

    last_name = forms.CharField( )

    email = forms.EmailField()

    phone = forms.CharField()

    country = forms.ChoiceField(
        required=True,
        choices=COUNTRIES_TUPLES,
        widget=forms.Select(
            attrs={'class': 'form-control input-sm'}
        )
    )

    gender = forms.ChoiceField(
        required=True,
        choices=Gender.values(),
        widget=forms.Select(
            attrs={'class': 'form-control input-sm'}
        )
    )

    birthday = forms.DateField()

    class Meta:
        # create a new user when form validate
        model = User

        # field to show on the forms
        fields = ['username', 'first_name', 'last_name', 'phone', 'email', 'gender', 'birthday', 'country',]
