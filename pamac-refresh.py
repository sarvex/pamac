#! /usr/bin/pkexec /usr/bin/python3
# -*- coding:utf-8 -*-

from time import sleep
from pamac import common, config

if not common.pid_file_exists():
	common.write_pid_file()
	print('refreshing')
	handle = config.handle()
	for db in handle.get_syncdbs():
		try:
			t = handle.init_transaction()
			db.update(force = False)
			t.release()
		except:
			try:
				t.release()
			except:
				pass
			print('refreshing {} failed'.format(db.name))
			break
		else:
			print('refreshing {} succeeded'.format(db.name))
	sleep(1)
	common.rm_pid_file()
