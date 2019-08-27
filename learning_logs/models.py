from django.db import models

# Create your models here.
class Topic(models.Model):
    # Current topic user is interested in
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        #returns string representation of self
        return self.text

class Entry(models.Model):
    # Information about topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        #returns string representation of self
        return f"{self.text[:50]}..."
