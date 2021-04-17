from django.db import models
from django.contrib.auth.models import User


class ObjectManager(models.Manager):
    def get_or_none(self, *args, **kwargs):
        try:
            return self.get(*args, **kwargs)
        except ObjectDoesNotExist:
            return None


class Task(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    name = models.CharField(max_length=255, null=False, default="New task")
    description = models.TextField(null=False, default="")
    deadline_at = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ObjectManager()
