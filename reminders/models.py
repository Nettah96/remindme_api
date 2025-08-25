from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
