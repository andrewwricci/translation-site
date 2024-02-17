from django.contrib import admin

from .models import Original_Text, Translated_Text

admin.site.register(Original_Text)
admin.site.register(Translated_Text)
