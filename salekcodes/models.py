from django.db import models
from django.utils import timezone

# region abstract/base


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)
    modified_at = AutoDateTimeField(default=timezone.now)

    class Meta:
        abstract = True


# endregion
