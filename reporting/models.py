from django.db import models
# Creates your models here.
class User(models.Model):
    full_name = models.CharField(max_length=300, null=True, blank=True)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "Message from:" + self.email
            