function PanelBook(onAdded) {
    PanelBook.superclass.constructor.call(this);
    this.cur_book = null;
    this.borrnowArr = [];
    this.panelReader = null;

    var f = complib.floatFormat;
    var s = complib.stringFormat;
    var b = complib.boolFormat;
    var d = complib.dateFormat;
    var m = complib.moneyFormat;
    this.v_inssts_r = function (obj) { return obj.inssts == '0'; };

    this.descs = [
        { bookinsid: [s, null, null] }, { bookname: [s, null, null] }, { bookclsid: [s, null, null] },
        { inssts_r: [s, null, this.v_inssts_r] }, { auth: [s, null, null] }, { isbn: [s, null, null] },
        { pubcd_r: [s, null, null] }, { catcd_r: [s, null, null] }, { placecd_r: [s, null, null] },
        { price: [m, null, null] }
    ];

    this.formId = "book_result";
    this.descId = "book_desc";
    this.searchId = "search_bookinsid";

    this.validateMsg = "";
    this.existMsg = "已在队列";
    this.unexistMsg = "设备不存在";
    this.cantborrowMsg = "不可此分类";
    this.overquantityMsg = "达到最大数";
    this.errMsg = "操作失败";

    this.onAdded = onAdded;
}
extend(PanelBook, PanelBase);
PanelBook.prototype.checkData = function (borrnow) {
    if (!this.v_inssts_r(borrnow)) {
        return false;
    }
    if (borrnow.canborrow_c === false) {
        this.showDesc(this.cantborrowMsg, "warndesc");
        return false;
    }
    if (!borrnow.ok_c) {
        this.showDesc(this.errMsg, "warndesc");
        return false;
    }
    return true;
};
PanelBook.prototype.setData = function (data) {
    this.cur_book = data;
};
PanelBook.prototype.okData = function (borrnow) {
    this.borrnowArr.push(borrnow);
    if (this.onAdded) {
        borrnow.borrexpdt_c = this.panelReader.reader.borrexpdt_c;
        this.onAdded(borrnow);
    }
    this.panelReader.increase_quantity();
};
PanelBook.prototype.notifyNext = function () {
    $('#' + this.searchId).val('');
};
//ui
PanelBook.prototype.clear = function () {
    this.clearForm();
    this.clearDesc();
    this.clearWarn(this.cur_book);
    this.cur_book = null;
};
PanelBook.prototype.reset = function () {
    this.clear();
    this.borrnowArr = [];
    $('#' + this.searchId).val('');
    $('#' + this.searchId).attr({ disabled: "disabled" });
};
PanelBook.prototype.prepare = function () {
    $('#' + this.searchId).removeAttr("disabled");
    $('#' + this.searchId).val('');
    $('#' + this.searchId).focus();
};
PanelBook.prototype.postBorrnow = function (bookinsid) {
    this.clear();
    if (!this.panelReader.reader)
        return;
    var reader = this.panelReader.reader;
    if (reader.quantity >= reader.typquantity) {
        this.showDesc(this.overquantityMsg, "warndesc");
        return;
    }
    var exist = Array.find(this.borrnowArr, function (b) {
        return b.bookinsid == bookinsid;
    });
    if (exist) {
        this.showDesc(this.existMsg, "warndesc");
        return;
    }
    this.xhrData('/borrow/borrow', 'POST', { act: 'borrow', readercardno: this.panelReader.reader.readercardno, bookinsid: bookinsid });
};



