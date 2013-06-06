function PanelReader2(onAdded) {
    PanelReader2.superclass.constructor.call(this);
    complib.fixDescsWarn(this.descs);
    this.onAdded = onAdded;
}
extend(PanelReader2, PanelReader);
PanelReader2.prototype.checkData = function (reader) {
    return true;
};
PanelReader2.prototype.setData = function (reader) {
    this.reader = reader;
};
PanelReader2.prototype.okData = function (reader) {
    if (this.onAdded) {
        for (var i = 0; i < reader.borrnowArr.length; i++)
            this.onAdded(reader, reader.borrnowArr[i]);
    }
};
PanelReader2.prototype.notifyNext = function () {
    this.disabled();
};
//ui
PanelReader2.prototype.clear = function () {
    this.clearForm();
    this.clearDesc();
    this.clearWarn(this.reader);
    this.reader = null;
};
PanelReader2.prototype.decrease_acc = function (money) {
    this.reader.deposit -= money;
    var $target = $("#txt_deposit")
    $target.val(complib.moneyFormat(this.reader.deposit));
    complib.glitter($target);
};
PanelReader2.prototype.getReader = function (readercardno) {
    this.clear();
    this.xhrData('/borrow/renew', 'GET', { act: 'reader', readercardno: readercardno });
};

