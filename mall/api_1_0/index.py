# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/11-18:00
from . import api
from mall import redis_store
from flask import session

@api.route('/index')
def index():
	session['name'] = 'xxxxxxxxxxx' # 测试开启session后,
	redis_store.set('name=','xiaobai')
	return 'ceshi'
