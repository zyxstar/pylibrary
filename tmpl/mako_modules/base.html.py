# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333678264.25
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/public/base.html'
_template_uri=u'base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = [u'head', 'js', 'css', u'title']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def head():
            return render_head(context.locals_(__M_locals))
        next = context.get('next', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\r\n<html xmlns="http://www.w3.org/1999/xhtml">\r\n<head>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        # SOURCE LINE 21
        __M_writer(u'  \r\n</head>\r\n<body>\r\n\r\n')
        # SOURCE LINE 25
        __M_writer(unicode(next.body(**context.kwargs)))
        __M_writer(u'\r\n\r\n</body>\r\n</html>\r\n\r\n')
        # SOURCE LINE 32
        __M_writer(u'\r\n\r\n')
        # SOURCE LINE 36
        __M_writer(u'\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def head():
            return render_head(context)
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\r\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />\r\n    <title>')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 6
        __M_writer(u'</title>\r\n    <link rel="shortcut icon" href="/static/images/favicon.ico" />\r\n    ')
        # SOURCE LINE 8
        __M_writer(unicode(self.css("base.css")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 9
        __M_writer(unicode(self.css("jbox.css")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 10
        __M_writer(unicode(self.css("btn.css")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 11
        __M_writer(unicode(self.css('table.css')))
        __M_writer(u'\r\n\r\n    ')
        # SOURCE LINE 13
        __M_writer(unicode(self.js("com/utils.js")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 14
        __M_writer(unicode(self.js("com/array-extras.js")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 15
        __M_writer(unicode(self.js("com/jquery-1.7.2.min.js")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 16
        __M_writer(unicode(self.js("com/jquery.jBox-2.3.min.js")))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 17
        __M_writer(unicode(self.js("com/jquery.jBox-zh-CN.js")))
        __M_writer(u'\r\n\r\n    ')
        # SOURCE LINE 19
        __M_writer(unicode(self.js('lib/complib.js')))
        __M_writer(u'\r\n    ')
        # SOURCE LINE 20
        __M_writer(unicode(self.js('lib/PanelBase.js')))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context,path):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\r\n<script src="/static/js/')
        # SOURCE LINE 35
        __M_writer(unicode(path))
        __M_writer(u'" type="text/javascript"></script>\r\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_css(context,path):
    context.caller_stack._push_frame()
    try:
        context._push_buffer()
        __M_writer = context.writer()
        # SOURCE LINE 30
        __M_writer(u'\r\n<link href="/static/css/')
        # SOURCE LINE 31
        __M_writer(unicode(path))
        __M_writer(u'" rel="stylesheet" type="text/css" />\r\n')
    finally:
        __M_buf = context._pop_buffer()
        context.caller_stack._pop_frame()
    return __M_buf.getvalue()


def render_title(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


