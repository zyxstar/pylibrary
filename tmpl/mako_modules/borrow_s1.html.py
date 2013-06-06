# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1332922928.0780001
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/borrow/borrow_s1.html'
_template_uri=u'borrow_s1.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div class="table-wrapper">\r\n    <table id="borrnow_table" width="100%">\r\n        <thead>\r\n            <tr>\r\n                <th class="table-header light">\r\n                    bookinsid\r\n                </th>\r\n                <th class="table-header light">\r\n                    bookclsid\r\n                </th>\r\n                <th class="table-header light">\r\n                    bookname\r\n                </th>\r\n                <th class="table-header light">\r\n                    auth\r\n                </th>\r\n                <th class="table-header light">\r\n                    isbn\r\n                </th>\r\n                <th class="table-header light">\r\n                    pub\r\n                </th>\r\n                <th class="table-header light">\r\n                    borrdt\r\n                </th>\r\n                <th class="table-header light">\r\n                    borrexpdt\r\n                </th>\r\n                <th class="table-header light">\r\n                    \u72b6\u6001\r\n                </th>\r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n        </tbody>\r\n    </table>\r\n</div>\r\n<div class="center">\r\n    <input type="button" id="btn_fresh" class="btn big" value="\u5b8c\u6210" /><br />\r\n</div>\r\n<script language="javascript">\r\n    function addRow(borrnow) {\r\n        var tr = document.createElement("tr");\r\n        tr.id = "tr_" + borrnow.bookinsid;\r\n        tr.className = "table-row";\r\n\r\n        var f = complib.floatFormat;\r\n        var s = complib.stringFormat;\r\n        var b = complib.boolFormat;\r\n        var d = complib.dateFormat;\r\n        var attrs = [\r\n            { bookinsid: s }, { bookclsid: s }, { bookname: s },\r\n            { auth: s }, { isbn: s }, { pubcd_r: s },\r\n            { borrdt: d }, { borrexpdt_c: d }\r\n        ];\r\n        complib.appendTdArr(tr, borrnow, attrs);\r\n\r\n        tr.appendChild(complib.createTdText("\u6210\u529f\u501f\u51fa"));\r\n        $("#borrnow_table tbody").append(tr);\r\n    }\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


