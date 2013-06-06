#coding:utf-8
import web
import datetime

### mako
#from web.contrib.template import render_mako
from mako.template import Template
from mako.lookup import TemplateLookup
from mako import exceptions
from logic import fn_utils

import os
_basedir = os.path.join(fn_utils.module_path(), 'tmpl').replace('\\', '/')
print _basedir
lookup = TemplateLookup(directories = [_basedir + '/public', _basedir + '/borrow', _basedir + '/sub', _basedir + '/gencode'],
                          output_encoding = 'utf-8',
                          input_encoding = 'utf-8',
                          #default_filters=['decode.utf8'],
                          module_directory = 'tmpl/mako_modules')

def render(templatename, **kwargs):
    try:
        mytemplate = lookup.get_template(templatename)
        return mytemplate.render(**kwargs)
    except:
        return exceptions.html_error_template().render()


### json
try:
    import json
except ImportError:
    import simplejson as json

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self, obj)

def jsondumps(obj):
    return json.dumps(obj, cls = JSONDateTimeEncoder)

def datetime_decoder(d):
    if isinstance(d, list):
        pairs = enumerate(d)
    elif isinstance(d, dict):
        pairs = d.items()
    result = []
    for k, v in pairs:
        if isinstance(v, basestring):
            try:
                # The %f format code is only supported in Python >= 2.6.
                # For Python <= 2.5 strip off microseconds
                # v = datetime.datetime.strptime(v.rsplit('.', 1)[0],
                #     '%Y-%m-%dT%H:%M:%S')
                v = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
            except ValueError:
                try:
                    v = datetime.datetime.strptime(v, '%Y-%m-%d').date()
                except ValueError:
                    pass
        elif isinstance(v, (dict, list)):
            v = datetime_decoder(v)
        result.append((k, v))
    if isinstance(d, list):
        return [x[1] for x in result]
    elif isinstance(d, dict):
        return dict(result)

def jsonloads(obj):
    return json.loads(obj, object_hook = datetime_decoder)



def jsonOut(fn):
    def decorate(*args, **kw):
        return jsondumps(fn(*args, **kw))
    return decorate



### basehander
class BaseHandler:
    def GET(self):
        self.q = web.input(act = '')
        self.o = get_operator()
        if self.q.act == '':
            return self.entry()
        else:
            return getattr(self, self.q.act)()

    def POST(self):
        return self.GET()


def onlyPost(fn):
    def decorate(*args, **kw):
        if web.ctx["method"] != 'POST':
            return None
        return fn(*args, **kw)
    return decorate


def get_operator():
    try:
        return web.ctx["session"].operator
    except:
        return "fakeadmin"


