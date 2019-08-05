from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models.user_model import User

from xlib.django.models import COUNTRIES_TUPLES
from xlib.enums import Gender


class UserRegisterForm(UserCreationForm):

    username = forms.CharField(max_length=50)

    first_name = forms.CharField(
        required=True,
        max_length=45,
        label='First Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'John',}
        )
    )

    last_name = forms.CharField(
        required=True,
        max_length=45,
        label='Last Name',
        widget=forms.TextInput(
            attrs={'placeholder': 'Woo',}
        )
    )

    email = forms.EmailField(
        required=True,
        max_length=70,
        widget=forms.EmailInput(
            attrs={'placeholder': 'email@example.com',}
        )
    )

    phone = forms.CharField(
        required=False,
        max_length=45,
        widget=forms.TextInput(
            attrs={'placeholder': '650-449-7300',}
        )
    )

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

    birthday = forms.DateField(
        # input_formats='%d/%m/%Y',
        label='Birthday',
        help_text='month/day/year',
        required=True,
        # widget=forms.DateInput(format='%d/%m/%Y')
    )

    class Meta:
        # create a new user when form validate
        model = User

        # field to show on the forms
        fields = ['username', 'first_name', 'last_name', 'phone',
                  'email', 'gender', 'birthday', 'country', 'password1',
                  'password2',
                  ]
