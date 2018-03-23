title: 函数作用域与块作用域
Date: 2017-09-05 20:30
Category: 学习笔记
Tags: JavaScript

JS变量以函数作为作用域。

```javascript
function f() {
    function b() {
        console.log(i);
    }
    for (var i=0; i<10; i++) {
        bar();
    }
}
```
JS没有块作用域的概念，ES6引入了关键字let，可以用于生成传统的块作用域。

```javascript
if (true) {
    let b = 2;   // b是该代码块的局部变量
    console.log(b);
}
console.log(b);    // ReferenceError 
```

思考下面代码将会输出什么？

```javascript
a = 1;
var a;
console.log(a)
```

将会输出1，原因是在JS中声明会被提升，但是赋值和其他可执行的逻辑依然保留在原位置，上面的代码片段实际是这样执行的：

```javascript
var a;
a = 1;
console.log(a)
```

思考下面的代码将会输出什么？

```javascript
foo();
function foo() {
    console.log(a);
    var a = 1;
}
```

关于提升很重要的一点就是，他是以作用域为单位进行的，在函数foo中，变量声明被提到函数内部顶部，而不是整个程序的顶部，提升后的foo函数变成以下这样：

```javascript
foo();
function foo() {
    var a;
    console.log(a);
    a = 1;
}
```

所以会输出1.

函数声明和变量声明都会被提升，但是但是函数在先，变量在后。

注意：不要根据条件来使用函数声明，这种行为是非标准化的，并且在不同的浏览器中行为也不同。

下面的例子展示了这种用法：

```javascript
if (true) {
    function say() {
        return 'say1';
    }
}
else {
    function say() {
        return 'say2';
    }
}
say();
```

可以用函数表达式来代替。　

```javascript
if (true) {
    say = function() {
        return 'say1';
    }
}
else {
    say = function() {
        return 'say2';
    }
}
say();
```

