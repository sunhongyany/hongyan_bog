title: arguments参数
Date: 2017-09-06 20:30
Category: 学习笔记
Tags: JavaScript

arguments参数是传递给函数的所有参数的集合。这个集合有个名为length的属性，它包含了参数的个数。

```javascript
var sum = function () {
    var i, total = 0;
    for (i = 0, i < arguments.length; i += 1) {
        total += arguments[i];
    }
    return total;
}
console.log(sum(1, 2, 3, 4));    // 打印出10
```

arguments类似数组，可以用下面的方法将其转化成数组：

```javascript
var args = Array.prototype.slice.call(arguments);
```

