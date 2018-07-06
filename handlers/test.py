from handlers.base import BaseHandler

import logging
logger = logging.getLogger('boilerplate.' + __name__)


class TestHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")
        
    def post(self):
        name = self.get_json_argument("name")
        self.write("Hello " + name)    