from django.forms import ModelForm
from .models import Original_Text

class OriginalTextForm(ModelForm):
    class Meta:
        model = Original_Text
        fields = ['user_id', 'text']
        labels = {
            'user_id': 'ユーザID',
            'text': '文章'
        }