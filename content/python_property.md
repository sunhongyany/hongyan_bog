title: property 
Date: 2018-02-08 20:30
Category: python

```python
In [28]: class Person(object):
    ...:     def __inti__(self, first_name, last_name):
    ...:         self.first_name = first_name
    ...:         self.last_name = last_name
    ...:     @property
    ...:     def full_name(self):
    ...:         return "%s %s"%(self.first_name, self.last_name)
    ...:

In [29]: person = Person('mike', 'Driscoll')
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-29-96673ca1435c> in <module>()
----> 1 person = Person('mike', 'Driscoll')

TypeError: object() takes no parameters

In [30]: class Person(object):
    ...:     def __init__(self, first_name, last_name):
    ...:         self.first_name = first_name
    ...:         self.last_name = last_name
    ...:     @property
    ...:     def full_name(self):
    ...:         return "%s %s"%(self.first_name, self.last_name)
    ...:

In [31]: person = Person('mike', 'Driscoll')

In [32]: person.full_name
Out[32]: 'mike Driscoll'

In [33]: person.first_name
Out[33]: 'mike'

In [34]: person.full_name = 'sunhongyan'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-34-d97cf07940e2> in <module>()
----> 1 person.full_name = 'sunhongyan'

AttributeError: can't set attribute

In [35]: person.first_name = "Dan"

In [36]: person.full_name
Out[36]: 'Dan Driscoll'

In [37]: 1 in {1, 2}
Out[37]: True

In [38]: from decimal import Decimal

In [39]: class Fees(object):
    ...:     def __init__(self):
    ...:         self._fee = None
    ...:     def get_fee(self):
    ...:         return self._fee
    ...:     def set_fee(self, value):
    ...:         if isinstance(value, str):
    ...:             self._fee = Decimal(value)
    ...:         elif isinstance(value, Decimal):
    ...:             self._fee = value
    ...:

In [40]: class Fees(object):
    ...:     def __init__(self):
    ...:         self._fee = None
    ...:     def get_fee(self):
    ...:         return self._fee
    ...:     def set_fee(self, value):
    ...:         if isinstance(value, str):
    ...:             self._fee = Decimal(value)
    ...:         elif isinstance(value, Decimal):
    ...:             self._fee = value
    ...:     fee = property(get_fee, set_fee)
    ...:

In [41]: f = Fees()

In [42]: f.set_fee('2')

In [43]: f.fee
Out[43]: Decimal('2')

In [44]: f.fee = '1'

In [45]: f.get_fee()
Out[45]: Decimal('1')

In [46]: from decimal import Decimal

In [47]: class Fees(object):
    ...:     def __init__(self):
    ...:         self._fee = None
    ...:     @property
    ...:     def fee(self):
    ...:         return self._fee
    ...:     @fee.setter
    ...:     def fee(self, value):
    ...:         if isinstance(value, str):
    ...:             self._fee = Decimal(value)
    ...:         elif isinstance(value, Decimal):
    ...:             self._fee = value
    ...:

In [48]: f = Fees()

In [49]: f.fee = 1

In [50]: f.fee

In [51]: f.fee = '2'

In [52]: f.fee
Out[52]: Decimal('2')
```
