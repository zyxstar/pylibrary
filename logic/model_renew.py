#coding:utf-8
import datetime
import web
import op_reader
import op_book
import op_borrow
from model_base import ModelBase
from model_giveback import ModelGiveback
from model_lost import ModelLost

class ModelRenew(ModelBase):
    def check_borrexp(self, borrnow):
        return borrnow.borrexpdt.date() >= datetime.datetime.now().date()

    def check_renewtimes(self, borrnow, reader):
        return  borrnow.renewtimes < reader.typrenewtimes

    def ui_reader(self, readercardno):
        reader = self.get_reader(readercardno)
        if not reader: return
        op_reader.bind_ref(reader)

        borrnowArr = []
        for b in self.query_borrnow2(reader.readerid):
            op_book.bind_ref(b)
            b.notborrexp_c = self.check_borrexp(b)
            b.renewtimes_c = self.check_renewtimes(b, reader)

            give = ModelGiveback()
            b.overdays_c = give.calc_overdays(b)
            b.typoverprice_c = reader.typoverprice
            b.overprice_c = give.calc_overprice(b.overdays_c, reader)

            lost = ModelLost()
            b.typlostpay_c = reader.typlostpay
            b.lostprice_c = lost.calc_lostprice(b, reader)
            b.sumprice_c = b.overprice_c + b.lostprice_c

            borrnowArr.append(b)

        reader.borrnowArr = borrnowArr
        return reader

    def post_renew(self, operator, bookinsid, newexpdt, renewtimes):
        op_borrow.renew(operator, bookinsid, newexpdt, renewtimes)

    def renew(self, operator, bookinsid, bookclsid = None, bookname = None):
        borrnow = self.get_borrnow(bookinsid)
        if not borrnow: return False
        if not self.check_borrexp(borrnow): return False

        reader = self.get_reader(borrnow.readercardno)
        if not reader: return False
        if not self.check_renewtimes(borrnow, reader): return False

        self.newexpdt = borrnow.borrexpdt + datetime.timedelta(days = reader.typrenewterm)
        self.renewtimes = borrnow.renewtimes + 1
        self.post_renew(operator, bookinsid, self.newexpdt, self.renewtimes)
        self.log(insby = operator,
                 readercardno = borrnow.readercardno,
                 readerid = borrnow.readerid,
                 readername = reader.readername,
                 bookclsid = bookclsid,
                 bookinsid = bookinsid,
                 bookname = bookname,
                 actcd = 'RENEW',
                 actval = self.renewtimes)
        return True

    def ui_renew(self, operator, bookinsid, bookclsid = None, bookname = None):
        ret = web.Storage()
        if self.renew(operator, bookinsid, bookclsid, bookname):
            ret.newexpdt = self.newexpdt
            ret.renewtimes = self.renewtimes

        return ret









