from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class TestHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")