#coding:utf-8
import datetime
import web
import op_reader
import op_book
import op_borrow
import uuid
from model_base import ModelBase

class ModelGiveback(ModelBase):
    def calc_overprice(self, overdays, reader):
        if overdays > 0:
            return overdays * reader.typoverprice
        return 0

    def calc_overdays(self, borrnow):
        expdt = borrnow.borrexpdt.date()
        today = datetime.datetime.now().date()
        return (today - expdt).days

    def post_giveback(self, operator, borrhisid, borrnow, overdays, overprice):
        op_borrow.giveback(operator, borrhisid, borrnow, overdays, overprice)

    def giveback(self, operator, bookinsid):
        borrnow = self.get_borrnow(bookinsid)
        if not borrnow: return False
        self.borrnow = borrnow

        bookins = self.get_bookins(borrnow.bookinsid)
        if not bookins: return False
        self.bookins = bookins

        reader = self.get_reader(borrnow.readercardno)
        if not reader: return False
        self.reader = reader

        self.borrhisid = str(uuid.uuid1())
        self.overdays = self.calc_overdays(borrnow)
        self.overprice = self.calc_overprice(self.overdays, reader)
        self.post_giveback(operator, self.borrhisid, borrnow, self.overdays, self.overprice)
        self.log(insby = operator,
                 borrhisid = self.borrhisid,
                 readercardno = borrnow.readercardno,
                 readerid = borrnow.readerid,
                 readername = reader.readername,
                 bookclsid = bookins.bookclsid,
                 bookinsid = borrnow.bookinsid, 
                 bookname = bookins.bookname,
                 actcd = 'GIVEBACK')
        return True

    def ui_giveback(self, operator, bookinsid):
        ret = web.Storage()
        if self.giveback(operator, bookinsid):
            ret.ok_c = True
            ret.borrhisid = self.borrhisid
            ret.overdays = self.overdays
            ret.overprice = self.overprice

        if hasattr(self, "bookins"):
            op_book.bind_ref(self.bookins)
            ret.update(self.bookins)
        if hasattr(self, "reader"):
            op_reader.bind_ref(self.reader)
            ret.update(self.reader)
        if hasattr(self, "borrnow"):
            ret.update(self.borrnow)

        return ret

    def overdue(self, operator, borrhisid, paycd, 
                readername = None, bookclsid = None, bookname = None):
        borrhis = self.get_borrhis(borrhisid)
        if not borrhis: return

        op_borrow.overdue(borrhis.readerid, borrhisid, borrhis.overprice, paycd)
        self.log(insby = operator,
                 borrhisid = borrhisid,
                 readercardno = borrhis.readercardno,
                 readerid = borrhis.readerid,
                 readername = readername,
                 bookclsid = bookclsid,
                 bookinsid = borrhis.bookinsid,
                 bookname = bookname,
                 actcd = 'OVERDUE',
                 actval = borrhis.overprice,
                 paycd = paycd)

    def deface(self, operator, borrhisid, price, paycd, note, 
               readername = None, bookclsid = None, bookname = None):
        borrhis = self.get_borrhis(borrhisid)
        if not borrhis: return

        op_borrow.deface(borrhis.readerid, borrhisid, price, paycd, note)
        self.log(insby = operator,
                 borrhisid = borrhisid,
                 readercardno = borrhis.readercardno,
                 readerid = borrhis.readerid,
                 readername = readername,
                 bookinsid = borrhis.bookinsid,
                 bookclsid = bookclsid,                 
                 bookname = bookname,
                 actcd = 'DEFACE',
                 actval = price,
                 paycd = paycd)



