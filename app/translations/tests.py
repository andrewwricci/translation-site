import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Original, Status


class OriginalModelTests(TestCase):
    def test_was_published_recently_with_future_original(self):
        """
        was_published_recently() returns False for original texts whose created_datetime
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(seconds=1)
        future_original = Original(created_datetime=time)
        self.assertIs(future_original.was_published_recently(), False)

    def test_was_published_recently_with_old_original(self):
        """
        was_published_recently() returns False for original texts whose created_datetime
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_original = Original(created_datetime=time)
        self.assertIs(old_original.was_published_recently(), False)


    def test_was_published_recently_with_recent_original(self):
        """
        was_published_recently() returns True for original texts whose created_datetime
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_original = Original(created_datetime=time)
        self.assertIs(recent_original.was_published_recently(), True)

    def test_is_status_editable_with_editable_status(self):
        status = int(Status.DRAFT)
        editable_original = Original(status=status)
        self.assertIs(editable_original.is_status_editable(), True)

    def test_is_status_editable_with_uneditable_status(self):
        status = int(Status.TRANSLATION_ONGOING)
        uneditable_original = Original(status=status)
        self.assertIs(uneditable_original.is_status_editable(), False)
