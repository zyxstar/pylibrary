#coding:utf-8
import op_borrow
from model_base import ModelBase
from model_giveback import ModelGiveback

class ModelLost(ModelBase):
    def calc_lostprice(self, bookins, reader):
        return bookins.price * reader.typlostpay

    def post_lost(self, operator, borrhisid,
             readercardno, readerid, readername,
             bookclsid, bookinsid, bookname,
             lostprice, paycd, note):
        op_borrow.lost(readerid, borrhisid, bookinsid, lostprice, paycd, note)
        self.log(insby = operator,
                 borrhisid = borrhisid,
                 readercardno = readercardno,
                 readerid = readerid,
                 readername = readername,
                 bookclsid = bookclsid,
                 bookinsid = bookinsid,
                 bookname = bookname,
                 actcd = 'LOST',
                 actval = lostprice,
                 paycd = paycd)

    def lost(self, operator, bookinsid, paycd, note):
        give = ModelGiveback()
        if give.giveback(operator, bookinsid):
            reader = give.reader
            bookins = give.bookins
            borrhisid = give.borrhisid

            if give.overprice > 0:
                give.overdue(operator, borrhisid, paycd,
                             reader.readername, bookins.bookclsid, bookins.bookname)

            self.post_lost(operator, borrhisid,
                      reader.readercardno, reader.readerid, reader.readername,
                      bookins.bookclsid, bookins.bookinsid, bookins.bookname,
                      self.calc_lostprice(bookins, reader), paycd, note)

