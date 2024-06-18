from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f'Message from {self.sender} to {self.recipient} in SELF.BUSINESS'

    @property
    def sender_is_business(self):
        return self.sender.business.exists()

    @property
    def recipient_is_business(self):
        return self.recipient.business.exists()