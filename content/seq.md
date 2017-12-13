title: 序列的修改，散列和切片
Date: 2017-08-25 20:30
Category: python

```python
In [84]: from array import array

In [85]: import reprlib

In [86]: import math

In [87]: import numbers

In [88]: import functools

In [89]: import operator

In [90]: class Vector:
    ...:     typecode = 'd'
    ...:     def __init__(self, components):
    ...:         self._components = array(self.typecode, components)
    ...:     def __iter__(self):
    ...:         return iter(self._components)
    ...:     def __repr__(self):
    ...:         components = reprlib.repr(self._components)
    ...:         components = components[components.find('['):-1]
    ...:         return 'Vector({})'.format(components)
    ...:     def __str__(self):
    ...:         return str(tuple(self))
    ...:     def __bytes__(self):
    ...:         return (bytes([ord(self.typecode)])) + bytes(self._components)
    ...:     def __eq__(self, other):
    ...:         return len(self) == len(other) and all(a == b for a, b in zip(self, other))
    ...:     def __abs__(self):
    ...:         return math.sqrt(sum(x*x for x in self))
    ...:     def __bool__(self):
    ...:         return bool(abs(self))
    ...:     @classmethod
    ...:     def frombytes(cls, octets):
    ...:         typecode = chr(octets[0])
    ...:         memv = memoryview(octets[1:]).cast(typecode)
    ...:         return cls(memv)
    ...:     def __len__(self):
    ...:         return len(self._components)
    ...:     def __getitem__(self, index):
    ...:         cls = type(self)
    ...:         if isinstance(index, slice):
    ...:             return cls(self._components[index])
    ...:         elif isinstance(index, Integral):
    ...:             return self._components[index]
    ...:         else:
    ...:             msg = '{cls.__name__} indices must be integers'
    ...:             raise TypeError(msa.format(cls=cls))
    ...:     shortcut_names = 'xyzt'
    ...:     def __getattr__(self, name):
    ...:         cls = type(self)
    ...:         if len(name) == 1:
    ...:             pos = cls.shortcut_names.find(name)
    ...:             if 0 <= pos < len(self._components):
    ...:                 return self._components[pos]
    ...:         msg = '{.__name__!r} object has no attribute {!r}'
    ...:         raise AttributeError(msg.format(cls, name))
    ...:     def __hash__(self):
    ...:         hashes = (hash(x) for x in self._components)
    ...:         return functools.reduce(operator.xor, hashes, 0)
    ...:
```

reprlib.repr这个函数用于生成大型结构或递归结构的安全表示形式，他限制输出字符串长度，用···表示截断部分。
