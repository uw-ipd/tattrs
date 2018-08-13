import collections

import attr

from attr._compat import isclass

from .exceptions import NotTattrsClassError


@attr.s(frozen=True)
class TensorAttribute(object):
    name = attr.ib(type=str)
    tensor_type = attr.ib(type=type)


def tensor_fields(cls):
    """
    Return tuple of tensor attributes for a class.

    The tuple also allows accessing the fields by their names.

    :param type cls: Class to introspect.

    :raise TypeError: If *cls* is not a class.
    :raise tattr.exceptions.NotTattrsClassError: If *cls* is not an
        ``tattrs`` class.

    :rtype: tuple (with name accessors) of :class:`tattr.TensorAttribute`
    """

    if not isclass(cls):
        raise TypeError("Passed object must be a class.")

    tattrs = getattr(cls, "__tattrs_attrs__", None)
    if tattrs is None:
        raise NotTattrsClassError(
            "{cls!r} is not an attrs-decorated class.".format(cls=cls)
        )
    return tattrs


def tattrs(cls):
    if not attr.has(cls):
        cls = attr.s(cls)

    tensor_attrs = [
        TensorAttribute(f.name, f.metadata.get("tensor")) for f in attr.fields(cls) if f.metadata.get("tensor")
    ]

    container = collections.namedtuple("{}TensorAttributes".format(cls.__name__), [t.name for t in tensor_attrs])

    cls.__tattrs_attrs__ = container(*tensor_attrs)

    return cls


s = tattrs
