#!/usr/bin/python

import cherrypy
import os.path
from controller.root import Root
from modules import database
from modules import createTemporaryUser

database.init()

app = cherrypy.tree.mount(Root(), '', 'config/app.conf')

if __name__ == '__main__':
    cherrypy.config.update('config/global_dev.conf')
    app.merge('config/app_dev.conf')
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    cherrypy.config.update('config/global_prod.conf')
