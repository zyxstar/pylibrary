#coding:utf-8
import fn_db
import op_reader
import op_book
import op_borrow

class ModelBase():
    def get_reader(self, readercardno):
        return op_reader.get_reader_join(readercardno)

    def get_bookins(self, bookinsid):
        return op_book.get_bookins_join(bookinsid)

    def get_borrnow(self, bookinsid):
        return fn_db.get("LIT_BORRNOW", "bookinsid", bookinsid)

    def get_borrhis(self, borrhisid):
        return fn_db.get("LIT_BORRHIS", "borrhisid", borrhisid)

    def query_borrnow(self, readerid):
        return op_borrow.query_borrnow(readerid)

    def query_borrnow2(self, readerid):
        return op_borrow.query_borrnow2(readerid)

    def log(self, **kw):
        op_borrow.log(**kw)

