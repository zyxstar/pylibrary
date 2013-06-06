#coding:utf-8
import web
from utils import BaseHandler, jsonOut, onlyPost, render
from logic import model_borrow, model_giveback, model_renew, model_lost

urls = ('', 'borrow',
        '/borrow', 'borrow',
        '/giveback', 'giveback',
        '/renew', 'renew',
        '/lost', 'lost',
        )

class borrow(BaseHandler):
    def entry(self):
        return render("borrow.html")

    def model(self):
        return model_borrow.ModelBorrow()

    @jsonOut
    def reader(self):
        return self.model().ui_reader(self.q.readercardno)

    @jsonOut
    @onlyPost
    def borrow(self):
        return self.model().ui_borrow(self.o, self.q.readercardno, self.q.bookinsid)


class giveback(BaseHandler):
    def entry(self):
        return render("giveback.html")

    def model(self):
        return model_giveback.ModelGiveback()

    @jsonOut
    @onlyPost
    def giveback(self):
        return self.model().ui_giveback(self.o, self.q.bookinsid)

    @jsonOut
    @onlyPost
    def overdue(self):
        self.model().overdue(self.o, self.q.borrhisid, self.q.paycd.upper(),
                             self.q.readername, self.q.bookclsid, self.q.bookname)

    @jsonOut
    @onlyPost
    def deface(self):
        price = float(self.q.price)
        if price < 0:return
        self.model().deface(self.o, self.q.borrhisid, price, self.q.paycd.upper(), self.q.note,
                            self.q.readername, self.q.bookclsid, self.q.bookname)


class renew(BaseHandler):
    def entry(self):
        return render("renew.html")

    def model(self):
        return model_renew.ModelRenew()

    @jsonOut
    def reader(self):
        return self.model().ui_reader(self.q.readercardno)

    @jsonOut
    @onlyPost
    def renew(self):
        return self.model().ui_renew(self.o, self.q.bookinsid, self.q.bookclsid, self.q.bookname)

class lost(BaseHandler):
    def entry(self):
        return render("lost.html")

    def dialog(self):
        return render("dialog.html", file = "lost_2.html")

    @jsonOut
    @onlyPost
    def lost(self):
        return model_lost.ModelLost().lost(self.o, self.q.bookinsid, self.q.paycd.upper(), self.q.note)


app = web.application(urls, globals())
