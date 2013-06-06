#coding:utf-8
import unittest
import datetime
import sys

sys.path.append(r"F:\eclipsWorkSpace\pylibrary")
#sys.path.append(r"D:\eclipseWorkSpace\pylibrary")

from logic import fn_db, model_giveback

class ModelGivebackTest2(unittest.TestCase):
    def setUp(self):
        pass

    def prepare(self):
        fn_db.ins("LIM_READERCARD", readercardno = "T_C02", readerid = "T_R02",
                   cardsts = "0", expdt = datetime.datetime.strptime("2099-01-01", "%Y-%m-%d"))

        fn_db.ins("LIM_READER", readerid = "T_R02", readername = "ZYX2",
                   readercardno = "T_C02", readertypcd = "T_TYP1", orgcd = 'MD',
                   gender = 'F', quantity = 30, deposit = 100.0)

        fn_db.ins("LIC_READERTYP", readertypcd = "T_TYP1", typname = 'NORMAL',
                   typquantity = 50, typdtlimit = 10, typoverprice = 0.28,
                   typdeposit = 100.0, typborrcat = "A1,A2", typrenewtimes = 1,
                   typrenewterm = 5, typlostpay = 2.0)

        fn_db.ins("LIM_BOOKCLS", bookclsid = "T_BC5", bookname = u"血压计",
                   isbn = '9781234567123', auth = 'auth1', pubcd = 'P1',
                   price = 23.6, catcd = "A2")
        fn_db.ins("LIM_BOOKCLS", bookclsid = "T_BC6", bookname = u"血糖仪",
                   isbn = '9781234567124', auth = 'auth1', pubcd = 'P2',
                   price = 53.6, catcd = "A1")

        fn_db.ins("LIM_BOOKINS", bookinsid = "T_BI5", bookclsid = "T_BC5",
                  inssts = "1", placecd = "P1", readerid = "T_R02")
        fn_db.ins("LIM_BOOKINS", bookinsid = "T_BI6", bookclsid = "T_BC6",
                  inssts = "1", placecd = "P1", readerid = "T_R02")
        fn_db.ins("LIM_BOOKINS", bookinsid = "T_BI7", bookclsid = "T_BC5",
                  inssts = "1", placecd = "P1", readerid = "T_R02")
        fn_db.ins("LIM_BOOKINS", bookinsid = "T_BI8", bookclsid = "T_BC6",
                  inssts = "1", placecd = "P1", readerid = "T_R02")
        fn_db.ins("LIM_BOOKINS", bookinsid = "T_BI9", bookclsid = "T_BC5",
                  inssts = "1", placecd = "P1", readerid = "T_R02")

        fn_db.ins("LIT_BORRNOW", readerid = "T_R_NO", readercardno = "T_C_NO",
                  bookinsid = "T_BI_NO", renewtimes = 1, 
                  borrdt = datetime.datetime.strptime("2001-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.strptime("2001-01-01", "%Y-%m-%d")
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI7", renewtimes = 1, 
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.strptime("2012-03-01", "%Y-%m-%d")
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI8", renewtimes = 1, 
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.strptime("2012-03-11", "%Y-%m-%d")
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI9", renewtimes = 1, 
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now()
                  )


    def get_borrnow(self):
        model = model_giveback.ModelGiveback()
        self.assertFalse(model.giveback("operator", "NO"))

        self.assertFalse(model.giveback("operator", "T_BI_NO"))
        self.assertNotEqual(model.borrnow, None)

    def get_bookins(self):
        fn_db.ins("LIT_BORRNOW", readerid = "T_R_NO", readercardno = "T_C_NO",
                  bookinsid = "T_BI5", renewtimes = 1
                  )
        model = model_giveback.ModelGiveback()
        self.assertFalse(model.giveback("operator", "T_BI5"))
        self.assertNotEqual(model.bookins, None)

    def pregiveback_notover(self):
        fn_db.delete("LIT_BORRNOW", "bookinsid", "T_BI5")
        self.overdays = 10
        self.borrdt = datetime.datetime.now()
        self.borrexpdt = datetime.datetime.now() + datetime.timedelta(days = self.overdays)
        fn_db.delete("LIT_BORRNOW", "bookinsid", "T_BI5")
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI5", renewtimes = 1, 
                  borrdt = self.borrdt,
                  borrexpdt = self.borrexpdt
                  )

    def giveback_notover(self):
        model = model_giveback.ModelGiveback()
        self.assertTrue(model.giveback("operator", "T_BI5"))

    def postgiveback_notover(self):
        self.assertEqual(fn_db.get("LIT_BORRNOW", "bookinsid", "T_BI5"), None)
        borrhis = fn_db.get("LIT_BORRHIS", "bookinsid", "T_BI5")
        self.assertEqual(borrhis.readerid, "T_R02")
        self.assertEqual(borrhis.readercardno, "T_C02")
        self.assertEqual(borrhis.bookinsid, "T_BI5")
        self.assertEqual(borrhis.renewtimes, 1)
        self.assertEqual(borrhis.borrdt, self.borrdt)
        self.assertEqual(borrhis.borrexpdt, self.borrexpdt)
        self.assertEqual(borrhis.overdays, 0 - self.overdays)
        self.assertEqual(borrhis.overprice, 0)
        self.assertEqual(borrhis.retdt.date(), datetime.datetime.now().date())

        bookins = fn_db.get("LIM_BOOKINS", "bookinsid", "T_BI5")
        self.assertEqual(bookins.inssts, "0")
        self.assertEqual(bookins.readerid, "")

        reader = fn_db.get("LIM_READER", "readerid", "T_R02")
        self.assertEqual(reader.quantity, 29)


    def pregiveback_over(self):
        self.overdays2 = 18
        self.borrdt2 = datetime.datetime.now() - datetime.timedelta(days = 30)
        self.borrexpdt2 = datetime.datetime.now() - datetime.timedelta(days = self.overdays2)
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI6", renewtimes = 1, 
                  borrdt = self.borrdt2,
                  borrexpdt = self.borrexpdt2
                  )

    def giveback_over(self):
        model = model_giveback.ModelGiveback()
        self.assertTrue(model.giveback("operator", "T_BI6"))

    def postgiveback_over(self):
        self.assertEqual(fn_db.get("LIT_BORRNOW", "bookinsid", "T_BI6"), None)
        borrhis = fn_db.get("LIT_BORRHIS", "bookinsid", "T_BI6")
        self.assertEqual(borrhis.overdays, self.overdays2)
        self.assertEqual(borrhis.overprice, self.overdays2 * 0.28)

        bookins = fn_db.get("LIM_BOOKINS", "bookinsid", "T_BI6")
        self.assertEqual(bookins.inssts, "0")
        self.assertEqual(bookins.readerid, "")

        reader = fn_db.get("LIM_READER", "readerid", "T_R02")
        self.assertEqual(reader.quantity, 28)

    def overdue_cash(self):
        fn_db.db.delete("LIT_BORRLOG", where = "borrhisid='T_HIS_overdue_cash'")
        kw = dict(borrhisid = "T_HIS_overdue_cash",
                  insby = "operator",
                  updby = "operator",
                  readerid = "T_R02",
                  readercardno = "T_C02",
                  bookinsid = "T_BI1",
                  overprice = 12.5)
        fn_db.ins("LIT_BORRHIS", **kw)
        model = model_giveback.ModelGiveback()

        model.overdue("operator2", "T_HIS_overdue_cash", "CASH")
        borrhis = model.get_borrhis("T_HIS_overdue_cash")
        self.assertEqual(borrhis.overprice, 12.5)
        self.assertEqual(borrhis.overpaycd, "CASH")
        log = fn_db.db.select("LIT_BORRLOG", where = "borrhisid='T_HIS_overdue_cash' and actcd='OVERDUE'")[0]        
        self.assertEqual(log.paycd, "CASH")
        self.assertEqual(log.actval, 12.5)

    def overdue_acc(self):
        fn_db.db.delete("LIT_BORRLOG", where = "borrhisid='T_HIS_overdue_acc'")
        kw = dict(borrhisid = "T_HIS_overdue_acc",
                  insby = "operator",
                  updby = "operator",
                  readerid = "T_R02",
                  readercardno = "T_C02",
                  bookinsid = "T_BI1",
                  overprice = 12.5)
        fn_db.ins("LIT_BORRHIS", **kw)
        fn_db.upd("LIM_READER", "readerid", "T_R02", deposit = 100)
        model = model_giveback.ModelGiveback()
        
        model.overdue("operator2", "T_HIS_overdue_acc", "ACC")
        self.assertEqual(fn_db.get("LIM_READER", "readerid", "T_R02").deposit, 100 - 12.5)
        borrhis = model.get_borrhis("T_HIS_overdue_acc")        
        self.assertEqual(borrhis.overprice, 12.5)
        self.assertEqual(borrhis.overpaycd, "ACC")
        log = fn_db.db.select("LIT_BORRLOG", where = "borrhisid='T_HIS_overdue_acc' and actcd='OVERDUE'")[0]
        self.assertEqual(log.paycd, "ACC")
        self.assertEqual(log.actval, 12.5)


    def deface_cash(self):
        fn_db.db.delete("LIT_BORRLOG", where = "borrhisid='T_HIS_deface_cash'")
        kw = dict(borrhisid = "T_HIS_deface_cash",
                  insby = "operator",
                  updby = "operator",
                  readerid = "T_R02",
                  readercardno = "T_C02",
                  bookinsid = "T_BI1")
        fn_db.ins("LIT_BORRHIS", **kw)
        model = model_giveback.ModelGiveback()

        model.deface("operator2", "T_HIS_deface_cash", 12.5, "CASH", "NOTE")
        borrhis = model.get_borrhis("T_HIS_deface_cash")
        self.assertEqual(borrhis.defaceprice, 12.5)
        self.assertEqual(borrhis.defacepaycd, "CASH")
        self.assertEqual(borrhis.defacenote, "NOTE")
        log = fn_db.db.select("LIT_BORRLOG", where = "borrhisid='T_HIS_deface_cash' and actcd='DEFACE'")[0]
        self.assertEqual(log.paycd, "CASH")
        self.assertEqual(log.actval, 12.5)


    def deface_acc(self):
        fn_db.db.delete("LIT_BORRLOG", where = "borrhisid='T_HIS_deface_acc'")
        kw = dict(borrhisid = "T_HIS_deface_acc",
                  insby = "operator",
                  updby = "operator",
                  readerid = "T_R02",
                  readercardno = "T_C02",
                  bookinsid = "T_BI1")
        fn_db.ins("LIT_BORRHIS", **kw)
        fn_db.upd("LIM_READER", "readerid", "T_R02", deposit = 100)
        model = model_giveback.ModelGiveback()

        model.deface("operator2", "T_HIS_deface_acc", 12.5, "ACC", "NOTE")
        self.assertEqual(fn_db.get("LIM_READER", "readerid", "T_R02").deposit, 100 - 12.5)
        borrhis = model.get_borrhis("T_HIS_deface_acc")
        self.assertEqual(borrhis.defaceprice, 12.5)
        self.assertEqual(borrhis.defacepaycd, "ACC")
        self.assertEqual(borrhis.defacenote, "NOTE")
        log = fn_db.db.select("LIT_BORRLOG", where = "borrhisid='T_HIS_deface_acc' and actcd='DEFACE'")[0]
        self.assertEqual(log.paycd, "ACC")
        self.assertEqual(log.actval, 12.5)

    def test_model(self):
        self.clear()
        self.prepare()
        self.get_borrnow()
        self.get_bookins()

        self.pregiveback_notover()
#        self.giveback_notover()
#        self.postgiveback_notover()

        self.pregiveback_over()
#        self.giveback_over()
#        self.postgiveback_over()
#
#        self.overdue_cash()
#        self.overdue_acc()
#
#        self.deface_cash()
#        self.deface_acc()

    def clear(self):
        fn_db.deleteTest()

    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelGivebackTest2)
    unittest.TextTestRunner(verbosity = 2).run(suite)
