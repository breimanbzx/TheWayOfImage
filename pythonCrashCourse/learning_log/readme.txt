在cmd终端切换到当前路径
创建虚拟环境
virtualenv ll_env

1.启动虚拟环境
ll_env\Scripts\activate

2.在django中创建项目learning_log
diango-admin startproject learning_log .

3.创建数据库
python manange.py migrate

4.启动服务
python manage.py runserver

