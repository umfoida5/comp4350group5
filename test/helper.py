"""A library of helper functions for the CherryPy test suite.

The actual script that runs the entire CP test suite is called
"test.py" (in this folder); test.py calls this module as a library.

Usage
=====
Each individual test_*.py module imports this module (helper),
usually to make an instance of CPWebCase, and then call testmain().

The CP test suite script (test.py) imports this module and calls
run_test_suite, possibly more than once. CP applications may also
import test.py (to use TestHarness), which then calls helper.py.
"""

# GREAT CARE has been taken to separate this module from test.py,
# because different consumers of each have mutually-exclusive import
# requirements. So don't go moving functions from here into test.py,
# or vice-versa, unless you *really* know what you're doing.

import re
import sys
import thread

import cherrypy
from cherrypy.lib import http, profiler
from cherrypy.test import webtest


class CPWebCase(webtest.WebCase):
    
    script_name = ""
    
    def prefix(self):
        return self.script_name.rstrip("/")
    
    def exit(self):
        sys.exit()
    
    def tearDown(self):
        pass
    
    def getPage(self, url, headers=None, method="GET", body=None, protocol=None):
        """Open the url. Return status, headers, body."""
        if self.script_name:
            url = http.urljoin(self.script_name, url)
        webtest.WebCase.getPage(self, url, headers, method, body, protocol)
    
    def assertErrorPage(self, status, message=None, pattern=''):
        """Compare the response body with a built in error page.
        
        The function will optionally look for the regexp pattern,
        within the exception embedded in the error page."""
        
        # This will never contain a traceback
        page = cherrypy._cperror.get_error_page(status, message=message)
        
        # First, test the response body without checking the traceback.
        # Stick a match-all group (.*) in to grab the traceback.
        esc = re.escape
        epage = esc(page)
        epage = epage.replace(esc('<pre id="traceback"></pre>'),
                              esc('<pre id="traceback">') + '(.*)' + esc('</pre>'))
        m = re.match(epage, self.body, re.DOTALL)
        if not m:
            self._handlewebError('Error page does not match\n' + page)
            return
        
        # Now test the pattern against the traceback
        if pattern is None:
            # Special-case None to mean that there should be *no* traceback.
            if m and m.group(1):
                self._handlewebError('Error page contains traceback')
        else:
            if (m is None) or (not re.search(re.escape(pattern), m.group(1))):
                msg = 'Error page does not contain %s in traceback'
                self._handlewebError(msg % repr(pattern))


CPTestLoader = webtest.ReloadingTestLoader()
CPTestRunner = webtest.TerseTestRunner(verbosity=2)

def setConfig(conf):
    """Set the global config using a copy of conf."""
    if isinstance(conf, basestring):
        # assume it's a filename
        cherrypy.config.update(conf)
    else:
        cherrypy.config.update(conf.copy())


def run_test_suite(moduleNames, server, conf):
    """Run the given test modules using the given server and conf.
    
    The server is started and stopped once, regardless of the number
    of test modules. The config, however, is reset for each module.
    """
    cherrypy.config.reset()
    setConfig(conf)
    cherrypy.server.quickstart(server)
    cherrypy.engine.start_with_callback(_run_test_suite_thread,
                                        args=(moduleNames, conf))

def sync_apps(profile=False):
    apps = []
    for base, app in cherrypy.tree.apps.iteritems():
        if base == "/":
            base = ""
        if profile:
            apps.append((base, profiler.make_app(app, aggregate=False)))
        else:
            apps.append((base, app))
    apps.sort()
    apps.reverse()
    for s in cherrypy.server.httpservers:
        s.mount_points = apps

def _run_test_suite_thread(moduleNames, conf):
    for testmod in moduleNames:
        # Must run each module in a separate suite,
        # because each module uses/overwrites cherrypy globals.
        cherrypy.tree = cherrypy._cptree.Tree()
        cherrypy.config.reset()
        setConfig(conf)
        
        m = __import__(testmod, globals(), locals())
        setup = getattr(m, "setup_server", None)
        if setup:
            setup()
        
        # The setup functions probably mounted new apps.
        # Tell our server about them.
        sync_apps(profile=conf.get("profiling.on", False))
        
        suite = CPTestLoader.loadTestsFromName(testmod)
        CPTestRunner.run(suite)
        
        teardown = getattr(m, "teardown_server", None)
        if teardown:
            teardown()
    thread.interrupt_main()

def testmain(conf=None):
    """Run __main__ as a test module, with webtest debugging."""
    if conf is None:
        conf = {}
    setConfig(conf)
    try:
        cherrypy.server.quickstart()
        cherrypy.engine.start_with_callback(_test_main_thread)
    except KeyboardInterrupt:
        cherrypy.server.stop()
        cherrypy.engine.stop()

def _test_main_thread():
    try:
        webtest.WebCase.PORT = cherrypy.server.socket_port
        webtest.main()
    finally:
        thread.interrupt_main()

