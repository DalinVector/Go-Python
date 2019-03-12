# U CAN U UP NO BB学习记录
## 2019年3月8日 第二天
- 昨天的问题也一并记录在此吧：
    
    在安装完VSCode后，怎么都不能在"Terminal"里克隆自己的GitHub仓库，心急如焚。在诸位童鞋帮助下，又冷静的搜索了一些答案，发现竟让是电脑木有安装GitHub的客户端！遂解决。
- 今天在克隆的时候应该输入
    ```
    git clone https://github.com/DalinVector/Go-Python.git
    ```
    然而，第一次在clone后面少了一个空格竟然木有成功呢，所以，这么个小细节能影响成败呢！
- 就在刚刚，21点7分，我TM竟然push成功了！虽然云里雾里，但是确实是成功了！

无图言吊：

![](C:\Users\HUHU\Desktop\捕获.png)

![](C:\Users\HUHU\Desktop\捕获1.png)
## 2019年3月9日 第三天

- 作业为复习之前的vscode指令，熟悉push操作，记录学习进度。
- 完成情况：

    1.当在目录库下新创建分支文件或文件夹时，首次上传的指令为：

    git add +文件名/文件夹名

    -Enter

    git commit -m +"推送备注"

    -Enter

    git push origin master
    
    -Enter
2. 当在原有文件基础上做了变动及变更的情况下，上传指令为：


    git add -A

    -Enter

    git commit -m +"推送备注"

    -Enter

    git push origin master

    -Enter
## 2019年3月12日 第五天

- 任务：

    1、阅读相关电子书，对照参考，熟悉布尔值与布林运算相关概念。

    2、创建1个新的py文件，并把所有的布林运算的情况，都写在脚本中，并执行运算你观察结果。比如：

    True and True True or False not True

    3、然后再次回顾书中相关介绍。

    4、熟练使用 print() 和 #注释 ，来帮助自己理解今日脚本中的每一句。

    5、所有练习推送提交到github。
- 练习：

    1. 经查，布尔值“True"为真，"False"为假，python语言中所有数据类型都自带布尔值，数据只有在0，None和空的时候，其布尔值为False。
    2. 对布尔值进行的运算成为布林运算or  and和not。类似高中时候学的“或”，“且”，“非”运算：

        或：有真则真，同假则假

        且：有假则假，同真则真

        非：假则真，真则假
    3. 在运算优先级上的规则：

        not>and>or
    
    练习代码见文档Hellopython.py
