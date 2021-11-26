from django.db import models

from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task
