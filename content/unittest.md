title: unittest.mock - mock对象库
Date: 2017-08-05 20:30
Category: python

unittest.mock 是一个用于在Python中测试的库。它允许您使用模拟对象替换测试中的系统部件，并对其使用方式进行断言。

unittest.mock 提供了一个核心 Mock 类，无需在整个测试套件中创建一个主机的存根。执行一个动作后，你可以断言使用了哪些方法/属性以及调用它们的参数。您还可以以正常方式指定返回值并设置所需的属性。

另外，mock提供了一个 patch() 装饰器，用于处理测试范围内的修补模块和类级别属性，以及用于创建唯一对象的 sentinel。有关如何使用 Mock，MagicMock 和 patch() 的一些示例，请参阅 quick guide。

Mock非常容易使用，并且设计用于 unittest。 Mock基于“action - > assertion”模式，而不是许多模拟框架使用的“record - > replay”。

对于早期版本的Python，有一个 unittest.mock 的反向端口，可以作为 模拟PyPI。

1. Mock类

class unittest.mock.Mock(spec=None, side_effect=None, return_value=DEFAULT, wraps=None, name=None, spec_set=None, unsafe=False, **kwargs)

创建一个Mock对象，Mock对象使用几个可选参数用来指定Mock对象的行为。

- spec: 可以是一个字符串列表或者是一个已经存在的作为该mock对象的规范的对象（一个类或实例），如果设置了一个对象，会通过调用对象的dir方法，形成一个字符串列表（除了不支持的魔法方法和属性，访问不在此列表中的属性会引发AttributeError异常。

如果spec是一个对象（而不是一个字符串列表），__class__返回spec对象的类，这允许mock通过isinstance()测试。

- spec_set: 一个更严格的spec变体，如果被使用，试图设置或获得一个不是作为spec_set上的模拟的属性，会引发 AttributeError。

- side_effect：每当调用Mock时都会调用的函数，对于引发一个异常和动态改变返回值很有用，该函数和mock调用一样的的参数，除非它返回DEFAULT。这个函数的返回值被用作mock的返回值。

另外，side_effect可以是一个异常类或实例，在这种情况下，当mock被调用时，该异常会被触发。

如果side_effect是一个可迭代对象，每一次调用mock都会返回迭代对象的下一个值。

side_effect可以通过设置为None被清除。

- return_value：当mock被调用时会返回这个值，默认情况下，这是一个新的Mock，（第一次访问时创建）。

- unsafe：默认情况下，如果任意以assert或assert开头的属性将会引发AttributeError，通过设置unsafe=True会允许通过这些属性。

- wraps：要包装模拟对象的项目。如果wraps不是None，那么调用这次Mock会将调用传递给包装的对象（返回真实结果）。对模拟的属性返回一个Mock对象，该对象包装被包装对象的相应属性，（获得一个不存在的属性将会引发一个异常）。

- name：如果mock有一个name那么它将会被使用在mock的repr中，这个可能会作为调试使用，这个名字将会传播到子mock。

unittest.mock.patch(target, new=DEFAULT, spec=None, create=False, spec_set=None, autospec=None, new_callable=None, **kwargs)

patch()作为一个函数装饰器，类装饰器，或者上下文装饰器，在函数或者with声明中，target用new对象用来打补丁，当函数或with声明结束时这个补丁被取消。

如果new被省略，则用MagicMock替换这个目标，如果patch()被用作一个装饰器并且new被省略，创建的mock当作一个额外的参数给装饰的函数。如果patch()被用作一个上下文管理器中，则上下文管理器返回被创建的mock。

target应该是'package.module.ClassName'这种形式的字符串，该target会被导入，并且用一个new对象替换。所以这个target从能调用patch()的环境中导入，是在执行装饰器功能时被导入不是在装饰的时候。

如果patch创建一个MagicMock，spec和spec_set关键字参数传递给该MagicMock。

另外你可以传递spec=True或spec_set=True，这样会造成补丁作为spec/sepc_set对象传递给正在被模拟的对象。

new_callable允许你指定一个不同的类，或者可调用对象，将会被调用以创建new对象。默认使用MagicMock。

autospec是spec更有力的一种形式，如果设置autospec=True，那么将会使用要替换的对象的spec创建模拟。这次模拟的所有属性和被替换的对象的属性有相应属性的规范。被模拟的方法和函数会检查他们的参数，如果他们被错误的签名调用将会引发TypeError。对于替换类的模拟，他们的返回值将会和这个类有相同的规范。

如果
