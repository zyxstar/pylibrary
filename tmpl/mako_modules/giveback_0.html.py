# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333679330.5309999
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/borrow/giveback_0.html'
_template_uri=u'giveback_0.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<script language="javascript" type="text/javascript">\r\n    $(document).ready(function () {\r\n        var panelBook = new PanelBook2(function (borrhis) {\r\n            addRow(borrhis);\r\n        });\r\n\r\n        function reset() {\r\n            panelBook.clear();\r\n            window.location.reload();\r\n        }\r\n\r\n        function postBorrhis() {\r\n            complib.getInput(\'#search_bookinsid\', function (bookinsid) {\r\n                panelBook.postBorrhis(bookinsid);\r\n            });\r\n        }\r\n\r\n        function clearBook() {\r\n            panelBook.clear();\r\n            $(\'#search_bookinsid\').val(\'\');\r\n            try {\r\n                $(\'#search_bookinsid\').focus();\r\n            } catch (e) { }\r\n        }\r\n\r\n        $(\'#search_bookinsid\').keydown(function (event) {\r\n            if (event.keyCode == 13) {\r\n                postBorrhis();\r\n            }\r\n        });\r\n\r\n        $(\'#btn_getbook\').bind(\'click\', postBorrhis);\r\n        $(\'#btn_clearbook\').bind(\'click\', clearBook);\r\n\r\n        $(\'#search_bookinsid\').focus();\r\n\r\n        window.done = reset;\r\n    });  \r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


