title: 闭包
Date: 2017-06-24 20:30
Category: 学习笔记
Tags: python

闭包指延伸了作用域的函数，其中包含函数体中的引用，但是不在定义体中定义的非全局变量。

通过以下例子理解一下。

我们定义一个不断增加系列值的均值。就像下面这样。

```python
>>> avg(10)
10.0

>>> avg(11)
10.5

>>> avg(12)
11.0

```

可以按如下方式实现：

```python

In [15]: class Averager():
    ...:     def __init__(self):
    ...:         self.series = []
    ...:     def __call__(self, num):
    ...:         self.series.append(num)
    ...:         total = sum(self.series)
    ...:         return total/len(self.series)
    ...:

In [17]: avg = Averager()

In [18]: avg(20)
Out[18]: 20.0

In [19]: avg(10)
Out[19]: 15.0

In [20]: avg(12)
Out[20]: 14.0

In [21]: avg(22)
Out[21]: 16.0

```

我们也可以定义一个高阶函数。

```python

In [22]: def make_averager():
    ...:     series = []
    ...:     def averager(new_value):
    ...:         series.append(new_value)
    ...:         total = sum(series)
    ...:         return total/len(series)
    ...:     return averager
    ...:

In [23]: ave = make_averager()

In [24]: ave(10)
Out[24]: 10.0

In [25]: ave(11)
Out[25]: 10.5

In [26]: ave(12)
Out[26]: 11.0

```

在上面的例子中，series是make_averager函数的局部变量，因为那个函数的定义体中初始化了series，

可是调用啊 ave(10)时，make_averager已经返回，而他的本地作用域也一并一去不复返了。

在averager中series是个自由变量（指未在本地作用域中绑定的变量）。

综上，闭包是一种函数，他会保留定义函数时存在自由变量的绑定，这样调用函数时虽然定义域不可用

了，但是仍能使用那些绑定。

上面的make_averager()效率太低，应该是只存储目前的总值和元素个数，使用这两个值计算平均值。

下面定义一个函数来实现

```python
In [28]: def make_averager():
    ...:     total = 0
    ...:     total = 0
    ...:     def averager(new_value):
    ...:         total += new_value
    ...:         total += 1
    ...:         return total/total
    ...:     return averager
    ...:
```

看着似乎没什么问题，但调用时确保错。

```python
In [29]: ave = make_averager()

In [30]: ave(10)

---------------------------------------------------------------------------

UnboundLocalError                         Traceback (most recent call last)

<ipython-input-30-6b9bb62587bf> in <module>()

----> 1 ave(10)
      3     total = 0
      4     def averager(new_value):
----> 5         total += new_value
      6         total += 1
      7         return total/total

UnboundLocalError: local variable 'total' referenced before assignment
```

问题是total是数字或任何不可变类型时，total += 1 的作用与total = total + 1，averager里为total赋值

了。total就成为了局部变量。

最开始定义的make_averager没有遇到这个问题是因为没有给series赋值，而是调用了series，并把传给sum和

len()。也就是利用了列表是可变的对象。

但对不可变类型，例如total += 1，会隐式创建局部变量，这样total就不是自由变量了，就不会保存在闭

包中，为了解决这个问题python3引入了nonlocal声明，它的作用是把变量标记为自由变量。

```python
In [31]: def make_averager():
    ...:     count = 0
    ...:     total = 0
    ...:     def averager(new_value):
    ...:         nonlocal count, total
    ...:         total += new_value
    ...:         count += 1
    ...:         return total/count
    ...:     return averager
    ...:
In [32]: ave = make_averager()

In [33]: ave(10)
Out[33]: 10.0

In [34]: ave(12)
Out[34]: 11.0
```


