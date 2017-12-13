title: 重载运算符
Date: 2017-08-25 20:30
Category: python

python对重载运算符施加类一些限制：

1. 不能重载内置类型的运算符。

2. 不能新建运算符，只能重载现有的。

3. 某些运算符不能重载——is，and，or和not（不过位运算符&，|， ～可以）。

为了支持设计不同类型的运算，python位中缀运算符特殊方法提供了特殊的分派机制。对表达式a+b来

说，解释器会执行以下几步:

1. 如果a有__add__方法，而且返回值不是NotImplemented,调用a.__add__(b),然后返回结果。

2. 如果a没有__add__方法，或者调用__add__方法返回值不是NotImplemented，检查b有没有__radd__

方法，如果有且返回值不是NotImplemented,调用b.__radd__(a),然后返回结果。

3. 如果b没有__radd__方法，或者调用__add__方法返回值是NotImplemented,抛出TypeError，并在错

误信息中指明操作类型不支持。


