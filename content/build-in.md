Title: python中的内置序列（一） 
Date: 2017-06-03 20:20
Category: python

python的序列按存放的数据类型是否相同，可分为：

容器序列：

* tuple，list，collections.queue这些序列可以存放的不同数据类型。

扁平序列：

* str，bytes，bytearry，memoryview和array.array这些序列只能容纳一种类型。

容器序列存放的是它们所包含的任意类型对象的引用，而扁平序列存放的是值不是引用。扁平序列是一

段连续的内存空间，扁平序列更加紧凑，但他只能存放诸如字符，数值和字节这种基础类型。

还可按照能否被修改来分类：

可变序列：

* list，bytearray，array.array，collections.queue和memoryview。

不可变序列：

* tuple，str和bytes。
