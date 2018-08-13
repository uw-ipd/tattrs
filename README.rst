======
tattrs
======

``tattrs`` provides support for ``attrs``-style dataclass definitions over
multidimensional arrays. ``tattrs`` is array-type agnostic, supporting
``numpy`` ndarrays and ``pytorch`` tensors, but exposes underlying library
features whenever possible. ``tattrs`` combines the development joy of
boilerplate-free definitions, the safety of composable and strongly typed
dataclasses, and the power of a modern numeric libraries. Yippee ki-yay.

A quick sample, defining a 2-d coordinate system:

.. doctest::

  >>> import tattr
  >>> import torch
  >>> from math import pi

  >>> @tattr.s(auto_attribs=True, tensor=torch.Tensor)
  ... class Cartesian:
  ...     x: float
  ...     y: float
  ...
  ...     @property
  ...     def polar(self):
  ...        """Convert to polar coords."""
  ...        return Polar(
  ...            r = (self.x ** 2 + self.y ** 2) ** 1/2,
  ...            phi = torch.atan2(self.y, self.x),
  ...        )
  ...         

  >>> @tattr.s(auto_attribs=True, tensor=torch.Tensor)
  ... class Polar:
  ...     r: float
  ...     phi: float
  ...
  ...     @property
  ...     def cartesian(self):
  ...        """Convert to cartesian coords."""
  ...        return Cartesian(
  ...            x = self.r * torch.cos(self.phi),
  ...            y = self.r * torch.sin(self.phi),
  ...        )

  >>> units = Polar(r=[1, 1, 1, 1], phi=[0 * pi, 1/2 * pi, 1 * pi, 3/2 * pi])

  >>> units

  >>> units.cartesian

Of course, you be working on higher-dimensional tensors:

.. doctest::

  >>> samples = Cartesian(torch.rand(1000, 1000), torch.rand(1000, 1000))

  >>> samples.shape

Or tensors on cuda devices:

.. doctest::

  >>> cuda_samples = samples.cuda()

  >>> (cuda_samples.x + cuda_samples.y).mean()


Credits
-------

* The teams behind numpy_ and pytorch_ for exceptional core data types.
* The team behind attrs_ for a brilliant programming model.

.. _attrs: http://www.attrs.org/en/stable/
.. _numpy: http://numpy.org
.. _pytorch: http://pytorch.org
