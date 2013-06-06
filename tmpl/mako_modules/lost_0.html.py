# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333678267.7650001
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/borrow/lost_0.html'
_template_uri=u'lost_0.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        runtime._include_file(context, u'renew_0.html', _template_uri)
        return ''
    finally:
        context.caller_stack._pop_frame()


