title: js闭包
Date: 2017-09-05 20:30
Category: JS

```javascript
var outer = "outer";
var copy;
function OuterFn() {
	var inner = "inner";
	function InnerFn(){
		console.log(inner);
		console.log(outer);
	}
	copy = InnerFn;
}
OuterFn();
copy();
```

```javascript
var outer = "outer";
var copy;
function OuterFn(p) {
	var inner = "inner";
	function InnerFn(){
		console.log(inner);
		console.log(outer);
		console.log(p);
		console.log(magic);
	}
	copy = InnerFn;
}
console.log(magic);
var magic = "magic";
OuterFn();
copy();
```

循环与闭包

```javascript
for(var i=1; i<=5; i++){
	setTimeout(function delay(){
		console.log(i);
	}, i*1000);
}
```

```javascript
for(var i=1; i<=5; i++){
	(function (i){
		setTimeout(function delay(){
			console.log(i);
		}, i*1000);})(i);
}
```
