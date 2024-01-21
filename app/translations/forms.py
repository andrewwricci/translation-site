from django.forms import ModelForm, BooleanField, HiddenInput
from .models import Original_Text

class OriginalTextForm(ModelForm):

    class Meta:
        model = Original_Text
        # 最終的にuser_idはログインしているユーザ
        fields = ['user_id', 'text', 'extra_info']
        labels = {
            'user_id': 'ユーザID',
            'text': '文章',
            'extra_info': '補足'
        }