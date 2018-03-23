Title: namedtuple 
Date: 2017-06-23 20:20
Category: 学习笔记
tags: python

&emsp;&emsp;collections.namedtuple是一个工厂函数,它可以用来构建个一个带字段名的元祖和一个有名字的类，

这个带名字的类对调试有很大帮助。

&emsp;&emsp;用namedtuple构建的类的实例和元祖所需内存是一样的，因为字段名都被存在对应的类里，这个实

例和普通的实例对象比起来也要小一些，因为python不用__dict__存放这些实例的属性。

&emsp;&emsp;创建一个namedtuple，需要传两个参数，一个是类名，一个是类的各个字段名，后者可是数个字符

组成的可迭代对象或者是由空格分隔开的字段名组成的字符串。存放在对应字段里的数据要以一段参数

的形式传入到构造函数中(注意：元祖的构造函数却只接受单一的可迭代对象)。

&emsp;&emsp;可以通过字段名或者位置来获取一个字段信息。

&emsp;&emsp;namestuple除了从普通元祖继承来的属性，还有一些专有属性，最有用的是类属性_fields,类方法

_make(iterable),实例方法_asdict().

    >>> import collections
    >>> s = collections.namedtuple('s', 'a b c')
    >>> s._fields
    ('a', 'b', 'c')
    >>> data = ('1', '2', '3')
    >>> i = s._make(data)
    >>> i._asdict()
    OrderedDict([('a', '1'), ('b', '2'), ('c', '3')])
