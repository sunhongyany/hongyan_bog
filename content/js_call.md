title: js中各种调用方式
Date: 2017-09-07 20:30
Category: JavaScript

1. 作为函数调用

如果函数不是以方法，构造函数或通过apply(),call()调用，那么它只能作为一个函数被调用：

```javascript
function add() {}
add();
var sub = function() {
};
sub();
```

当以这种模式调用时，this被绑定在全局对象上。

2. 作为方法被调用

方法是作为对象属性的函数。对于方法来说，this被绑定在方法被调用时所在的对象上。

```javascript
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>title</title>
<script>
function testF() { return this; }
console.log(testF());
var testFCopy = testF;
console.log(testFCopy());
var testObj = {
	testObjFunc: testF
};
console.log(testObj.testObjFunc());
</script>
</head>
<body>
</body>
</html>
```

![Alt Text]({filename}/images/call.png)

前两次调用都是函数调用，因此this指向的是全局上下文，最后是方法调用，this看到的是函数上下文。

3. 作为构造函数被调用

this会被绑定到新建的对象上。

```javascript
var Person = function (name) {
	this.name = name;
}
Person.prototype.greet = function () {
	return this.name;
}
var albert = new Person('Albert');
console.log(albert.greet());
```

4. 通过apply()和call()方法调用
