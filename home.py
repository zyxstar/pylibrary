# -*- coding: UTF-8 -*-
import os
import web
from utils import render
import borrow


web.config.debug = True
web.webapi.internalerror = web.debugerror

urls = ('/', 'index',
        '/favicon\.ico', 'favicon',
        '/borrow', borrow.app,
        '/(.*)/', 'redirect')

app = web.application(urls, globals())

if web.config.get('_session') is None:
    session = web.session.Session(app, web.session.DiskStore('sessions'),
                                  {'operator': "sysadmin"})
    web.config._session = session
else:
    session = web.config._session

class index:
    def GET(self):
        return render('index.html')

class favicon:
    def GET(self):
        web.header('Content-Type', 'image/x-icon')
        f = open(os.path.abspath(os.path.dirname(__file__))+'/static/images/favicon.ico', 'rb')
        data = f.read()
        f.close()
        return data

class redirect:
    def GET(self, path):
        web.seeother('/' + path)

def session_hook():
    web.ctx.session = session
    
app.add_processor(web.loadhook(session_hook))

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        sys.argv.append('8081')
    app.run()




