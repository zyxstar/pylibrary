#coding:utf-8
import datetime
import web
import op_reader
import op_book
import op_borrow
from model_base import ModelBase

class ModelBorrow(ModelBase):
    def post_borrow(self, operator, readercardno, readerid , bookinsid, typdtlimit):
        op_borrow.borrow(operator, readercardno, readerid , bookinsid, typdtlimit)

    def check_readercard(self, reader):
        if reader.cardsts != '0':
            return False
        if reader.expdt.date() < datetime.datetime.now().date():
            return False
        return True

    def check_reader(self, reader):
        if reader.quantity >= reader.typquantity:
            return False
        if reader.deposit < reader.typdeposit:
            return False
        return True

    def check_overdue(self, reader):
        query = self.query_borrnow(reader.readerid)
        return any([item.borrexpdt.date() < datetime.datetime.now().date() for item in query])

    def check_book(self, bookins):
        return bookins.inssts == '0'

    def check_borrcat(self, reader, bookins):
        return op_reader.can_borrow(reader.typborrcat, bookins.catcd)

    def borrow(self, operator, readercardno, bookinsid):
        reader = self.get_reader(readercardno)
        if not reader:return False
        self.reader = reader
        if not self.check_readercard(reader):return False
        if not self.check_reader(reader):return False
        if self.check_overdue(reader):return False

        bookins = self.get_bookins(bookinsid)
        if not bookins:return False
        self.bookins = bookins
        if not self.check_book(bookins):return False

        self.canborrow = self.check_borrcat(reader, bookins)
        if not self.canborrow: return False

        self.post_borrow(operator, readercardno, reader.readerid, bookinsid, reader.typdtlimit)
        self.log(insby = operator,
                 readercardno = readercardno,
                 readerid = reader.readerid,
                 readername = reader.readername,
                 bookclsid = bookins.bookclsid,
                 bookinsid = bookinsid,                 
                 bookname = bookins.bookname,
                 actcd = 'BORROW')
        return True

    def ui_reader(self, readercardno):
        reader = self.get_reader(readercardno)
        if not reader: return
        op_reader.bind_ref(reader)
        reader.isexp_c = reader.expdt.date() < datetime.datetime.now().date()
        reader.borrexpdt_c = datetime.datetime.now() + datetime.timedelta(days = reader.typdtlimit)
        reader.hasoverdue_c = self.check_overdue(reader)
        return reader

    def ui_borrow(self, operator, readercardno, bookinsid):
        ret = web.Storage()
        if self.borrow(operator, readercardno, bookinsid):
            ret.ok_c = True
            ret.borrdt = datetime.datetime.now()
            
        if hasattr(self, "bookins"):
            op_book.bind_ref(self.bookins)
            ret.update(self.bookins)
        if hasattr(self, "canborrow"):
            ret.canborrow_c = self.canborrow
            
        return ret






