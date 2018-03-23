title: 初试tornado
Date: 2017-08-24 20:30
Category: 学习笔记
Tags: Tornado

新建文件hello.py，代码如下：

```python
#!/usr/bin/env python
# coding:utf-8

import tornado.web
import tornado.ioloop

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Itcast!")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
```

执行如下命令，开启tornado：

```python
$ python hello.py
```

打开浏览器，输入网址127.0.0.1:8000（或localhost:8000），查看效果：

![Alt Text]({filename}/images/hello.png)

代码讲解

1. tornado.web

tornado的基础web框架模块

RequestHandler

封装了对应一个请求的所有信息和方法，write(响应信息)就是写响应信息的一个方法；对应每一种http请

求方式（get、post等），把对应的处理逻辑写进同名的成员方法中（如对应get请求方式，就将对应的

处理逻辑写在get()方法中），当没有对应请求方式的成员方法时，会返回“405: Method Not Allowed”错

误。

2. tornado.ioloop

tornado的核心io循环模块，封装了Linux的epoll和BSD的kqueue，tornado高性能的基石。

IOLoop.current()

返回当前线程的IOLoop实例。

IOLoop.start()

启动IOLoop实例的I/O循环,同时服务器监听被打开。

在hello.py中app.listen(8000)，创建了一个http服务器示例并绑定到给定端口，我们能不能自己动手来实

现这一部分功能呢？

我们来修改上一实例的代码：

```python
#!/usr/bin/env python
# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver # 新引入httpserver模块

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Itcast!")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    # ------------------------------
    # 我们修改这个部分
    # app.listen(8000)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8000)
    # ------------------------------
    tornado.ioloop.IOLoop.current().start()
```

在这一修改版本中，我们引入了tornado.httpserver模块，顾名思义，它就是tornado的HTTP服务器实

现。

我们创建了一个HTTP服务器实例http_server，因为服务器要服务于我们刚刚建立的web应用，将接收到

的客户端请求通过web应用中的路由映射表引导到对应的handler中，所以在构建http_server对象的时候

需要传入web应用对象app。http_server.listen(8000)将服务器绑定到8000端口。

实际上一版代码中app.listen(8000)正是对这一过程的简写。

我们刚刚实现的都是单进程,我们也可以一次启动多个进程，修改上面的代码如下：

```python
#!/usr/bin/env python
# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver 

class IndexHandler(tornado.web.RequestHandler):
    """主路由处理类"""
    def get(self):
        """对应http的get请求方式"""
        self.write("Hello Itcast!")

if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app) 
    # -----------修改----------------
    http_server.bind(8000)
    http_server.start(0)
    # ------------------------------
    tornado.ioloop.IOLoop.current().start()
```

http_server.bind(port)方法是将服务器绑定到指定端口。

http_server.start(num_processes=1)方法指定开启几个进程，参数num_processes默认值为1，即默认

仅开启一个进程；如果num_processes为None或者<=0，则自动根据机器硬件的cpu核芯数创建同等数

目的子进程；如果num_processes>0，则创建num_processes个子进程。

2.关于多进程

虽然tornado给我们提供了一次开启多个进程的方法，但是由于：

每个子进程都会从父进程中复制一份IOLoop实例，如过在创建子进程前我们的代码动了IOLoop实例，

那么会影响到每一个子进程，势必会干扰到子进程IOLoop的工作；

所有进程是由一个命令一次开启的，也就无法做到在不停服务的情况下更新代码；

所有进程共享同一个端口，想要分别单独监控每一个进程就很困难。

不建议使用这种多进程的方式，而是手动开启多个进程，并且绑定不同的端口。
