Title: python中 __repr__和__str__ 
Date: 2017-06-05 20:20
Category: 学习笔记
Tags: python

python对象的一个基本要求就是它得有个合理的字符串表示形式，我们可以通过__repr__ 和__str__来满

足这个要求，前者方便调试和记录日志，后者是给终端用户看的。

例如，我们构造一个Person类：

    class Person(object):

        def __init__(self, name, gender):

            self.name = name

            self.gender = gender

        def __str__(self):

            return '(Person: %s, %s)' % (self.name, self.gender)

当在终端输入：

    >>> p = Person("a", "women")

    >>> print(p)

    (Person: a, women)

    >>> p

    <__main__.Person object at 0x1055b4b70>

可以看出，当直接输入p时，并没有调用__str__方法。

<__main__.Person object at 0x1055b4b70> 的意思是变量p指向类Person的object，后面的0x1055b4b70

是内存地址，每个object的内存地址都不一样，而Person本身是个类。

接下来我们在Person里定义__repr__方法：

    class Person(object):

        def __init__(self, name, gender):

            self.name = name

            self.gender = gender

        def __repr__(self):

            return '(Person: %s, %s)' % (self.name, self.gender)

当在终端输入：

    >>> p = Person("a", "women")

    >>> print(p)

    (Person: a, women)

    >>> p

    (Person: a, women)

