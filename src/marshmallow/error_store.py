"""Utilities for storing collections of error messages.

.. warning::

    This module is treated as private API.
    Users should not need to use this module directly.
"""
from marshmallow.exceptions import SCHEMA


class ErrorStore:

    def __init__(self):
        self.errors = {}


def merge_errors(errors1, errors2):
    """Deeply merge two error messages.

    The format of ``errors1`` and ``errors2`` matches the ``message``
    parameter of :exc:`marshmallow.exceptions.ValidationError`.
    """
    pass
