from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from phonenumber_field.formfields import PhoneNumberField

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email')

class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label = 'パスワード',
        strip = False,
        widget = forms.PasswordInput(),
        help_text = '8文字以上、数字のみではない'
    )
    password2 = forms.CharField(
        label = 'パスワード再入力',
        strip = False,
        widget = forms.PasswordInput(),
        help_text = '以上のパスワードと同じもの'
    )
    phone_number = PhoneNumberField(
        label = '携帯番号',
        help_text = 'ハイフンは不要です。海外の番号の場合、「+」と国番号の後に電話番号を入力してください。例：+1XXXXXXX'
    )

    class Meta:
        model = get_user_model()
        fields = ('email', 'phone_number', 'password1', 'password2')
        labels = {
                'email': 'メールアドレス',
            }
