#coding:utf-8
import datetime
import fn_db
import op_reader

def log(**kw):
    kw['insdt'] = datetime.datetime.now()
    try:
        fn_db.db.insert('LIT_BORRLOG', **kw)
    except:
        pass

def query_borrnow(readerid):
    return fn_db.db.select("LIT_BORRNOW", where = "readerid=$readerid", vars = locals())

def query_borrnow2(readerid):
    return fn_db.db.query("""
        SELECT a.*, b.*, c.*
          FROM LIT_BORRNOW a LEFT JOIN LIM_BOOKINS b ON a.bookinsid = b.bookinsid
               LEFT JOIN LIM_BOOKCLS c ON b.bookclsid = c.bookclsid
         WHERE a.readerid = $readerid
        """, vars = locals())

def borrow(operator, readercardno, readerid, bookinsid, typdtlimit):
    with fn_db.db.transaction():
        kw = dict(readerid = readerid,
                  readercardno = readercardno,
                  insby = operator,
                  updby = operator,
                  bookinsid = bookinsid,
                  borrdt = datetime.datetime.now(),
                  borrexpdt = datetime.datetime.now() + datetime.timedelta(days = typdtlimit),
                  renewtimes = 0)
        fn_db.ins('LIT_BORRNOW', **kw)
        fn_db.increase("LIM_READER", "readerid", readerid, 'quantity', 1)
        fn_db.upd("LIM_BOOKINS", "bookinsid", bookinsid, inssts = "1", readerid = readerid)

def giveback(operator, borrhisid, borrnow, overdays, overprice):
    with fn_db.db.transaction():
        kw = dict(borrhisid = borrhisid,
                  insby = operator,
                  updby = operator,
                  readerid = borrnow.readerid,
                  readercardno = borrnow.readercardno,
                  bookinsid = borrnow.bookinsid,
                  borrdt = borrnow.borrdt,
                  borrexpdt = borrnow.borrexpdt,
                  overdays = overdays,
                  renewtimes = borrnow.renewtimes,
                  retdt = datetime.datetime.now(),
                  overprice = overprice)
        fn_db.ins("LIT_BORRHIS", **kw)
        fn_db.delete('LIT_BORRNOW', "bookinsid", borrnow.bookinsid)
        fn_db.decrease("LIM_READER", "readerid", borrnow.readerid, 'quantity', 1)
        fn_db.upd("LIM_BOOKINS", "bookinsid", borrnow.bookinsid, inssts = "0", readerid = "")

def overdue(readerid, borrhisid, overprice, paycd):
    with fn_db.db.transaction():
        if paycd == 'ACC':
            op_reader.decreaseAcc(readerid, overprice)
        fn_db.upd("LIT_BORRHIS", "borrhisid", borrhisid, overpaycd = paycd)

def deface(readerid, borrhisid, defaceprice, paycd, note):
    with fn_db.db.transaction():
        if paycd == 'ACC':
            op_reader.decreaseAcc(readerid, defaceprice)
        fn_db.upd("LIT_BORRHIS", "borrhisid", borrhisid, defaceprice = defaceprice, defacepaycd = paycd , defacenote = note)

def renew(operator, bookinsid, newexpdt, renewtimes):
    fn_db.upd('LIT_BORRNOW', "bookinsid", bookinsid, borrexpdt = newexpdt, renewtimes = renewtimes)

def lost(readerid, borrhisid, bookinsid, lostprice, paycd, note):
    with fn_db.db.transaction():
        if paycd == 'ACC':
            op_reader.decreaseAcc(readerid, lostprice)
        fn_db.upd("LIT_BORRHIS", "borrhisid", borrhisid, lostprice = lostprice, lostpaycd = paycd, lostnote = note)
        fn_db.upd("LIM_BOOKINS", "bookinsid", bookinsid, inssts = "2", readerid = readerid)

