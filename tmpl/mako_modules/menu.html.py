# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333678264.2650001
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/public/menu.html'
_template_uri=u'menu.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<ul class="sf-menu">\r\n    <li><a href="#">\u8bbe\u5907\u7ba1\u7406</a>\r\n        <ul>\r\n            <li><a href=\'/borrow/borrow\'>\u8bbe\u5907\u7ed1\u5b9a</a></li>\r\n            <li><a href=\'/borrow/giveback\'>\u8bbe\u5907\u89e3\u7ed1</a></li>\r\n            <li><a href=\'/borrow/renew\'>\u8bbe\u5907\u91cd\u542f</a></li>\r\n            <li><a href=\'/borrow/lost\'>\u8bbe\u5907\u6302\u5931</a></li>\r\n        </ul>\r\n    </li>\r\n    <li><a href="#">\u5065\u5eb7\u62a5\u8868</a>\r\n        <ul>\r\n            <li><a href=\'#\'>borrow</a>\r\n                <ul>\r\n                    <li><a href=\'/borrow/borrow\'>borrow</a></li>\r\n                    <li><a href=\'/borrow/giveback\'>giveback</a></li>\r\n                    <li><a href=\'/borrow/renew\'>renew</a></li>\r\n                </ul>\r\n            </li>\r\n            <li><a href=\'/borrow/giveback\'>giveback</a></li>\r\n            <li><a href=\'/borrow/renew\'>renew</a></li>\r\n        </ul>\r\n    </li>\r\n</ul>\r\n<script type="text/javascript">\r\n    $(document).ready(function () {\r\n        $(\'ul.sf-menu\').superfish();\r\n    });\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


