# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333678267.7650001
_template_filename=u'F:/eclipsWorkSpace/pylibrary/tmpl/borrow/renew_0.html'
_template_uri=u'renew_0.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<script language="javascript" type="text/javascript">\r\n    $(document).ready(function () {\r\n        window.panelReader = new PanelReader2(function (reader, borrnow) {\r\n            addRow(reader, borrnow);\r\n        });\r\n\r\n        function getReader() {\r\n            complib.getInput(\'#search_readercardno\', function (readercardno) {\r\n                panelReader.getReader(readercardno);\r\n            });\r\n        }\r\n        function resetReader() {\r\n            panelReader.clear();\r\n            $(\'#search_readercardno\').val(\'\');\r\n            $(\'#search_readercardno\').removeAttr("disabled");\r\n\r\n            window.location.reload();\r\n        }\r\n        $(\'#search_readercardno\').focus();\r\n        $(\'#search_readercardno\').keydown(function (event) {\r\n            if (event.keyCode == 13) {\r\n                getReader();\r\n            }\r\n        });\r\n        $(\'#btn_getreader\').bind(\'click\', getReader);\r\n        $(\'#btn_resetreader\').bind(\'click\', resetReader);\r\n\r\n        window.done = resetReader;\r\n    });  \r\n</script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


