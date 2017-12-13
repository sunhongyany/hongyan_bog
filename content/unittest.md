title: unittest.mock - mock对象库
Date: 2017-08-05 20:30
Category: python

unittest.mock 是一个用于在Python中测试的库。它允许您使用模拟对象替换测试中的系统部件，并对其使用方式进行断言。

unittest.mock 提供了一个核心 Mock 类，无需在整个测试套件中创建一个主机的存根。执行一个动作后，你可以断言使用了哪些方法/属性以及调用它们的参数。您还可以以正常方式指定返回值并设置所需的属性。

另外，mock提供了一个 patch() 装饰器，用于处理测试范围内的修补模块和类级别属性，以及用于创建唯一对象的 sentinel。有关如何使用 Mock，MagicMock 和 patch() 的一些示例，请参阅 quick guide。

Mock非常容易使用，并且设计用于 unittest。 Mock基于“action - > assertion”模式，而不是许多模拟框架使用的“record - > replay”。

对于早期版本的Python，有一个 unittest.mock 的反向端口，可以作为 模拟PyPI。


