Title: 常见的映射方法
Date: 2017-06-24 20:30
Category: 学习笔记
Tags: python

常见的映射类型有dict，defaultdict，OrderDict。

dict中有个setdefault方法，用于处理找不到的键。

```python
    >>> d = {}
    >>> k = 'k'
    >>> d.setdefault(k, []).append('a')
    >>> d
    >>> {'k': ['a']}
```

defaultdict处理找不到键的一个选择。

```python
    >>> from collections import defaultdict

    >>> d = defaultdict(list)

    >>> d
    >>> defaultdict(list, {})

    >>> d['k'].append('a')

    >>> d
    >>> defaultdict(list, {'k': ['a']})

    >>> d['k']
    >>> ['a']
```

用来生成默认值的可调用对象存放在default_factory这个实例属性中。

    >>> d.default_factory()
    >>> []

collections.defaultdict里的defautl_factory只会在__getitem__里被调用，在其他方法里完全不发挥

作用。

    d = defaultdict(list)

```python
    >>> ['k1']
    >>> []

    >>> d
    >>> defaultdict(list, {'k1': []})

    >>> d.get('k2')

    >>> d
    >>> defaultdict(list, {'k1': []})
```

所有映射类型再找不到映射类型时都会调用__missing__这个方法，dict并没有定义该方法，所以如果继

承了dict，还想实现在__getitem__中找不到键的时候给一个默认值，要自己定义__missing__方法，

__missing__只会被__getitem__调用，提供__missing__方法对get和__contains__这些方法没有影响。

collections.OrderDict：这个类型在添加键的时候总会保持顺序，因此键的迭代顺序总是一致的，

OrderDict的popitem方法默认删除并返回字典里的最后一个元素，popitem里有个last参数如果last=

False，会删除并返回第一个被添加进去的元素。

collections.Chainmap()
```python
    >>> import builtins
    >>> pylookup = ChainMap(locals(), globals(), vars(builtins))
```

collections.Counter()

```python
    In [80]: from collections import Counter

    In [81]: c = Counter('qqqwwweeeqqqqq')

    In [82]: c
    Out[82]: Counter({'e': 3, 'q': 8, 'w': 3})

    In [83]: c.update('sss')

    In [84]: c
    Out[84]: Counter({'e': 3, 'q': 8, 's': 3, 'w': 3})

    In [85]: c.most_common(4)
    Out[85]: [('q', 8), ('w', 3), ('e', 3), ('s', 3)]
```
