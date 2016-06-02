# -*- coding: utf-8 -*-
import six
from redis import StrictRedis

from .base import BaseReader


class Reader(BaseReader):
    """
    Redis settings Reader
    A simple redis getter
    """
    _default_conf = {'host': 'localhost', 'port': 6379}

    def __init__(self, conf):
        super(Reader, self).__init__(conf)

        self.redis = StrictRedis(
            host=self.conf['host'],
            port=self.conf['port']
        )

    def _get(self, key):
        result = self.redis.get(key)
        if isinstance(result, six.binary_type):
            result = result.decode('utf-8')
        return result