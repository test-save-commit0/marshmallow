"""Abstract base classes.

These are necessary to avoid circular imports between schema.py and fields.py.

.. warning::

    This module is treated as private API.
    Users should not need to use this module directly.
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class FieldABC(ABC):
    """Abstract base class from which all Field classes inherit."""
    parent = None
    name = None
    root = None


class SchemaABC(ABC):
    """Abstract base class from which all Schemas inherit."""
