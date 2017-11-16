Title: datetime
Date: 2017-06-24 21:30
Category: python

&emsp;&emsp;datetime是Python处理日期和时间的标准库。

获取当前日期和时间

我们先看如何获取当前日期和时间：

```python
    In [10]: from datetime import datetime

    In [11]: now = datetime.now()

    In [12]: now
    Out[12]: datetime.datetime(2017, 10, 24, 22, 51, 27, 806565)

    In [13]: print(type(now))
    <class 'datetime.datetime'>
```

&emsp;&emsp;注意到datetime是模块，datetime模块还包含一个datetime类，通过from datetime import datetime

导入的才是datetime这个类。

&emsp;&emsp;如果仅导入import datetime，则必须引用全名datetime.datetime。

&emsp;&emsp;datetime.now()返回当前日期和时间，其类型是datetime

str转换为datetime

&emsp;&emsp;很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。

转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：

```python
    In [15]: from datetime import datetime

    In [16]: s = '2017-05-02 09:10:20'

    In [17]: d = datetime.strptime(s, '%Y-%m-%d %H:%M:%S')

    In [18]: print(d)
    2017-05-02 09:10:20
```

datetime转换为str

&emsp;&emsp;如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通

过strftime()实现的，同样需要一个日期和时间的格式化字符串：

```python
    In [20]:  print(d.strftime('%a, %b %d %H:%M'))
    Fri, Jan 02 09:10
```

datetime加减

&emsp;&emsp;对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用

+和-运算符，不过需要导入timedelta这个类：

```python
    In [21]: from datetime import timedelta

    In [22]: d + timedelta(hours=10)
    Out[22]: datetime.datetime(2015, 1, 2, 19, 10, 20)

    In [23]: d - timedelta(hours=10)
    Out[23]: datetime.datetime(2015, 1, 1, 23, 10, 20)

    In [24]: d + timedelta(days=2, hours=12)
    Out[24]: datetime.datetime(2015, 1, 4, 21, 10, 20)
```

