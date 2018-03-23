title: python的私有属性和受保护的属性
Date: 2017-07-25 20:30
Category: 学习笔记
Tags: python

编写一个dog类，这个类的内部用到了mood实例属性，但没有将其开放，现在如果创建一个dog子类

beagle，里面也定义mood实例属性，就会将父类的实例属性mood覆盖。为了避免这种情况，如果以

__mood的形式命名实例属性，python会把属性名存入实例的__dict__中而且会在前面加一个下划线和

类名，因此对dog类来说， __mood会变成_dog__mood;对beagle来说就会变成_beagle__mood，这个语

言特性叫做改写。

在模块中，顶层名称使用一个前导下划线，对from 模块名 import *来说，不会导入，但可以用from 模块

名 import 私有属性 导入

