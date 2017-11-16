title: itemgetter与attrgetter
Date: 2017-06-24 20:30
Category: python

itemgetter的常见用途：根据元祖的某个字段给元祖列表排序。

'''python
    In [1]: from operator import itemgetter

    In [2]: args = [(2, 'b', '123'), (1, "a", "123"), (3, "c", "345")]

    In [3]: for i in sorted(args, key=itemgetter(1)):

    ...:     print(i)

    ...:

    (1, 'a', '123')

    (2, 'b', '123')

    (3, 'c', '345')
'''

如果把多个参数传给itemgetter，他构建的函数会返回提取的值构成元祖。

'''python
    In [86]: d = itemgetter(1, 2)

    In [87]: for i in args:

        ...:     print(d(i))

        ...:

    ('b', '123')

    ('a', '123')

    ('c', '345')
'''

attrgetter的属性与itemgetter的属性类似，它创建的函数根据根据名称提取对象的属

性，如果把多个属性名传给attrgetter, 他也会返回提取的值构成元祖。

