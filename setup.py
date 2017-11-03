# -*- coding: utf-8 -*-

from setuptools import setup

import os.path

base_dir = os.path.dirname(__file__)

about = {}
with open(os.path.join(base_dir, "dogpile_appengine", "__about__.py")) as f:
    exec(f.read(), about)

setup(
    name="dogpile_appengine",
    description="dogpile.cache backend for Memcache on Google AppEngine",
    version=about["__version__"],
    license=about["__license__"],
    author=about["__author__"],
    author_email=about["__email__"],
    keywords="python dogpile memcache backend appengine",

    install_requires=[
    ],

    packages=[
        "dogpile_appengine"
    ],

    entry_points={
        'dogpile.cache': [
            'appengine_memcache = '
            'dogpile_appengine.backend:AppEngineMemcacheBackend',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
