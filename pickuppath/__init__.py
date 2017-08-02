# -*- coding:utf-8 -*-
import logging
import os.path
logger = logging.getLogger(__name__)


def iter_parents(filename, current=None):
    current = os.path.normpath(os.path.abspath(current or os.getcwd()))
    while True:
        yield os.path.join(current, filename)
        if current == "/":
            break
        current, dropped = os.path.split(current)


def pickup_path(filename, current=None, default=None):
    """pickupping the config file path

    start path = "/foo/bar/boo", filename = "config.ini"
    finding candidates are ["/foo/bar/boo/config.ini", "/foo/bar/config.ini", "/foo/config.ini", "/config.ini"]
    """
    for path in iter_parents(filename, current):
        logger.debug("check: %s", path)
        if os.path.exists(path):
            return path
    return default
