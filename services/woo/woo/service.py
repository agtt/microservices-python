from nameko.rpc import rpc
# from nameko_sentry import SentryReporter
from nameko.events import BROADCAST, event_handler
from utils import timeout


import time
import random
import os
import uuid
from woocommerce import API


class WoocommerceService:
    name = "woocommerce"

    uid = uuid.uuid4()

    @rpc
    def auth(self):
        return API(
            url="https://gourmetladies.co",
            consumer_key="ck_1847ea2a2a046b162792fcfc2d24c4cf61ed4bb8",
            consumer_secret="cs_2e8d71f7b72a2f2505b8b3deb4800dc581f7b203",
            version="wc/v3"
        )

    @rpc
    def orders(self,name):
        import json
        test = self.auth().get('orders')
        time.sleep(random.randint(0, int(os.getenv("RANDOM_TIMEOUT", "0"))))
        return test.json()

    @rpc
    def order(self, id):
        return "Get Order Service {}".format(id)

    @rpc
    def products(self, id):
        return self.auth().get('products').json()

    @rpc
    def product(self, id):
        return "Get Product Service {}".format(id)
