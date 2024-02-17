from django.forms import ModelForm, BooleanField, HiddenInput
from .models import Original_Text

class OriginalTextForm(ModelForm):

    class Meta:
        model = Original_Text
        # 最終的にuser_idはログインしているユーザ
        fields = ['text', 'extra_info']
        labels = {
            'text': '文章',
            'extra_info': '補足'
        }