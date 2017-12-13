title: 内置类型方法
Date: 2017-08-26 20:30
Category: python

内置类型的方法基本上不会调用子类覆盖的方法。例如，dict的子类覆盖的__getitem__()不会被内置类

型的get()调用内置类型dict的__init__,__update__方法会忽略我们覆盖的__setitem__方法。

```python
In [90]: class D(dict):
    ...:     def __setitem__(self, key, value):
    ...:         super().__setitem__(key, [value] * 2)
    ...:

In [91]: d = D()

In [92]: d = D(one=[1])

In [93]: d
Out[93]: {'one': [1]}

In [94]: d['two'] = 2

In [95]: d
Out[95]: {'one': [1], 'two': [2, 2]}

In [96]: d.update(three=3)

In [97]: d
Out[97]: {'one': [1], 'three': 3, 'two': [2, 2]}
```

直接子类化内置类型（如dict，list或str）容易出错，因为内置类型的方法通常会忽略用户覆盖的方法

不要子类话内置类型，用户自己定义的类应该继承collections模块中的类，例如UserDict，UserList，

UserString，这些类做了特殊设计，因此易于扩展。
