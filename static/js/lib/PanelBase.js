function PanelBase() { }
PanelBase.prototype = {
    clearForm: function () {
        $('#' + this.formId)[0].reset();
    },
    clearDesc: function () {
        var $desc = $('#' + this.descId);
        $desc.removeAttr("class");
        $desc.html();
        $desc.hide();
    },
    clearWarn: function (data) {
        complib.renderObj(data, this.descs,
            null, //css
            function ($target, attr) {//warn
                $target.removeClass("warn");
                $('#lab_' + attr).removeClass("warn");
            },
            function (attr, val) {//gen
                $target = $('#txt_' + attr);
                return $target;
            }
        );
    },
    showDesc: function (msg, clsnm) {
        var $desc = $('#' + this.descId);
        $desc.removeAttr("class");
        $desc.addClass(clsnm);
        $desc.html("<em></em>" + msg);
        $desc.show();
    },
    showValidate: function () {
        this.showDesc(this.validateMsg, "validatedesc");
    },
    showUnexist: function () {
        this.showDesc(this.unexistMsg, "warndesc");
    },

    render: function (data) {
        complib.renderObj(data, this.descs,
            function ($target, attr, css) {//css
                $target.addClass(css);
                $('#lab_' + attr).addClass(css);
            },
            function ($target, attr) {//warn
                $target.addClass("warn");
                $('#lab_' + attr).addClass("warn");
            },
            function (attr, val) {//gen
                $target = $('#txt_' + attr);
                $target.val(val);
                return $target;
            }
        );
    },
    setData: function (data) { },
    okData: function (data) { },
    xhrData: function (url, type, para) {
        var me = this;
        complib.xhr(url, type, para, function (data) {
            if (complib.isEmpty(data)) {
                me.showUnexist();
                return;
            }
            me.setData(data);
            me.render(data);
            if (me.checkData(data)) {
                me.okData(data);
                me.showValidate();
                me.notifyNext();
            }
        });
    }
};