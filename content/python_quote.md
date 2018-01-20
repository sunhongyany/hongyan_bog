title: urllib中的quote函数
Date: 2017-09-19 19:30
Category: python

urllib.parse.quote(text)

按照标准， URL 只允许一部分 ASCII 字符（数字字母和部分符号），其他的字符（如汉字）是不符合 URL 标准的。所以 URL 中使用其他字符就需要进行 URL 编码。URL 中传参数的部分（query String），格式是：name1=value1&name2=value2&name3=value3 

假如你的 name 或者 value 值中有『&』或者『=』等符号，就当然会有问题。所以URL中的参数字符串也需要把『&=』等符号进行编码。URL编码的方式是把需要编码的字符转化为 %xx 的形式。通常 URL 编码是基于 UTF-8 的（当然这和浏览器平台有关）。

```python 
>>> from urllib import parse
>>> query = {
  'name': 'walker',
  'age': 99,
  }
>>> parse.urlencode(query)
'name=walker&age=99'
```

