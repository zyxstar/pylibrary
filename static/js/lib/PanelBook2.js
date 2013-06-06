function PanelBook2(onAdded) {
    PanelBook2.superclass.constructor.call(this, null);
    this.borrhisArr = [];
    complib.fixDescsWarn(this.descs);
    this.onAdded = onAdded;
}
extend(PanelBook2, PanelBook);
PanelBook2.prototype.checkData = function (borrhis) {
    if (!borrhis.ok_c) {
        this.showDesc(this.errMsg, "warndesc");
        return false;
    }
    return true;
};
PanelBook2.prototype.okData = function (borrhis) {
    this.borrhisArr.push(borrhis);
    if (this.onAdded) {
        this.onAdded(borrhis);
    }
};
//ui
PanelBook2.prototype.postBorrhis = function (bookinsid) {
    this.clear();
    var exist = Array.find(this.borrhisArr, function (b) {
        return b.bookinsid == bookinsid;
    });
    if (exist) {
        this.showDesc(this.existMsg, "warndesc");
        return;
    }
    this.xhrData('/borrow/giveback', 'POST', { act: 'giveback', bookinsid: bookinsid });
};

