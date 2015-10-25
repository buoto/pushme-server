import factory
from accounts import models

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = models.User
