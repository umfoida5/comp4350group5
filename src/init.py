#!/usr/bin/python

import cherrypy
import os.path
from controller.root import Root
from modules.database import init_db

init_db()

cherrypy.tree.mount(Root(), '', 'config/app.conf')

if __name__ == '__main__':
    cherrypy.config.update('config/dev_global.conf')
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    cherrypy.config.update('config/prod_global.conf')
