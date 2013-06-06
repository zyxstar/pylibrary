var complib = {
    //ajax
    xhr: function (url, type, data, callback) {
        $.ajax({
            type: type, cache: false, dataType: "json",
            url: url, data: data,
            success: callback,
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                var errMsg;
                if (XMLHttpRequest.status != 200)
                    errMsg = XMLHttpRequest.responseText ? XMLHttpRequest.responseText : "";
                else if (textStatus)
                    errMsg = textStatus + errorThrown ? errorThrown : "";
                $.jBox.error(errMsg, "系统错误", { width: 500, height: 350 });
            }
        });
    },


    //getInputtext
    getInput: function (id, callback) {
        var text = $.trim($(id).val());
        if (text == '') return;
        $(id).val(text);
        callback(text);
    },

    //format
    boolFormat: function (data) {
        if (data == undefined) return "";
        if (data) return "有";
        else return "无";
    },
    floatFormat: function (data) {
        if (data == undefined) return "";
        if (data == 0) return "0.00";
        return data.toFixed(2);
    },
    moneyFormat: function (data) {
        if (data == undefined)
            data = 0;
        return "￥" + complib.floatFormat(data);
    },
    stringFormat: function (data) {
        if (data == undefined) return "";
        return data;
    },
    dateFormat: function (data) {
        if (data == undefined) return "";
        return data.split('T')[0];
    },
    renderObj: function (obj, descs, fnCss, fnWarn, fnGen) {
        if (!obj) return;
        for (var i = 0; i < descs.length; i++) {
            var desc = descs[i];
            for (var attr in desc) {
                var format = desc[attr][0];
                var val = format(obj[attr]);
                var target = fnGen(attr, val);
                var css = desc[attr][1];
                if (css) {
                    fnCss(target, attr, css);
                }
                var validate = desc[attr][2];
                if (validate) {
                    if (!validate(obj)) {
                        fnWarn(target, attr);
                    }
                }
                break;
            }
        }
    },
    fixDescsWarn: function (descs) {
        for (var i = 0; i < descs.length; i++) {
            var desc = descs[i];
            for (var attr in desc)
                desc[attr][2] = null;
        }
    },

    //glitter
    glitter: function ($target) {
        $target.css({ color: '#DE564B', backgroundColor: '#FBEC88' });
        $target.fadeIn('fast', 'linear')
               .fadeOut('fast', 'linear')
               .fadeIn('fast', 'linear')
               .fadeOut('fast', 'linear')
               .fadeIn('fast', function () { $target.removeAttr("style"); });
    },

    //empty
    isEmpty: function (obj) {
        for (var attr in obj) {
            return false;
        }
        return true;
    },
    isOnlyOneAttr: function (obj) {
        var i = 0;
        for (var attr in obj) {
            i++;
        }
        if (i == 1)
            return true;
        return false;
    },


    //table
    createTextNode: function (text) {
        if (text == undefined)
            text = " ";
        return document.createTextNode(text);
    },
    createTd: function (node) {
        var td = document.createElement("td");
        td.appendChild(node);
        return td;
    },
    createTdText: function (text) {
        return complib.createTd(complib.createTextNode(text));
    },
    appendTdArr: function (tr, obj, key, descs) {
        complib.renderObj(obj, descs,
            function ($td, attr, css) {//css
                $td.addClass(css);
            },
            function ($td, attr) {//warn
                $td.addClass("warn");
            },
            function (attr, val) {//gen
                var td = complib.createTdText(val);
                td.id = attr + "_" + obj[key];
                tr.appendChild(td);
                return $(td);
            }
        );
    },

    //btn
    createBtn: function (id, text, onclick) {
        var btn = document.createElement("input");
        btn.id = id;
        btn.type = "button";
        btn.className = "btn",
        btn.value = text;
        $(btn).bind("click", onclick);
        return btn;
    },

    createTdBtn: function (id, text, onclick) {
        return complib.createTd(complib.createBtn(id, text, onclick));
    },

    chgTdStatus: function (td, clsnm) {
        $(td).html("<em></em>");
        $(td).addClass(clsnm);
    }

};

