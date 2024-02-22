from django.forms import ModelForm, BooleanField, HiddenInput
from .models import Original

class OriginalExistingUserForm(ModelForm):

    class Meta:
        model = Original
        fields = ['text', 'extra_info']
        labels = {
            'text': '文章',
            'extra_info': '補足'
        }

# 最終的にemailという値で新しいoriginalを作りながら新しいユーザを作る

# class OriginalNewUserForm(ModelForm):

#     class Meta:
#         model = Original
#         fields = ['text', 'extra_info', 'email']
#         labels = {
#             'text': '文章',
#             'extra_info': '補足',
#             'email': 'メールアドレス'
#         }