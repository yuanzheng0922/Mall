# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/11-16:52
from flask import Flask,session
import redis
import pymysql
pymysql.install_as_MySQLdb()
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from config import config_dict
import logging
from logging.handlers import RotatingFileHandler


redis_store = None
db = SQLAlchemy()

def set_loglevel(level):
	# 设置日志的记录等级
	logging.basicConfig(level=level)  # 调试debug级
	# 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
	file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
	# 创建日志记录的格式                 日志等级    输入日志信息的文件名 行数    日志信息
	formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
	# 为刚创建的日志记录器设置日志记录格式
	file_log_handler.setFormatter(formatter)
	# 为全局的日志工具对象（flask app使用的）添加日志记录器
	logging.getLogger().addHandler(file_log_handler)



# 工厂函数
def create_app(config_name):
	# 创建app
	app = Flask(__name__)

	config_cls = config_dict[config_name]
	app.config.from_object(config_cls)  # 对app进行 config配置
	set_loglevel(config_cls.LOG_LEVEL)
	# db = SQLAlchemy() # 在函数内部,其他py文件无法调用
	db.init_app(app)
	Session(app) #开启session
	CSRFProtect(app)  # 开启防护
	global redis_store
	redis_store = redis.StrictRedis(host=config_cls.REDIS_HOST,port=config_cls.REDIS_PORT)
	# 注册蓝图
	from mall.api_1_0 import api
	app.register_blueprint(api,url_prefix='/api/v1.0')

	return app
