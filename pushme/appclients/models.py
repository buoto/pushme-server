from django.db import models
import accounts.models
import datetime
import hashlib
from django.utils.timezone import now

def generate_api_key():
    seed = unicode(datetime.datetime.utcnow())
    return hashlib.md5(seed.encode()).hexdigest()

class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(accounts.models.User, related_name='clients')
    apikey = models.CharField(max_length=100, default=generate_api_key)
    created_at = models.DateTimeField(default=now)

    def regenerate_api_key(self):
        self.apikey = generate_api_key()
        self.save()
        return self.apikey
