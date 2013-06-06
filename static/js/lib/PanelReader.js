function PanelReader() {
    PanelReader.superclass.constructor.call(this);
    this.reader = null;
    this.panelBook = null;

    var f = complib.floatFormat;
    var s = complib.stringFormat;
    var b = complib.boolFormat;
    var d = complib.dateFormat;
    var m = complib.moneyFormat;
    this.v_cardsts_r = function (obj) { return obj.cardsts == '0'; };
    this.v_isexp_c = function (obj) { return obj.isexp_c == false; };
    this.v_quantity = function (obj) { return obj.quantity < obj.typquantity; };
    this.v_deposit=function (obj) { return obj.deposit >= obj.typdeposit; };

    this.descs = [
        { readername: [s, null, null] }, { gender_r: [s, null, null] }, { orgcd_r: [s, null, null] },
        { typname: [s, null, null] }, { cardsts_r: [s, null, this.v_cardsts_r] }, { expdt: [d, null, this.v_isexp_c] },
        { typquantity: [s, null, null] }, { quantity: [s, null, this.v_quantity] }, { typdeposit: [m, null, null] },
        { deposit: [m, null, this.v_deposit]}, { typrenewtimes: [s, null, null] }, { typrenewterm: [s, null, null] }
    ];

    this.formId = "reader_result";
    this.descId = "reader_desc";
    this.searchId = "search_readercardno";
    this.searchBtn = "btn_getreader";

    this.validateMsg = "";
    this.unexistMsg = "会员不存在";
    this.overdueMsg = "存在超期未还";
}
extend(PanelReader, PanelBase);
PanelReader.prototype.checkData = function (reader) {
    var isValidate = true;
    if (!this.v_cardsts_r(reader)) {
        isValidate = false;
    }
    if (!this.v_isexp_c(reader)) {
        isValidate = false;
    }
    if (!this.v_quantity(reader)) {
        isValidate = false;
    }
    if (!this.v_deposit(reader)) {
        isValidate = false;
    }
    if (reader.hasoverdue_c === true) {
        isValidate = false;
        this.showDesc(this.overdueMsg, "warndesc");
    }
    return isValidate;
};
PanelReader.prototype.setData = function (reader) {
    this.reader = reader;
};
PanelReader.prototype.notifyNext = function () {
    this.disabled();
    this.panelBook.prepare();
};
//ui
PanelReader.prototype.clear = function () {
    this.clearForm();
    this.clearDesc();
    this.clearWarn(this.reader);
    this.reader = null;
    this.panelBook.reset();
};
PanelReader.prototype.disabled = function () {
    $('#' + this.searchId).attr({ disabled: "disabled" });
    $('#' + this.searchBtn).attr({ disabled: "disabled" });
};
PanelReader.prototype.increase_quantity = function () {
    this.reader.quantity += 1;
    var $target = $("#txt_quantity")
    $target.val(this.reader.quantity);
    complib.glitter($target);
};
PanelReader.prototype.getReader = function (readercardno) {
    this.clear();
    this.xhrData('/borrow/borrow', 'GET', { act: 'reader', readercardno: readercardno });
};