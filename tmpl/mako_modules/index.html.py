# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 6
_modified_time = 1333091159.734
_template_filename='F:/eclipsWorkSpace/pylibrary/tmpl/public/index.html'
_template_uri='index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\r\n<script src="/static/js/com/jquery-1.7.2.min.js"></script>\r\n<style>\r\n    body{ background:#000}\r\n    \r\nul.topnav {  \r\n    list-style: none;  \r\n    padding: 0 20px;  \r\n    margin: 0;  \r\n    float: left;  \r\n    width: 920px;  \r\n    background: #222;  \r\n    font-size: 1.2em;  \r\n    background: url(topnav_bg.gif) repeat-x;  \r\n}  \r\nul.topnav li {  \r\n    float: left;  \r\n    margin: 0;  \r\n    padding: 0 15px 0 0;  \r\n    position: relative; /*--Declare X and Y axis base for sub navigation--*/  \r\n}  \r\nul.topnav li a{  \r\n    padding: 10px 5px;  \r\n    color: #fff;  \r\n    display: block;  \r\n    text-decoration: none;  \r\n    float: left;  \r\n}  \r\nul.topnav li a:hover{  \r\n    background: url(topnav_hover.gif) no-repeat center top;  \r\n}  \r\nul.topnav li span { /*--Drop down trigger styles--*/  \r\n    width: 17px;  \r\n    height: 35px;  \r\n    float: left;  \r\n    background: url(subnav_btn.gif) no-repeat center top;  \r\n}  \r\nul.topnav li span.subhover {background-position: center bottombottom; cursor: pointer;} /*--Hover effect for trigger--*/  \r\nul.topnav li ul.subnav {  \r\n    list-style: none;  \r\n    position: absolute; /*--Important - Keeps subnav from affecting main navigation flow--*/  \r\n    left: 0; top: 35px;  \r\n    background: #333;  \r\n    margin: 0; padding: 0;  \r\n    display: none;  \r\n    float: left;  \r\n    width: 170px;  \r\n    border: 1px solid #111;  \r\n}  \r\nul.topnav li ul.subnav li{  \r\n    margin: 0; padding: 0;  \r\n    border-top: 1px solid #252525; /*--Create bevel effect--*/  \r\n    border-bottom: 1px solid #444; /*--Create bevel effect--*/  \r\n    clear: both;  \r\n    width: 170px;  \r\n}  \r\nhtml ul.topnav li ul.subnav li a {  \r\n    float: left;  \r\n    width: 145px;  \r\n    background: #333 url(dropdown_linkbg.gif) no-repeat 10px center;  \r\n    padding-left: 20px;  \r\n}  \r\nhtml ul.topnav li ul.subnav li a:hover { /*--Hover effect for subnav links--*/  \r\n    background: #222 url(dropdown_linkbg.gif) no-repeat 10px center;  \r\n}  \r\n</style>\r\n\r\n<ul class="topnav">  \r\n    <li><a href="#">Home</a></li>  \r\n    <li>  \r\n        <a href="#">Tutorials</a>  \r\n        <ul class="subnav">  \r\n            <li><a href="#">Sub Nav Link</a></li>  \r\n            <li><a href="#">Sub Nav Link</a></li>  \r\n        </ul>  \r\n    </li>  \r\n    <li>  \r\n        <a href="#">Resources</a>  \r\n        <ul class="subnav">  \r\n            <li><a href="#">Sub Nav Link</a></li>  \r\n            <li><a href="#">Sub Nav Link</a></li>  \r\n        </ul>  \r\n    </li>  \r\n    <li><a href="#">About Us</a></li>  \r\n    <li><a href="#">Advertise</a></li>  \r\n    <li><a href="#">Submit</a></li>  \r\n    <li><a href="#">Contact Us</a></li>  \r\n</ul>  \r\n\r\n<script>\r\n$(document).ready(function(){  \r\n  \r\n    $("ul.subnav").parent().append("<span></span>"); //Only shows drop down trigger when js is enabled (Adds empty span tag after ul.subnav*)  \r\n  \r\n    $("ul.topnav li span").click(function() { //When trigger is clicked...  \r\n  \r\n        //Following events are applied to the subnav itself (moving subnav up and down)  \r\n        $(this).parent().find("ul.subnav").slideDown(\'fast\').show(); //Drop down the subnav on click  \r\n  \r\n        $(this).parent().hover(function() {  \r\n        }, function(){  \r\n            $(this).parent().find("ul.subnav").slideUp(\'slow\'); //When the mouse hovers out of the subnav, move it back up  \r\n        });  \r\n  \r\n        //Following events are applied to the trigger (Hover events for the trigger)  \r\n        }).hover(function() {  \r\n            $(this).addClass("subhover"); //On hover over, add class "subhover"  \r\n        }, function(){  //On Hover Out  \r\n            $(this).removeClass("subhover"); //On hover out, remove class "subhover"  \r\n    });  \r\n  \r\n});  \r\n</script>\r\n\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


