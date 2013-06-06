# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333946548.4530001
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/borrow/lost_1.html'
_template_uri=u'lost_1.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<div class="table-wrapper">\r\n    <table id="borrnow_table" width="100%">\r\n        <thead>\r\n            <tr>\r\n                <th class="table-header light">\r\n                    bookinsid\r\n                </th>\r\n                <th class="table-header light">\r\n                    bookclsid\r\n                </th>\r\n                <th class="table-header light">\r\n                    bookname\r\n                </th>\r\n                <th class="table-header light">\r\n                    auth\r\n                </th>\r\n                <th class="table-header light">\r\n                    isbn\r\n                </th>\r\n                <th class="table-header light">\r\n                    pub\r\n                </th>\r\n                <th class="table-header light">\r\n                    borrdt\r\n                </th>\r\n                <th class="table-header light">\r\n                    borrexpdt\r\n                </th>\r\n                <th class="table-header light">\r\n                    overdays\r\n                </th>\r\n                <th class="table-header light">\r\n                    typoverprice\r\n                </th>\r\n                <th class="table-header light">\r\n                    overprice\r\n                </th>\r\n                <th class="table-header light">\r\n                    op\r\n                </th>\r\n            </tr>\r\n        </thead>\r\n        <tbody>\r\n        </tbody>\r\n    </table>\r\n</div>\r\n<script language="javascript" type="text/javascript">\r\n    $(document).ready(function () {\r\n        function addRow(reader, borrnow) {\r\n            var tr = document.createElement("tr");\r\n            tr.id = "tr_" + borrnow.bookinsid;\r\n            tr.className = "table-row";\r\n            $(tr).data("borrnow", borrnow);\r\n\r\n            bindTr(tr, borrnow);\r\n\r\n            var td_lost = complib.createTdBtn("btn_lost_" + borrnow.bookinsid, "\u4e22\u5931", function () {\r\n                render_lost(reader, borrnow);\r\n            });\r\n            $(td_lost).addClass("center");\r\n            tr.appendChild(td_lost);\r\n\r\n            $("#borrnow_table tbody").append(tr);\r\n        }\r\n\r\n        function bindTr(tr, borrnow) {\r\n            var f = complib.floatFormat;\r\n            var s = complib.stringFormat;\r\n            var b = complib.boolFormat;\r\n            var d = complib.dateFormat;\r\n            var m = complib.moneyFormat;\r\n            var v_borrexpdt = function (obj) { return obj.notborrexp_c; };\r\n            var v_overdays = function (obj) { return obj.overdays_c <= 0; };\r\n\r\n            var descs = [\r\n                { bookinsid: [s, null, null] }, { bookclsid: [s, null, null] }, { bookname: [s, null, null] },\r\n                { auth: [s, null, null] }, { isbn: [s, null, null] }, { pubcd_r: [s, null, null] },\r\n                { borrdt: [d, null, null] }, { borrexpdt: [d, null, v_borrexpdt] }, { overdays_c: [s, "right", v_overdays] },\r\n                { typoverprice_c: [m, "right", null] }, { overprice_c: [m, "right", v_overdays] }\r\n            ];\r\n            complib.appendTdArr(tr, borrnow, "bookinsid", descs);\r\n        }\r\n\r\n        function render_lost(reader, borrnow) {\r\n            $.jBox.open(\'iframe:/borrow/lost?\' + $.param({ act: "dialog", bookinsid: borrnow.bookinsid }),\r\n                "\u4e22\u5931\u5904\u7406", 600, 320, { buttons: { "\u53d6\u6d88": false} });\r\n        }\r\n\r\n        window.addRow = addRow;\r\n        window.close_dialog = function (bookinsid, paycd) {\r\n            $.jBox.close(true);\r\n            complib.chgTdStatus($("#btn_lost_" + bookinsid).parent("td")[0], "ok");\r\n            if (paycd == \'ACC\')\r\n                panelReader.decrease_acc(getBorrnow(bookinsid).sumprice_c);\r\n        };\r\n        window.getBorrnow = function (bookinsid) {\r\n            return $("#tr_" + bookinsid).data("borrnow");\r\n        };\r\n\r\n    });\r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


