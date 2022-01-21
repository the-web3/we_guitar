### 小型博客系统，效果图如下

### PC 端效果
.： 
    ![.： 
](https://github.com/guoshijiang/we_guitar/blob/main/common/static/images/1.png)


### 手机端效果
.： 
    ![.： 
](https://github.com/guoshijiang/we_guitar/blob/main/common/static/images/2.png)


#### 1.项目介绍

整个项目是 Python 的 Django 框架编写，项目包含 PC 网页端，H5端。

#### 2.使用该代码部署自己的博客条件

-友链到该代码仓库，并把 问我学院: http://www.wenwoha.com; 链眼社区：https://chaineye.info/; 币家：http://coinfamily.cc/ 做为友链

#### 3.代码部署

在部署代码前，你需要安装 python 3.8 以上版本，Mysql 数据库和 Redis

第一步，克隆代码：
```buildoutcfg
git clone git@github.com:guoshijiang/chaineye.git
```

第二步，搭建一个 virtualenv：
```buildoutcfg
cd chaineye
virtualenv .env
source .env/bin/activate
```

第三步，安装依赖：
```buildoutcfg
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

第四步，数据库migrate：
```buildoutcfg
 python3 manage.py migrate
```
如果你改变数据库结构，请先运行 `python3 manage.py makemigrations`, 然后再运行 `python3 manage.py migrate`

第五步，Django Admin 的使用：
```buildoutcfg
 python3 manage.py createsuperuser
```
按照提示完成操作之后去 Django admin登陆。

第六步，运行服务：
```buildoutcfg
 python3 manage.py runserver
```

如果你在线上部署，建议使用，supervisor 管理进程，Ng 转发，把静态文件使用 `python3 manage.py collectstatic` 收集到相应的目录。


### 注意

如果您使用这套代码，搭建过程中有任何问题，可以去问我学院（www.wenwoha.com） 上面找联系方式联系我们，也可以直接加我的微信：LGZAXE





