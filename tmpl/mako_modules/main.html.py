# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333678264.234
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/public/main.html'
_template_uri=u'main.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = [u'head', u'title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def head():
            return render_head(context.locals_(__M_locals))
        next = context.get('next', UNDEFINED)
        self = context.get('self', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        def title():
            return render_title(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        # SOURCE LINE 2
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'head'):
            context['self'].head(**pageargs)
        

        # SOURCE LINE 9
        __M_writer(u'\r\n\r\n<div id="head">\r\n\u5c45\u5bb6\u5065\u5eb7\u7ba1\u7406\u65b9\u6848\r\n</div>\r\n<div id="menu">\r\n')
        # SOURCE LINE 15
        runtime._include_file(context, u'menu.html', _template_uri)
        __M_writer(u'\r\n</div>\r\n<p class="clear"></p>\r\n\r\n')
        # SOURCE LINE 19
        __M_writer(unicode(next.body(**context.kwargs)))
        __M_writer(u'\r\n\r\n<hr style="margin-top:20px"/>\r\n')
        # SOURCE LINE 22
        runtime._include_file(context, u'footer.html', _template_uri)
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def head():
            return render_head(context)
        self = context.get('self', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\r\n  ')
        # SOURCE LINE 4
        __M_writer(unicode(parent.head()))
        __M_writer(u'\r\n  ')
        # SOURCE LINE 5
        __M_writer(unicode(self.css("main.css")))
        __M_writer(u'\r\n  ')
        # SOURCE LINE 6
        __M_writer(unicode(self.css('superfish.css')))
        __M_writer(u'\r\n  ')
        # SOURCE LINE 7
        __M_writer(unicode(self.js("com/hoverIntent.js")))
        __M_writer(u'\r\n  ')
        # SOURCE LINE 8
        __M_writer(unicode(self.js("com/superfish.js")))
        __M_writer(u'\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


