from django.forms import ModelForm, BooleanField, HiddenInput
from .models import Original_Text

class OriginalTextExistingUserForm(ModelForm):

    class Meta:
        model = Original_Text
        fields = ['text', 'extra_info']
        labels = {
            'text': '文章',
            'extra_info': '補足'
        }

# 最終的にemailという値で新しいoriginal_textを作りながら新しいユーザを作る

# class OriginalTextNewUserForm(ModelForm):

#     class Meta:
#         model = Original_Text
#         fields = ['text', 'extra_info', 'email']
#         labels = {
#             'text': '文章',
#             'extra_info': '補足',
#             'email': 'メールアドレス'
#         }