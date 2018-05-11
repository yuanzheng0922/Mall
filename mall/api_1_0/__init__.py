# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/11-16:53


from flask import Blueprint

api = Blueprint('api_1',__name__)

from . import index
