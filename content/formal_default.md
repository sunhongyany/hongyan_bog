title: 使用可变类型作为参数的默认值
Date: 2017-06-28 20:30
Category: python

```python
In [115]: class Bus():
     ...:     def __init__(self, passengers=[]):
     ...:         self.passengers = passengers
     ...:     def pick(self, name):
     ...:         self.passengers.append(name)
     ...:     def drop(self, name):
     ...:         self.passengers.remove(name)
     ...:

In [116]: bus1 = Bus(['a', 'b'])

In [117]: bus1.pick('c')

In [118]: bus1.passengers
Out[118]: ['a', 'b', 'c']

In [119]: bus1.drop('a')

In [120]: bus2 = Bus()

In [121]: bus2.passengers
Out[121]: []

In [122]: bus2.pick('a')

In [123]: bus2.passengers
Out[123]: ['a']

In [124]: bus3 = Bus()

In [125]: bus3.passengers
Out[125]: ['a']
```

我们定义了一个Bus类，从上面可以看到，我们创建bus3时并没有传入任何参数，但是列表却不是空

的，而是用的bus创建的列表。所以当我们使用可变类型作为函数的参数默认值时要小心。

对上面程序可以修改为：

```python
In [126]: class Bus():
     ...:     def __init__(self, passengers=None):
     ...:         if passengers is None:
     ...:             self.passengers = []
     ...:         else:
     ...:             self.passengers = passengers
     ...:     def pick(self, name):
     ...:         self.passengers.append(name)
     ...:     def drop(self, name):
     ...:         self.passengers.remove(name)
     ...:
```

如果不想修改实参，那应该创建个副本给self.passengers，即：

```python
def __init__(self, passengers=None):
    if passengers is None:
        self.passengers = []
    else:
        self.passengers = list(passengers)
```
