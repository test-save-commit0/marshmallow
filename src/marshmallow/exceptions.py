"""Exception classes for marshmallow-related errors."""
from __future__ import annotations
import typing
SCHEMA = '_schema'


class MarshmallowError(Exception):
    """Base class for all marshmallow-related errors."""


class ValidationError(MarshmallowError):
    """Raised when validation fails on a field or schema.

    Validators and custom fields should raise this exception.

    :param message: An error message, list of error messages, or dict of
        error messages. If a dict, the keys are subitems and the values are error messages.
    :param field_name: Field name to store the error on.
        If `None`, the error is stored as schema-level error.
    :param data: Raw input data.
    :param valid_data: Valid (de)serialized data.
    """

    def __init__(self, message: (str | list | dict), field_name: str=SCHEMA,
        data: (typing.Mapping[str, typing.Any] | typing.Iterable[typing.
        Mapping[str, typing.Any]] | None)=None, valid_data: (list[dict[str,
        typing.Any]] | dict[str, typing.Any] | None)=None, **kwargs):
        self.messages = [message] if isinstance(message, (str, bytes)
            ) else message
        self.field_name = field_name
        self.data = data
        self.valid_data = valid_data
        self.kwargs = kwargs
        super().__init__(message)


class RegistryError(NameError):
    """Raised when an invalid operation is performed on the serializer
    class registry.
    """


class StringNotCollectionError(MarshmallowError, TypeError):
    """Raised when a string is passed when a list of strings is expected."""


class FieldInstanceResolutionError(MarshmallowError, TypeError):
    """Raised when schema to instantiate is neither a Schema class nor an instance."""
