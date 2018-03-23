title: 实例属性和原型属性
Date: 2017-09-09 19:30
Category: 学习笔记 
Tags: JavaScript 

利用函数作用域来实现类的效果。

1. 可以在函数中使用关键字var声明私有变量，它们可以由私有函数和特权方法访问。
2. 可以在对象的构造函数中声明私有函数，并由特权方法调用。
3. 特权方法可以使用this.method = function(){}.
4. 公共方法可以使用Class.prototype.method = function(){}来声明。
5. 公共属性可以使用this.prototype来声明，能够对外部访问。

```javascript
function Player(name, sport, age, country){
	this.constructor.noOfPlayers++;
	// 私有属性和函数，只能由特权对象浏览，编辑或调用。
	var retirementAge = 40;
	var available = true;
	var playerAge = age? age: 18;
	var PlayerSport = sport? sport: "Un";
	function isAvailable(){
		return available && (playerAge < retirementAge);
	};
	var playerName = name ? name: "Unknown";
	// 特权方法，可以从外部调用，也可以由成员访问，可以替换成对应的公共方法。
	this.book = function(){
		if (!isAvailable()){
			this.available = false;
		}else{
			console.log("Player is unavailable");
		}
	};
	this.getSport = function(){
		return playerSport;
	};
	// 公共属性可以在任何地方对其作出修改。
	this.batPreference = "Lefty";
	this.hasCelebGirlfriend = false;
	this.endorses = "super brand";
}
// 公共方法-任何人都可以读取或写入。只能访问公共属性和原型方法。
Player.prototype.switchHands = function(){
	this.batPreference = "righty";
};
Player.prototype.dateCeleb = function(){
	this.wearGlasses = false;
};
Player.prototype.fixEyes = function(){
	this.wearsGlasses = false;
};
// 原型属性-任何人都可以读取或写入（或覆盖）；
Player.prototype.wearsGlasses = true;
// 静态属性-任何人都可以读取或写入
Player.noOfPlayers = 0;
(function PlayerTest(){
	// 创建Player对象的新实例；
	console.log("a");
	var cricketer = new Player("V", "Cricket", 23, "E");
	var golfer = new Player("pete", "Golf", 32, "U");
	console.log(Player.noOfPlayers);
	// 两个函数共享公共的Player.prototype.wearsGlasses；
	cricketer.fixEyes();
	golfer.fixEyes();
	cricketer.endorses = "Other";
	// 通过Player的原型来改变其公共方法
	Player.prototype.fixEyes = function(){
		this.wearGlasses = true;
	};
	// 只改变了Cricketer的函数
	cricketer.switchHands = function(){
		this.batPreference = "undecided";
	};
	golfer.book();
})();
```


