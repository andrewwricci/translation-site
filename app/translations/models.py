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

class Original_Text(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    # add extra info for context
    # add image
    # add status (下書き、受付待ち、翻訳中、翻訳済みなど)
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
