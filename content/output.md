title: Output
Date: 2017-08-26 20:30
Category: 学习笔记
Tags: tornado

1. write(chunk)

将chunk数据写到输出缓冲区。如我们在之前的示例代码中写的：

```python
class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello python!")
```

想一想，可不可以在同一个处理方法中多次使用write方法？

下面的代码会出现什么效果？

```python
class IndexHandler(RequestHandler):
    def get(self):
        self.write("hello python 1!")
        self.write("hello python 2!")
        self.write("hello python 3!")
```

write方法是写到缓冲区的，我们可以像写文件一样多次使用write方法不断追加响应内容，最终所有写到缓冲区的内容一起作为本次请求的响应输出。

想一想，如何利用write方法写json数据？

```python
import json

class IndexHandler(RequestHandler):
    def get(self):
        stu = {
            "name":"zhangsan",
            "age":24,
            "gender":1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)
```

实际上，我们可以不用自己手动去做json序列化，当write方法检测到我们传入的chunk参数是字典类型后，会自动帮我们转换为json字符串。

```python
class IndexHandler(RequestHandler):
    def get(self):
        stu = {
            "name":"zhangsan",
            "age":24,
            "gender":1,
        }
        self.write(stu)
```

两种方式有什么差异？

对比一下两种方式的响应头header中Content-Type字段，自己手动序列化时为Content-Type:text/html; charset=UTF-8，而采用write方法时为Content-Type:application/json; charset=UTF-8。

write方法除了帮我们将字典转换为json字符串之外，还帮我们将Content-Type设置为application/json; charset=UTF-8。

2. set_header(name, value)

利用set_header(name, value)方法，可以手动设置一个名为name、值为value的响应头header字段。

用set_header方法来完成上面write所做的工作。

```python
import json

class IndexHandler(RequestHandler):
    def get(self):
        stu = {
            "name":"zhangsan",
            "age":24,
            "gender":1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.set_header("Content-Type", "application/json; charset=UTF-8")
```

3. set_default_headers()

该方法会在进入HTTP处理方法前先被调用，可以重写此方法来预先设置默认的headers。注意：在HTTP处理方法中使用set_header()方法会覆盖掉在set_default_headers()方法中设置的同名header。

```python
class IndexHandler(RequestHandler):
    def set_default_headers(self):
        print("执行了set_default_headers()")
        # 设置get与post方式的默认响应体格式为json
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        # 设置一个名为python、值为python的header
        self.set_header("python", "python")

    def get(self):
        print("执行了get()")
        stu = {
            "name":"zhangsan",
            "age":24,
            "gender":1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)
        self.set_header("python", "i love python") # 注意此处重写了header中的python字段

    def post(self):
        print("执行了post()")
        stu = {
            "name":"zhangsan",
            "age":24,
            "gender":1,
        }
        stu_json = json.dumps(stu)
        self.write(stu_json)
```

4. set_status(status_code, reason=None)

为响应设置状态码。

参数说明：

status_code int类型，状态码，若reason为None，则状态码必须为下表中的。

reason string类型，描述状态码的词组，若为None，则会被自动填充为下表中的内容。

5. redirect(url)

告知浏览器跳转到url。

```python
class IndexHandler(RequestHandler):
    """对应/"""
    def get(self):
        self.write("主页")

class LoginHandler(RequestHandler):
    """对应/login"""
    def get(self):
        self.write('<form method="post"><input type="submit" value="登陆"></form>')

    def post(self):
        self.redirect("/")
```

6. send_error(status_code=500, **kwargs)

抛出HTTP错误状态码status_code，默认为500，kwargs为可变命名参数。使用send_error抛出错误后tornado会调用write_error()方法进行处理，并返回给浏览器处理后的错误页面。

```python
class IndexHandler(RequestHandler):
    def get(self):
        self.write("主页")
        self.send_error(404, content="出现404错误")
```

注意：默认的write\_error()方法不会处理send\_error抛出的kwargs参数，即上面的代码中content="出现404错误"是没有意义的。
使用send_error()方法后就不要再向输出缓冲区写内容了！

7. write_error(status_code, **kwargs)

用来处理send_error抛出的错误信息并返回给浏览器错误信息页面。可以重写此方法来定制自己的错误显示页面。

```python
class IndexHandler(RequestHandler):
    def get(self):
        err_code = self.get_argument("code", None) # 注意返回的是unicode字符串，下同
        err_title = self.get_argument("title", "")
        err_content = self.get_argument("content", "")
        if err_code:
            self.send_error(err_code, title=err_title, content=err_content)
        else:
            self.write("主页")

    def write_error(self, status_code, **kwargs):
        self.write(u"<h1>出错了，程序员GG正在赶过来！</h1>")
        self.write(u"<p>错误名：%s</p>" % kwargs["title"])
        self.write(u"<p>错误详情：%s</p>" % kwargs["content"])
```

