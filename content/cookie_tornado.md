title: cookie
Date: 2017-08-27 20:30
Category: 学习笔记
Tags: Tornado

设置

set_cookie(name, value, domain=None, expires=None, path='/', expires_days=None)

参数说明：

参数名	            说明

name	        cookie名

value	        cookie值

domain	        提交cookie时匹配的域名

path	        提交cookie时匹配的路径

expires	        cookie的有效期，可以是时间戳整数、时间元组或者datetime类型，为UTC时间

expires_days	cookie的有效期，天数，优先级低于expires

获取

get_cookie(name, default=None)

获取名为name的cookie，可以设置默认值。

清除

clear_cookie(name, path='/', domain=None)

删除名为name，并同时匹配domain和path的cookie。

clear_all_cookies(path='/', domain=None)

删除同时匹配domain和path的所有cookie。

注意：执行清除cookie操作后，并不是立即删除了浏览器中的cookie，而是给cookie值置空，并改变其有效期使其失效。真正的删除cookie是由浏览器去清理的。

安全Cookie

Cookie是存储在客户端浏览器中的，很容易被篡改。Tornado提供了一种对Cookie进行简易加密签名的方法来防止Cookie被恶意篡改。

使用安全Cookie需要为应用配置一个用来给Cookie进行混淆的秘钥cookie_secret，将其传递给Application的构造函数。我们可以使用如下方法来生成一个随机字符串作为cookie_secret的值。

获取和设置

set_secure_cookie(name, value, expires_days=30)

设置一个带签名和时间戳的cookie，防止cookie被伪造。

get_secure_cookie(name, value=None, max_age_days=31)

如果cookie存在且验证通过，返回cookie的值，否则返回None。max_age_day不同于expires_days，expires_days是设置浏览器中cookie的有效期，而max_age_day是过滤安全cookie的时间戳。
