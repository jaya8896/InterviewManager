from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SettingsModel(models.Model):
    key = models.CharField(db_index=True, max_length=100)
    value = models.TextField(max_length=3000)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
