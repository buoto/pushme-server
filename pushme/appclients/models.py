from django.db import models
import accounts.models
import datetime
import hashlib

class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(accounts.models.User)
    apikey = models.CharField(max_length=100)

    def generate_api_key(self):
        seed = unicode(datetime.datetime.utcnow()) + self.name
        self.apikey = hashlib.md5(seed.encode()).hexdigest()
        return self.apikey
