from nameko.rpc import rpc
# from nameko_sentry import SentryReporter
from nameko.events import BROADCAST, event_handler
from utils import timeout
from nameko_sqlalchemy import DatabaseSession
from .models import Base, Credential
from nameko.events import EventDispatcher



import time
import random
import os
import uuid


class CreDentialService:
    name = "credentials"

    uid = uuid.uuid4()
    db = DatabaseSession(Base)
    event_dispatcher = EventDispatcher()


    @rpc
    def orders(self, name):
        time.sleep(random.randint(0, int(os.getenv("RANDOM_TIMEOUT", "0"))))
        return "Hello {} is calling!".format(name)

    @rpc
    def order(self, id):
        return "Get Order Service {}".format(id)

    @rpc
    def products(self, id):
        return "Get Products Service"

    @rpc
    def product(self, id):
        return "Get Product Service {}".format(id)
