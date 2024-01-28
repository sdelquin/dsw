from django.db import models
from django.urls import reverse


class Event(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateField()
    description = models.TextField(blank=True)
    important = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('events:detail', args=(self,))

    class Meta:
        ordering = ('date',)
        indexes = (models.Index(fields=('date',)),)
