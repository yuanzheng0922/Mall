# -*- coding: utf-8 -*-
# @Author : yz
# @Time   : 2018/5/11-16:50
from flask_migrate import Migrate,MigrateCommand,Manager
from mall import create_app,db,models


app = create_app('Develop')
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
	print app.url_map
	manager.run()
	# app.run()
