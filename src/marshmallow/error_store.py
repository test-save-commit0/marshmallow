"""Utilities for storing collections of error messages.

.. warning::

    This module is treated as private API.
    Users should not need to use this module directly.
"""
from marshmallow.exceptions import SCHEMA


class ErrorStore:

    def __init__(self):
        self.errors = {}

    def store_error(self, field_name, error):
        """Store an error message for a field."""
        if field_name not in self.errors:
            self.errors[field_name] = []
        self.errors[field_name].append(error)

    def get_errors(self):
        """Return all stored errors."""
        return self.errors


def merge_errors(errors1, errors2):
    """Deeply merge two error messages.

    The format of ``errors1`` and ``errors2`` matches the ``message``
    parameter of :exc:`marshmallow.exceptions.ValidationError`.
    """
    merged = errors1.copy()
    for key, value in errors2.items():
        if key in merged:
            if isinstance(merged[key], dict) and isinstance(value, dict):
                merged[key] = merge_errors(merged[key], value)
            elif isinstance(merged[key], list) and isinstance(value, list):
                merged[key].extend(value)
            else:
                merged[key] = [merged[key], value]
        else:
            merged[key] = value
    return merged
