import uuid
from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=100)
    created_datetime = models.DateTimeField("date created", auto_now_add=True)
    last_updated_datetime = models.DateTimeField("date created", auto_now=True)
    def __str__(self):
        return self.email
    
class Original_Text_Status(models.IntegerChoices):
    DRAFT = 0, "下書き"
    WAITING_FOR_ACTION = 1, "対応待ち"
    TRANSLATION_ONGOING = 2, "翻訳中"
    TRANSLATION_COMPLETED = 3, "翻訳済み"

class Original_Text(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    extra_info = models.CharField(max_length=10000, blank=True)
    # add image, video etc
    status = models.IntegerField(default=Original_Text_Status.DRAFT, choices=Original_Text_Status.choices)
    created_datetime = models.DateTimeField("date created", auto_now_add=True)
    last_updated_datetime = models.DateTimeField("date created", auto_now=True)
    def __str__(self):
        return self.text

class Translated_Text(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    original_text_id = models.ForeignKey(Original_Text, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    created_datetime = models.DateTimeField("date created", auto_now_add=True)
    last_updated_datetime = models.DateTimeField("date created", auto_now=True)
    def __str__(self):
        return self.text
