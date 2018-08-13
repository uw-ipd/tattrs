import attr
import torch
import numpy

import pytest

import tattr


def test_attrib_metadata():
    """tattrs are defined by metadata on attrs classes.

    * Dispatches through ``attr.s`` if the class is not already attr-ed.
    * Creates __tattr_attrs__ entries for any attribs with "tensor" metadata.
    * Captures the target tensor type from the attr.ib.
    """


    @tattr.s
    class Point(object):
        foo = attr.ib()

        x = attr.ib(metadata=dict(tensor=torch.Tensor))
        y = attr.ib(metadata=dict(tensor=numpy.ndarray))

    len(attr.fields(Point)) == 3
    len(tattr.tensor_fields(Point)) == 2

    tattr.tensor_fields(Point).x.tensor_type == torch.Tensor
    tattr.tensor_fields(Point).y.tensor_type == numpy.ndarray


def test_tensor_fields():
    """Tensor fields accessor accesses tensor attributes.

    * Returns tuple of tensor attributes, accessible by name or position.
    * Raises TypeError if passed an instance.

    * Raises NotTattrsClassError if passed a non-tattrs type.
    * Raises TypeError if passed an unrelated value
    """

    # passed class
    @tattr.s
    class Point(object):
        foo = attr.ib()

        x = attr.ib(metadata=dict(tensor=torch.Tensor))
        y = attr.ib(metadata=dict(tensor=numpy.ndarray))

    len(attr.fields(Point)) == 3
    len(tattr.tensor_fields(Point)) == 2

    # Access by name
    tattr.tensor_fields(Point).x.tensor_type == torch.Tensor
    tattr.tensor_fields(Point).y.tensor_type == numpy.ndarray

    # Access by position
    x, y = tattr.tensor_fields(Point)
    x.tensor_type == torch.Tensor
    y.tensor_type == numpy.ndarray

    # passed instance
    with pytest.raises(TypeError):
        tattr.tensor_fields(Point([0], [0]))

    # attrs, not tattrs, class
    @attr.s
    class AttrPoint(object):
        foo = attr.ib()

        x = attr.ib(metadata=dict(tensor=torch.Tensor))
        y = attr.ib(metadata=dict(tensor=numpy.ndarray))

    len(attr.fields(Point)) == 3
    with pytest.raises(tattr.exceptions.NotTattrsClassError):
        tattr.tensor_fields(AttrPoint)

    # Unrelated data types
    with pytest.raises(tattr.exceptions.NotTattrsClassError):
        tattr.tensor_fields(int)

    with pytest.raises(TypeError):
        tattr.tensor_fields(1663)
