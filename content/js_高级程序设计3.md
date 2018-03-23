title: JavaScript 数据类型
Date: 2017-09-11 11:30
Category: 学习笔记
tags: JavaScript

ECMAScript中有5种简单数据类型（也称为基本数据类型）：Undefined、Null、Boolean、Number和String。还有1种复杂数据类型——Object，Object本质上是由一组无序的名值对组成的。ECMAScript不支持任何创建自定义类型的机制，而所有值最终都将是上述6种数据类型之一。

1. typeof操作符
鉴于ECMAScript是松散类型的，因此需要有一种手段来检测给定变量的数据类型——typeof就是负责提供这方面信息的操作符。对一个值使用typeof操作符可能返回下列某个字符串：
    "undefined"——如果这个值未定义；
    "boolean"——如果这个值是布尔值；
    "string"——如果这个值是字符串；
    "number"——如果这个值是数值；
    "object"——如果这个值是对象或null；
    "function"——如果这个值是函数。

 typeof操作符的操作数可以是变量（message），也可以是数值字面量。
 注意，typeof是一个操作符而不是函数，因此例子中的圆括号尽管可以使用，但不是必需的。有些时候，typeof操作符会返回一些令人迷惑但技术上却正确的值。比如，调用typeof null会返回"object"，因为特殊值null被认为是一个空的对象引用。Safari 5及之前版本、Chrome 7及之前版本在对正则表达式调用typeof操作符时会返回"function"，而其他浏览器在这种情况下会返回"object"。从技术角度讲，函数在ECMAScript中是对象，不是一种数据类型。然而，函数也确实有一些特殊的属性，因此通过typeof操作符来区分函数和其他对象是有必要的。

String()函数遵循下列转换规则：
1. 如果值有toString()方法，则调用该方法（没有参数）并返回相应的结果；
2. 如果值是null，则返回"null"；
3. 如果值是undefined，则返回"undefined"。
