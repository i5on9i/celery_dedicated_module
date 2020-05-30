
from enum import Enum

import requests

from gigas.celconfig import CUMA_IP_ADDRESS, CUMA_IP_PORT

class NoValue(Enum):
    def __repr__(self):
        return '<%s.%s>' % (self.__class__.__name__, self.name)


class MyApi(NoValue):
    GET_INFORMATION= 'getInformation'

