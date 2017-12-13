title: memoryview
Date: 2017-07-25 20:30
Category: python

memoryview是一个内置类，她能让用户在不复制内容的情况下操作同一个数组的不同切片。

memoryview.cast能以不同的方式读写同一块内存数据而且内容字节不会随意移动。

```python
In [7]: import array

In [8]: numbers = array.array('h', [1, 2, 0, -1, -2])

In [11]: numbers_m = memoryview(numbers)

In [12]: numbers_m
Out[12]: <memory at 0x10709ad08>

In [13]: len(numbers_m)
Out[13]: 5

In [15]: numbers_c = numbers_m.cast('b')

In [16]: numbers_c.tolist()
Out[16]: [1, 0, 2, 0, 0, 0, -1, -1, -2, -1]

In [17]: numbers_c[5] = 2

In [18]: numbers
Out[18]: array('h', [1, 2, 512, -1, -2])
```


