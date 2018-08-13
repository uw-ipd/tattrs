def test_explict_metadata():
    """tattrs are defined by metadata on attrs classes.

    ``tattr.s``:
    Dispatches through ``attr.s`` if the class is not already attr-ed.
    Creates __tattr_fields__ entries for any attribs with "tensor" metadata.
    Captures the target tensor type and dtype froom the attr.ib.
    Converts the attr.ib type into the tensor-native dtype.
    """

    import attr
    import tattr
    import torch

    @tattr.s
    class Point:
        x = attr.ib(type=float, metadata=dict(tensor=torch.Tensor))
        y = attr.ib(type=int, metadata=dict(tensor=torch.Tensor))

    len(Point.__tattr_attrs__) == 2

    Point.__tattr_attrs__.x.dtype == torch.float32
    Point.__tattr_attrs__.x.tensor_type == torch.Tensor

    Point.__tattr_attrs__.y.dtype == torch.int64
    Point.__tattr_attrs__.y.tensor_type == torch.Tensor
