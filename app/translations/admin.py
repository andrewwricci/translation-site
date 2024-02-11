from django.contrib import admin

from .models import User, Original_Text, Translated_Text

admin.site.register(User)
admin.site.register(Original_Text)
admin.site.register(Translated_Text)
