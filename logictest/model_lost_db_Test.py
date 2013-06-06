#coding:utf-8
import unittest
import datetime
import sys

sys.path.append(r"F:\eclipsWorkSpace\pylibrary")
#sys.path.append(r"D:\eclipseWorkSpace\pylibrary")

from logic import fn_db, model_lost

class ModelLostTest(unittest.TestCase):
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


        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02", #over
                  bookinsid = "T_BI5", renewtimes = 0,
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() - datetime.timedelta(days = 2)
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI6", renewtimes = 1,
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() - datetime.timedelta(days = 2)
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI7", renewtimes = 0,
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() + datetime.timedelta(days = 2)
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI8", renewtimes = 1,
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() + datetime.timedelta(days = 2)
                  )

    def pre_lost_over_cash(self):
        pass

    def lost_over_cash(self):
        model = model_lost.ModelLost()
        model.lost("operator", "T_BI5", "CASH", "note")

    def post_lost_over_cash(self):
        borrhis = fn_db.get("LIT_BORRHIS", "bookinsid", "T_BI5")
        self.assertEqual(borrhis.overdays, 2)
        self.assertEqual(borrhis.overprice, 2 * 0.28)
        self.assertEqual(borrhis.lostprice, 23.6 * 2.0)
        self.assertEqual(borrhis.overpaycd, "CASH")
        self.assertEqual(borrhis.lostpaycd, "CASH")
        self.assertEqual(borrhis.lostnote, "note")

        self.assertTrue(any(fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI5' and actcd='GIVEBACK'")))

        log2 = fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI5' and actcd='OVERDUE'")[0]
        self.assertEqual(log2.actval, 2 * 0.28)
        self.assertEqual(log2.paycd, "CASH")

        log3 = fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI5' and actcd='LOST'")[0]
        self.assertEqual(log3.actval, 23.6 * 2.0)
        self.assertEqual(log3.paycd, "CASH")

    def pre_lost_over_acc(self):
        fn_db.upd("LIM_READER", "readerid", "T_R02", deposit = 100)

    def lost_over_acc(self):
        model = model_lost.ModelLost()
        model.lost("operator", "T_BI6", "ACC", "note")


    def post_lost_over_acc(self):
        borrhis = fn_db.get("LIT_BORRHIS", "bookinsid", "T_BI6")

        self.assertEqual(borrhis.overdays, 2)
        self.assertEqual(borrhis.overprice, 2 * 0.28)
        self.assertEqual(borrhis.lostprice, 53.6 * 2.0)
        self.assertEqual(borrhis.overpaycd, "ACC")
        self.assertEqual(borrhis.lostpaycd, "ACC")
        self.assertEqual(borrhis.lostnote, "note")

        self.assertTrue(any(fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI6' and actcd='GIVEBACK'")))

        log2 = fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI6' and actcd='OVERDUE'")[0]
        self.assertEqual(log2.actval, 2 * 0.28)
        self.assertEqual(log2.paycd, "ACC")

        log3 = fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI6' and actcd='LOST'")[0]
        self.assertEqual(log3.actval, 53.6 * 2.0)
        self.assertEqual(log3.paycd, "ACC")
        self.assertEqual(fn_db.get("LIM_READER", "readerid", "T_R02").deposit, 100 - 2 * 0.28 - 53.6 * 2.0)

    def pre_lost_notover_cash(self):
        pass

    def lost_notover_cash(self):
        model = model_lost.ModelLost()
        model.lost("operator", "T_BI7", "CASH", "note")


    def post_lost_notover_cash(self):
        borrhis = fn_db.get("LIT_BORRHIS", "bookinsid", "T_BI7")
        self.assertEqual(borrhis.overdays, -2)
        self.assertEqual(borrhis.overprice, 0)
        self.assertEqual(borrhis.lostprice, 23.6 * 2.0)
        self.assertEqual(borrhis.overpaycd, None)
        self.assertEqual(borrhis.lostpaycd, "CASH")
        self.assertEqual(borrhis.lostnote, "note")

        self.assertTrue(any(fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI7' and actcd='GIVEBACK'")))

        self.assertFalse(any(fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI7' and actcd='OVERDUE'")))

        log3 = fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI7' and actcd='LOST'")[0]
        self.assertEqual(log3.actval, 23.6 * 2.0)
        self.assertEqual(log3.paycd, "CASH")

    def pre_lost_notover_acc(self):
        fn_db.upd("LIM_READER", "readerid", "T_R02", deposit = 100)      
         
    def lost_notover_acc(self):
        model = model_lost.ModelLost()
        model.lost("operator", "T_BI8", "ACC", "note")

    def post_lost_notover_acc(self):
        borrhis = fn_db.get("LIT_BORRHIS", "bookinsid", "T_BI8")

        self.assertEqual(borrhis.overdays, -2)
        self.assertEqual(borrhis.overprice, 0)
        self.assertEqual(borrhis.lostprice, 53.6 * 2.0)
        self.assertEqual(borrhis.overpaycd, None)
        self.assertEqual(borrhis.lostpaycd, "ACC")
        self.assertEqual(borrhis.lostnote, "note")

        self.assertTrue(any(fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI8' and actcd='GIVEBACK'")))

        self.assertFalse(any(fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI8' and actcd='OVERDUE'")))

        log3 = fn_db.db.select("LIT_BORRLOG", where = "bookinsid='T_BI8' and actcd='LOST'")[0]
        self.assertEqual(log3.actval, 53.6 * 2.0)
        self.assertEqual(log3.paycd, "ACC")
        self.assertEqual(fn_db.get("LIM_READER", "readerid", "T_R02").deposit, 100 - 53.6 * 2.0)
        
    def test_model(self):
        self.clear()
        self.prepare()
#
#        self.pre_lost_over_cash()
#        self.lost_over_cash()
#        self.post_lost_over_cash()
#        
#        self.pre_lost_over_acc()
#        self.lost_over_acc()
#        self.post_lost_over_acc()
#        
#        self.pre_lost_notover_cash()
#        self.lost_notover_cash()
#        self.post_lost_notover_cash()
#        
#        self.pre_lost_notover_acc()
#        self.lost_notover_acc()
#        self.post_lost_notover_acc()


    def clear(self):
        fn_db.deleteTest()

    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelLostTest)
    unittest.TextTestRunner(verbosity = 2).run(suite)
