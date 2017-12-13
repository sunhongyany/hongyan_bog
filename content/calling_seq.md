title: 接口与调用顺序
Date: 2017-08-27 20:30
Category: Tornado

1. initialize()

对应每个请求的处理类Handler在构造一个实例后首先执行initialize()方法。路由映射中的第三个字典型参数会作为该方法的命名参数传递，如：

```python
class ProfileHandler(RequestHandler):
    def initialize(self, database):
        self.database = database

    def get(self):
        ...

app = Application([
    (r'/user/(.*)', ProfileHandler, dict(database=database)),
    ])
```

2. prepare()

预处理，即在执行对应请求方式的HTTP方法（如get、post等）前先执行，注意：不论以何种HTTP方式请求，都会执行prepare()方法。

3. HTTP方法

    get	     请求指定的页面信息，并返回实体主体。

    head	 类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头

    post	 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。
    
    POST请求可能会导致新的资源的建立和/或已有资源的修改。

    delete	 请求服务器删除指定的内容。

    patch	 请求修改局部数据。

    put	     从客户端向服务器传送的数据取代指定的文档的内容。

    options  返回给定URL支持的所有HTTP方法。

4. on_finish()

在请求处理结束后调用，即在调用HTTP方法后调用。通常该方法用来进行资源清理释放或处理日志等。注意：请尽量不要在此方法中进行响应输出。

5. set_default_headers()

6. write_error()

7. 调用顺序

在正常情况未抛出错误时，调用顺序为：

    set_defautl_headers()
    initialize()
    prepare()
    HTTP方法
    on_finish()

在有错误抛出时，调用顺序为：

    set_default_headers()
    initialize()
    prepare()
    HTTP方法
    set_default_headers()
    write_error()
    on_finish()
