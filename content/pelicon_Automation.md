title: Pelican自动发布网站
Date: 2017-05-19 20:30
Category: 学习笔记
Tags: Pelican

1. 使用make生成网站
    make html
2. 使用make生成站点
    make publish
3. 如果想自动侦测本地改变，使用下面的命令
    make regenerate
在你的浏览器中输入http://localhost:8000/，就可以预览。
4. 通常，你需要运行make regenenrate 和 make serve 在两个不同的终端, 但可以用一个命令实现。
    make devserver
5. 发布文章
    make rsync_upload
