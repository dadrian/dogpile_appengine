# -*- coding: utf-8 -*-

from dogpile.cache.backends.memcached import GenericMemcachedBackend


class AppEngineMemcacheBackend(GenericMemcachedBackend):
    """A backend for Google AppEngine Memcache"""

    def _imports(self):
        global memcache
        from google.appengine.api import memcache

    def _create_client(self):
        return memcache.Client()
