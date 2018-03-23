title: JavaScript 语句
Date: 2017-09-12 21:30
Category: 学习笔记
tags: JavaScript

1. label语句使用

label语句可以在代码中添加标签，以便将来使用。以下是label语句的语法：label: statement 下面是一个示例：start: for (var i=0; i < count; i++) {     alert(i);  } 这个例子中定义的start标签可以在将来由break或continue语句引用。加标签的语句一般都要与for语句等循环语句配合使用。

2. switch语句

使用表达式作为case值可以实现下列操作：
```JavaScript
var num = 25;
switch (true) {
    case num < 0:
        alert("Less than 0.");
        break;
    case num >= 0 && num <= 10:
    alert("Between 0 and 10.");
    break;
    case num > 10 && num <= 20:
    alert("Between 10 and 20.");
    break;
    default:
    alert("More than 20.");
}
```
这个例子首先在switch语句外面声明了变量num。而之所以给switch语句传递表达式true，是因为每个case值都可以返回一个布尔值。这样，每个case按照顺序被求值，直到找到匹配的值或者遇到default语句为止（这正是这个例子的最终结果）。switch语句在比较值时使用的是全等操作符，因此不会发生类型转换（例如，字符串"10"不等于数值10）。
