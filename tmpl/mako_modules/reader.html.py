# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333678264.2650001
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/sub/reader.html'
_template_uri=u'reader.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div id="panelreader" class="panel">\r\n    <label for="search_readercardno">\r\n        \u4f1a\u5458\u5361\u53f7:</label>\r\n    <br />\r\n    <input type="text" id="search_readercardno" class="search-field" />\r\n    <input type="button" id="btn_getreader" class="btn" value="\u67e5\u627e" />\r\n    <input type="button" id="btn_resetreader" class="btn" value="\u91cd\u7f6e" />\r\n    <span id="reader_desc"></span>\r\n    <form id="reader_result" name="reader_result" action="">\r\n    <ul class="result">\r\n        <li>\r\n            <label id="lab_readername" for="txt_readername">\r\n                \u59d3\u540d</label>\r\n            <input type="text" id="txt_readername" readonly="readonly" />\r\n        </li>\r\n        <li>\r\n            <label id="lab_orgcd_r" for="txt_orgcd_r">\r\n                \u5355\u4f4d</label>\r\n            <input type="text" id="txt_orgcd_r" readonly="readonly" />\r\n        </li>\r\n        <li class="short">\r\n            <label id="lab_gender_r" for="txt_gender_r">\r\n                \u6027\u522b</label>\r\n            <input type="text" id="txt_gender_r" readonly="readonly" />\r\n            <label id="lab_typname" for="txt_typname" class="shortlabel">\r\n                \u7c7b\u578b</label>\r\n            <input type="text" id="txt_typname" readonly="readonly" />\r\n        </li>\r\n        <li class="short">\r\n            <label id="lab_cardsts_r" for="txt_cardsts_r">\r\n                \u72b6\u6001</label>\r\n            <input type="text" id="txt_cardsts_r" readonly="readonly" />\r\n            <label id="lab_expdt" for="txt_expdt" class="shortlabel">\r\n                \u5931\u6548\u65e5\u671f</label>\r\n            <input type="text" id="txt_expdt" readonly="readonly" />\r\n        </li>\r\n        <li class="short">\r\n            <label id="lab_typquantity" for="txt_typquantity">\r\n                typquantity</label>\r\n            <input type="text" id="txt_typquantity" readonly="readonly" />\r\n            <label id="lab_quantity" for="txt_quantity" class="shortlabel">\r\n                quantity</label>\r\n            <input type="text" id="txt_quantity" readonly="readonly" />\r\n        </li>\r\n        <li class="short">\r\n            <label id="lab_typdeposit" for="txt_typdeposit">\r\n                typdeposit</label>\r\n            <input type="text" id="txt_typdeposit" readonly="readonly" />\r\n            <label id="lab_deposit" for="txt_deposit" class="shortlabel">\r\n                deposit</label>\r\n            <input type="text" id="txt_deposit" readonly="readonly" />\r\n        </li>\r\n        <li class="short">\r\n            <label id="lab_typrenewtimes" for="txt_typrenewtimes">\r\n                typrenewtimes</label>\r\n            <input type="text" id="txt_typrenewtimes" readonly="readonly" />\r\n            <label id="lab_typrenewterm" for="txt_typrenewterm" class="shortlabel">\r\n                typrenewterm</label>\r\n            <input type="text" id="txt_typrenewterm" readonly="readonly" />\r\n        </li>\r\n        <li class="clear"></li>\r\n    </ul>\r\n    </form>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


