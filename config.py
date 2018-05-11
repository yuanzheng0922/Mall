# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/11-16:53
import redis
import logging
# 配置项类
class ConfigCase(object):

	import base64,os
	SECRET_KEY = 'd7lflaqpWbed0MoJzPubqtVM+5N6SqNDJFiYkVjxqG7KzvSvG0wJGsMpdZHFR6Q8'
	# print base64.b64encode(os.urandom(48))
	# 数据库配置信息
	SQLALCHEMY_DATABASE_URI = 'mysql://user:yuanzheng3@140.143.249.76:3306/ihome26'
	SQLALCHEMY_TRACK_MODIFICATIONS  =False

	#redis配置信息
	REDIS_HOST = '140.143.249.76'
	REDIS_PORT= 6379

	# 设置Session选择哪个数据库
	SESSION_TYPE= 'redis'
	SESSION_USE_SIGNER = True
	SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
	PERMANENT_SESSION_LIFETIME = 60*5

class Product(ConfigCase):
	DEBUG = False  # 关闭调试模式
	LOG_LEVEL = logging.ERROR

class Develop(ConfigCase):
	DEBUG = True  # 开启调试模式
	LOG_LEVEL = logging.DEBUG
config_dict = {
	'Product':Product,
	'Develop':Develop
}