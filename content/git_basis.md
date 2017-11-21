title: git基础
Date: 2017-06-25 20:30
Category: git

### 获取git仓库

有两种取得git仓库的方法：

1. 在现有目录中初始化仓库  git init

2. 克隆现有的仓库  git clone [url]

### 检查当前文件的状态

git status

### 跟踪新文件

git add <new_file>

### 暂存已修改的文件

git add <modified_file>

git add 是个多功能命令，可以用它开始跟踪新文件，或者把已跟踪的文件放在暂存区，还能用于合并时

把有冲突的文件标记为已解决状态。

### 忽略文件
一般我们总会有些文件无需纳入 Git 的管理，也不希望它们总出现在未跟踪文件列表。通常都是些自动

生成的文 件，比如日志文件，或者编译过程中创建的临时文件等。在这种情况下，我们可以创建一个名

为 .gitignore 的文件，列出要忽略的文件模式。

文件 .gitignore 的格式规范如下:

• 所有空行或者以 # 开头的行都会被 Git 忽略。 

• 可以使用标准的 glob 模式匹配。

• 匹配模式可以以(/)开头防止递归。

• 匹配模式可以以(/)结尾指定目录。

• 要忽略指定模式以外的文件或目录，可以在模式前加上惊叹号(!)取反。

所谓的 glob 模式是指 shell 所使用的简化了的正则表达式。

### 查看已暂存和未暂存的修改

git diff

此命令比较的是工作目录中当前文件和暂存区域快照之间的差异，也就是修改之后还没有暂存起来的变

化内容。

若要查看已暂存的将要添加到下次提交里的内容，可以用 git diff --cached 命令。

### 提交更新

git commit

另外，你也可以在 commit 命令后添加 -m 选项，将提交信息与命令放在同一行。

git commit -m'提交信息'

### 移除文件

要从 Git 中移除某个文件，就必须要从已跟踪文件清单中移除(确切地说，是从暂存区域移除)，然后

提交。可 以用git rm命令完成此项工作，并连带从工作目录中删除指定的文件，这样以后就不会出现

在未跟踪文件清单中了。

下一次提交时，该文件就不再纳入版本管理了。如果删除之前修改过并且已经放到暂存区域的话，则必

须要用强 制删除选项 -f(译注:即 force 的首字母)。这是一种安全特性，用于防止误删还没有添加到

快照的数据，这 样的数据不能被 Git 恢复。

另外一种情况是，我们想把文件从 Git 仓库中删除(亦即从暂存区域移除)，但仍然希望保留在当前工作

目录中。换句话说，你想让文件保留在磁盘，但是并不想让 Git 继续跟踪。当你忘记添加 .gitignore 文

件，不小心把一个很大的日志文件或一堆 .a 这样的编译生成文件添加到暂存区时，这一做法尤其有用。

为达到这一目 的，使用 --cached 选项:

git rm --cached <file>

### 移动文件

git mv file_from file_to

### 查看提交历史

git log

默认不用任何参数的话，git log会按提交时间列出所有的更新，最近的更新排在最上面。

### 撤消操作

git commit --amend

### 查看远程仓库

git remote

你也可以指定选项 -v，会显示需要读写远程仓库使用的 Git 保存的简写与其对应的 URL。

### 添加远程仓库

git remote add <shortname> <url>

### 从远程仓库中抓取与拉取

git fetch [remote-name]

### 推送到远程仓库

git push [remote-name] [branch- name]

### 查看远程仓库

git remote show [remote-name]

### 远程仓库的移除与重命名

如果想要重命名引用的名字可以运行git remote rename去修改一个远程仓库的简写名。例如，想要将pb

重命名为paul，可以用git remote rename这样做:

  $ git remote rename pb paul

  $ git remote

  origin

  paul

值得注意的是这同样也会修改你的远程分支名字。那些过去引用 pb/master 的现在会引用 paul/master。

移除远程仓库

git remote rm 仓库名

### 列出标签

git tag

### 创建标签

Git 使用两种主要类型的标签:轻量标签(lightweight)与附注标签(annotated)。

一个轻量标签很像一个不会改变的分支 - 它只是一个特定提交的引用。

然而，附注标签是存储在 Git 数据库中的一个完整对象。它们是可以被校验的;其中包含打标签者的名

字、电子邮件地址、日期时间;还有一个标签信息;并且可以使用 GNU Privacy Guard (GPG)签名与验

证。通常建议创建附注标签，这样你可以拥有以上所有信息;但是如果你只是想用一个临时的 标签，或

者因为某些原因不想要保存那些信息，轻量标签也是可用的。

附注标签

在 Git 中创建一个附注标签是很简单的。最简单的方式是当你在运行 tag 命令时指定 -a 选项:

  $ git tag -a v1.4 -m 'my version 1.4'

  $ git tag

  v0.1

  v1.3

  v1.4

-m 选项指定了一条将会存储在标签中的信息。如果没有为附注标签指定一条信息，Git 会运行编辑器要

求你输入信息。

通过使用git show命令可以看到标签信息与对应的提交信息.

轻量标签

另一种给提交打标签的方式是使用轻量标签。轻量标签本质上是将提交校验和存储到一个文件中 - 没有

保存任何 其他信息。创建轻量标签，不需要使用 -a、-s 或 -m 选项，只需要提供标签名字:

$ git tag v1.4-lw

$ git tag

  v0.1

  v1.3

  v1.4

  v1.4-lw
 
后期打标签 

你也可以对过去的提交打标签。假设提交历史是这样的:

  $ git log --pretty=oneline

  4682c3261057305bdd616e23b64b0857d832627b added a todo file

  166ae0c4d3f420721acbb115cc33848dfcc2121a started write support

  9fceb02d0ae598e95dc970b74767f19372d61af8 updated rakefile

  964f16d36dfccde844893cac5b347e7b3d44abbc commit the todo

  8a5cbc430f1a9c3d00faaeffd07798508422908a updated readme

现在，假设在 v1.2 时你忘记给项目打标签，也就是在 “updated rakefile” 提交。你可以在之后补上标

签。要在那个提交上打标签，你需要在命令的末尾指定提交的校验和(或部分校验和):

  $ git tag -a v1.2 9fceb02

共享标签

默认情况下，git push命令并不会传送标签到远程仓库服务器上。在创建完标签后你必须显式地推送标

签到共享服务器上。这个过程就像共享远程分支一样-你可以运行git push origin [tagname]。

如果想要一次性推送很多标签，也可以使用带有--tags选项的git push命令。这将会把所有不在远程仓库

服务器上的标签全部传送到那里。

git push origin --tags

### Git 别名

Git 并不会在你输入部分命令时自动推断出你想要的命令。如果不想每次都输入完整的 Git 命令，可以通

过git config 文件来轻松地为每一个命令设置一个别名。这里有一些例子你可以试试:

  $ git config --global alias.co checkout

  $ git config --global alias.br branch

  $ git config --global alias.ci commit

  $ git config --global alias.st status

