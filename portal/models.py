from django.db import models

class Message(models.Model):
    message_text = models.CharField(max_length=800)
    sent_date = models.DateTimeField('date sent')
    def __str__(self):
        return self.message_text
    
