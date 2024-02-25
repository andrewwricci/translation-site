import datetime
import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()
    
class Status(models.IntegerChoices):
    DRAFT = 0, "下書き"
    WAITING_FOR_ACTION = 1, "対応待ち"
    TRANSLATION_ONGOING = 2, "翻訳中"
    TRANSLATION_COMPLETED = 3, "翻訳済み"

class EditableStatus(models.IntegerChoices):
    DRAFT = 0, "下書き"
    WAITING_FOR_ACTION = 1, "対応待ち"

class Original(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    extra_info = models.CharField(max_length=10000, blank=True)
    # add image, spreadsheet, video etc
    status = models.IntegerField(default=Status.DRAFT, choices=Status.choices)
    created_datetime = models.DateTimeField("date created", auto_now_add=True)
    last_updated_datetime = models.DateTimeField("date updated", auto_now=True)

    def __str__(self):
        return self.text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_datetime <= now
    
    def is_status_editable(self):
        return self.status in EditableStatus

class Translation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    original_id = models.ForeignKey(Original, on_delete=models.CASCADE)
    text = models.CharField(max_length=10000)
    created_datetime = models.DateTimeField("date created", auto_now_add=True)
    last_updated_datetime = models.DateTimeField("date created", auto_now=True)
    def __str__(self):
        return self.text
