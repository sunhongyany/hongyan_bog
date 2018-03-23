title: 生成一个或多个HTML标签
Date: 2017-06-24 20:30
Category: 学习笔记
Tags: python

```python
In [3]: def tag(name, *content, cls=None, **attrs):

   ...:     """生成一个或多个HTML标签"""

   ...:     if cls is not None:

   ...:         attrs['class'] = cls

   ...:     if attrs:

   ...:         attr_str = "".join(' %s="%s"' % (
                    attr, value) for attr, value in sorted(attrs.items()))

   ...:     else:

   ...:         attr_str = ""

   ...:     if content:

   ...:         return '\n'.join('<%s%s>%s</%s>' % (
                    name, attr_str, c, name) for c in content)

   ...:     else:

   ...:         return '<%s%s />' % (name, attr_str)

   ...:

In [4]: tag('br')

Out[4]: '<br />'


In [5]: tag('p', 'hello', 'python')

Out[5]: '<p>hello</p>\n<p>python</p>'


In [6]: print(tag('p', 'hello', 'python'))

<p>hello</p>

<p>python</p>
```

