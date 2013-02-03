#!/usr/bin/python

import cherrypy
import os.path
from webapp.root import Root

cherrypy.tree.mount(Root(), '', 'app.conf')

if __name__ == '__main__':
    cherrypy.config.update('dev_global.conf')
    cherrypy.engine.start()
    cherrypy.engine.block()
else:
    cherrypy.config.update('prod_global.conf')
