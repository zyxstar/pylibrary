function borrowTest() {
    module("DataLoader");
    test("noData", function () {
        expect(2);
        var callrender = false;
        var callshowUnexist = false;
        var panel = {
            render: function () { callrender = true; },
            showUnexist: function () { callshowUnexist = true; }
        };
        var loader = new DataLoader(panel);
        loader.callback(null);
        ok(callshowUnexist);
        ok(!callrender);
    });

    test("hasData_checktrue", function () {
        expect(6);
        var callrender = false;
        var callshowUnexist = false;
        var calladd = false;
        var panel = {
            render: function (data) { equal(data, "data"); callrender = true; },
            showUnexist: function () { callshowUnexist = true; },
            checkData: function (data) { equal(data, "data"); return true; },
            add: function (data) { equal(data, "data"); calladd = true; },
            showValidate: function () { },
            notifyNext: function () { }
        };
        var loader = new DataLoader(panel);
        loader.callback("data");
        ok(callrender);
        ok(calladd);
        ok(!callshowUnexist);
    });

    test("hasData_checkfalse", function () {
        expect(5);
        var callrender = false;
        var callshowUnexist = false;
        var calladd = false;
        var panel = {
            render: function (data) { equal(data, "data"); callrender = true; },
            showUnexist: function () { callshowUnexist = true; },
            checkData: function (data) { equal(data, "data"); return false; },
            add: function (data) { calladd = true; },
            showValidate: function () { },
            notifyNext: function () { }
        };
        var loader = new DataLoader(panel);
        loader.callback("data");
        ok(callrender);
        ok(!calladd);
        ok(!callshowUnexist);
    });

    module("ReaderPanel");
    test("noData", function () {
        expect(6);
        var panel = new ReaderPanel();
        var callclearForm = false;
        var callclearWarn = false;
        var callclearDesc = false;
        var callbookreset = false;

        panel.clearForm = function () { callclearForm = true; };
        panel.clearWarn = function () { callclearWarn = true; };
        panel.clearDesc = function () { callclearDesc = true; };
        panel.showDesc = function (msg) { equal(msg, panel.unexistMsg); };
        panel.bookPanel = { reset: function () { callbookreset = true; } };

        panel.loader.getData = function () {
            panel.loader.callback(null);
        };
        panel.getReader("");

        ok(callclearForm);
        ok(callclearWarn);
        ok(callclearDesc);
        ok(callbookreset);
        equal(panel.reader, null);
    });

    test("hasData_checkfalse", function () {
        expect(5);
        var panel = new ReaderPanel();
        var desclist = [];
        var warnlist = [];
        var reader = { cardsts: "1", cardsts_r: "无效", deposit: 99,
            dtlimit: 40, dtlimit_r: "2012-04-19", expdt: "2016-03-05",
            gender: "F", gender_r: "女", hasoverdue: true,
            isexp: true, orgcd: "MD", orgcd_r: "中间带",
            quantity: 30, readercardno: "C02", readerid: "R02",
            readername: "ZZZ", readertypcd: "TYP2", typdeposit: 100,
            typname: "VIP", typquantity: 30
        };

        panel.clearForm = function () { };
        panel.clearWarn = function () { };
        panel.clearDesc = function () { };

        panel.bookPanel = { reset: function () { } };
        complib.showWarn = function (attr) {
            warnlist.push(attr);
        };
        complib.formatObj = function (data, attrs) {
            equal(data, reader);
            equal(panel.attrs, attrs);
        };
        var loader = new DataLoader(panel);
        loader.callback(reader);

        same(desclist, []);
        same(warnlist, ["cardsts_r", "expdt", "quantity",
        "deposit", "hasoverdue"]);
        equal(panel.reader, null);
    });

    test("hasData_checktrue", function () {
        expect(5);
        var panel2 = new ReaderPanel();
        var desclist = [];
        var warnlist = [];
        var reader2 = { cardsts: "0", cardsts_r: "无效", deposit: 100,
            dtlimit: 40, dtlimit_r: "2012-04-19", expdt: "2016-03-05",
            gender: "F", gender_r: "女", hasoverdue: false,
            isexp: false, orgcd: "MD", orgcd_r: "中间带",
            quantity: 20, readercardno: "C02", readerid: "R02",
            readername: "ZZZ", readertypcd: "TYP2", typdeposit: 100,
            typname: "VIP", typquantity: 30
        };

        var calldisabled = false;
        var callbookprepare = false;

        panel2.clearForm = function () { };
        panel2.clearWarn = function () { };
        panel2.clearDesc = function () { };
        panel2.render = function () { };

        panel2.bookPanel = {
            reset: function () { },
            prepare: function () { callbookprepare = true; }
        };
        complib.showWarn = function (attr) {
            warnlist.push(attr);
        };
        panel2.showDesc = function (msg) {
            desclist.push(msg);
        };
        panel2.disabled = function () {
            calldisabled = true;
        };

        var loader = new DataLoader(panel2);
        loader.callback(reader2);

        ok(calldisabled);
        ok(callbookprepare);
        same(desclist, [panel2.validateMsg]);
        same(warnlist, []);
        equal(panel2.reader, reader2);
    });

//    module("BookPanel");
//    test("noData", function () {
//        expect(5);
//        var panel = new BookPanel();
//        var callclearForm = false;
//        var callclearWarn = false;
//        var callclearDesc = false;

//        panel.clearForm = function () { callclearForm = true; };
//        panel.clearWarn = function () { callclearWarn = true; };
//        panel.clearDesc = function () { callclearDesc = true; };
//        panel.showDesc = function (msg) { equal(msg, panel.unexistMsg); };

//        var loader = new DataLoader(panel);
//        loader.callback(null);

//        ok(callclearForm);
//        ok(callclearWarn);
//        ok(callclearDesc);
//        same(panel.books, []);
//    });

//    test("hasData_checkfalse", function () {
//        expect(3);
//        var panel = new BookPanel();
//        var desclist = [];
//        var warnlist = [];
//        var book = { auth: "zyx", bookclsid: "BC1", bookinsid: "BI4",
//            bookname: "中草药", booksts: "1", booksts_r: "可借出",
//            borrdt: "2012-03-10", canborrow: false, catcd: "C1",
//            catcd_r: "CAT1", isbn: "9787115226730", placecd: "P99",
//            placecd_r: "", price: 59.6, pubcd: "P1",
//            pubcd_r: "PUB1"
//        };

//        panel.clearForm = function () { };
//        panel.clearWarn = function () { };
//        panel.clearDesc = function () { };
//        panel.render = function () { };

//        panel.readerPanel = { reader: { quantity: 1} };
//        complib.showWarn = function (attr) {
//            warnlist.push(attr);
//        };
//        panel.showDesc = function (msg) {
//            desclist.push(msg);
//        };

//        var loader = new DataLoader(panel);
//        loader.callback(book);

//        same(desclist, [panel.cantborrowMsg]);
//        same(warnlist, ["booksts_r"]);
//        same(panel.books, []);
//    });

//    test("hasData_checktrue", function () {
//        expect(6);
//        var panel = new BookPanel();
//        var desclist = [];
//        var warnlist = [];
//        var book = { auth: "zyx", bookclsid: "BC1", bookinsid: "BI4",
//            bookname: "中草药", booksts: "0", booksts_r: "可借出",
//            borrdt: "2012-03-10", canborrow: true, catcd: "C1",
//            catcd_r: "CAT1", isbn: "9787115226730", placecd: "P99",
//            placecd_r: "", price: 59.6, pubcd: "P1",
//            pubcd_r: "PUB1"
//        };

//        var callnotifynext = false;
//        panel.clearForm = function () { };
//        panel.clearWarn = function () { };
//        panel.clearDesc = function () { };
//        panel.render = function () { };
//        panel.notifyNext = function () { callnotifynext = true; };


//        panel.readerPanel = { reader: { quantity: 1, dtlimit_r: "dd"} };
//        panel.bookTable = { add: function (data, dtlimit) {
//            equal(data, book);
//            equal(dtlimit, "dd");
//        }
//        };
//        complib.showWarn = function (attr) {
//            warnlist.push(attr);
//        };
//        panel.showDesc = function (msg) {
//            desclist.push(msg);
//        };

//        var loader = new DataLoader(panel);
//        loader.callback(book);

//        ok(callnotifynext);
//        same(desclist, [panel.validateMsg]);
//        same(warnlist, []);
//        same(panel.books, [book]);
//    });

//    test("hasData_checktrue_existsamebook", function () {
//        expect(4);
//        var panel = new BookPanel();
//        var desclist = [];
//        var warnlist = [];
//        var book = { auth: "zyx", bookclsid: "BC1", bookinsid: "BI4",
//            bookname: "中草药", booksts: "0", booksts_r: "可借出",
//            borrdt: "2012-03-10", canborrow: true, catcd: "C1",
//            catcd_r: "CAT1", isbn: "9787115226730", placecd: "P99",
//            placecd_r: "", price: 59.6, pubcd: "P1",
//            pubcd_r: "PUB1"
//        };

//        var callnotifynext = false;
//        panel.clearForm = function () { };
//        panel.clearWarn = function () { };
//        panel.clearDesc = function () { };
//        panel.render = function () { };
//        panel.notifyNext = function () { callnotifynext = true; };
//        panel.bookTable = { add: function () { } };
//        panel.readerPanel = { reader: { quantity: 2} };
//        complib.showWarn = function (attr) {
//            warnlist.push(attr);
//        };
//        panel.showDesc = function (msg) {
//            desclist.push(msg);
//        };

//        var loader = new DataLoader(panel);
//        loader.callback(book);
//        loader.callback(book);

//        ok(callnotifynext);
//        same(desclist, [panel.validateMsg, panel.existMsg]);
//        same(warnlist, []);
//        same(panel.books, [book]);
//    });

//    test("hasData_checktrue_overquantity", function () {
//        expect(6);
//        var panel = new BookPanel();
//        var desclist = [];
//        var warnlist = [];
//        var book = { auth: "zyx", bookclsid: "BC1", bookinsid: "BI4",
//            bookname: "中草药", booksts: "0", booksts_r: "可借出",
//            borrdt: "2012-03-10", canborrow: true, catcd: "C1",
//            catcd_r: "CAT1", isbn: "9787115226730", placecd: "P99",
//            placecd_r: "", price: 59.6, pubcd: "P1",
//            pubcd_r: "PUB1"
//        };

//        var book2 = { auth: "zyx", bookclsid: "BC1", bookinsid: "BI5",
//            bookname: "中草药", booksts: "0", booksts_r: "可借出",
//            borrdt: "2012-03-10", canborrow: true, catcd: "C1",
//            catcd_r: "CAT1", isbn: "9787115226730", placecd: "P99",
//            placecd_r: "", price: 59.6, pubcd: "P1",
//            pubcd_r: "PUB1"
//        };

//        var callnotifynext = false;
//        panel.clearForm = function () { };
//        panel.clearWarn = function () { };
//        panel.clearDesc = function () { };
//        panel.render = function () { };
//        panel.bookTable = { add: function () { } };
//        panel.notifyNext = function () { callnotifynext = true; };

//        panel.readerPanel = { reader: { quantity: 2} };
//        complib.showWarn = function (attr) {
//            warnlist.push(attr);
//        };
//        panel.showDesc = function (msg) {
//            desclist.push(msg);
//        };

//        var loader = new DataLoader(panel);
//        loader.callback(book);
//        loader.callback(book2);

//        ok(callnotifynext);
//        same(desclist, [panel.validateMsg, panel.validateMsg]);
//        same(warnlist, []);
//        same(panel.books, [book, book2]);

//        loader.callback(book);
//        same(desclist, [panel.validateMsg, panel.validateMsg, panel.overquantityMsg]);
//        same(panel.books, [book, book2]);
//    });

}