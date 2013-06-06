# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333678264.2650001
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/sub/book.html'
_template_uri=u'book.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div id="panelbook" class="panel">\r\n    <label for="search_bookinsid">\r\n        \u8bbe\u5907\u7f16\u53f7:</label>\r\n    <br />\r\n    <input type="text" id="search_bookinsid" />\r\n    <input type="button" id="btn_getbook" class="btn" value="\u67e5\u627e" />\r\n    <input type="button" id="btn_clearbook" class="btn" value="\u6e05\u7a7a" />\r\n    <span id="book_desc"></span>\r\n    <form id="book_result" name="reader_result" action="">\r\n    <ul class="result">\r\n        <li>\r\n            <label id="lab_bookinsid" for="txt_bookinsid">\r\n                \u8bbe\u5907\u7f16\u53f7</label>\r\n            <input type="text" id="txt_bookinsid" readonly="readonly" />\r\n        </li>\r\n        <li>\r\n            <label id="lab_bookclsid" for="txt_bookclsid">\r\n                bookclsid</label>\r\n            <input type="text" id="txt_bookclsid" readonly="readonly" />\r\n        </li>\r\n        <li>\r\n            <label id="lab_bookname" for="txt_bookname">\r\n                \u8bbe\u5907\u540d\u79f0</label>\r\n            <input type="text" id="txt_bookname" readonly="readonly" />\r\n        </li>\r\n        <li>\r\n            <label id="lab_auth" for="txt_auth">\r\n                auth</label>\r\n            <input type="text" id="txt_auth" readonly="readonly" />\r\n        </li>\r\n        <li class="short">\r\n            <label id="lab_inssts_r" for="txt_inssts_r">\r\n                \u8bbe\u5907\u72b6\u6001</label>\r\n            <input type="text" id="txt_inssts_r" readonly="readonly" />\r\n            <label id="lab_catcd_r" for="txt_catcd_r" class="shortlabel">\r\n                catcd_r</label>\r\n            <input type="text" id="txt_catcd_r" readonly="readonly" />\r\n        </li>\r\n        <li class="short">\r\n            <label id="lab_pubcd_r" for="txt_pubcd_r">\r\n                pubcd_r</label>\r\n            <input type="text" id="txt_pubcd_r" readonly="readonly" />\r\n            <label id="lab_isbn" for="txt_isbn" class="shortlabel">\r\n                isbn</label>\r\n            <input type="text" id="txt_isbn" readonly="readonly" />\r\n        </li>\r\n        <li class="short">\r\n            <label id="lab_price" for="txt_price">\r\n                price</label>\r\n            <input type="text" id="txt_price" readonly="readonly" />\r\n            <label id="lab_placecd_r" for="txt_placecd_r" class="shortlabel">\r\n                placecd_r</label>\r\n            <input type="text" id="txt_placecd_r" readonly="readonly" />\r\n        </li>\r\n        <li class="clear"></li>\r\n    </ul>\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


