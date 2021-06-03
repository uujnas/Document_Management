from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    def __str__(self):
        return Event.objects.filter(user=request.user)
    
class Leave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    leave_type = models.CharField(max_length=100,null=True)
    Reason = models.TextField(null=True)
    From = models.DateField(null=True)
    To = models.DateField(null=True)
    

    @property
    def get_html_url(self):
        url = reverse('cal:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'