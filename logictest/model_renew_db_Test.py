#coding:utf-8
import unittest
import datetime
import sys

sys.path.append(r"F:\eclipsWorkSpace\pylibrary")
#sys.path.append(r"D:\eclipseWorkSpace\pylibrary")

from logic import fn_db, model_renew

class ModelRenewTest2(unittest.TestCase):
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
        fn_db.ins("LIM_BOOKINS", bookinsid = "T_BI10", bookclsid = "T_BC6",
                  inssts = "1", placecd = "P1", readerid = "T_R02")
        
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI5", renewtimes = 0, 
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() - datetime.timedelta(days = 1)
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI6", renewtimes = 1, 
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() - datetime.timedelta(days = 1)
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI7", renewtimes = 0,
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() + datetime.timedelta(days = 1)
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI8", renewtimes = 1, 
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() + datetime.timedelta(days = 1)
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI9", renewtimes = 0, 
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now() + datetime.timedelta(days = 1)
                  )
        fn_db.ins("LIT_BORRNOW", readerid = "T_R02", readercardno = "T_C02",
                  bookinsid = "T_BI10", renewtimes = 0, 
                  borrdt = datetime.datetime.strptime("2012-01-01", "%Y-%m-%d"),
                  borrexpdt = datetime.datetime.now()
                  )
        
    def ui_reader(self):
        model = model_renew.ModelRenew()        
        print model.ui_reader("T_C02")

    def renew(self):
        model = model_renew.ModelRenew()
        self.assertFalse(model.renew("operator", "T_BI6"))
        self.assertFalse(model.renew("operator", "T_BI7"))
        self.assertFalse(model.renew("operator", "T_BI8"))
        
        self.assertTrue(model.renew("operator", "T_BI5"))
        borrnow=model.get_borrnow("T_BI5")
        self.assertEqual(borrnow.renewtimes, 1)
        self.assertEqual(borrnow.borrexpdt.date(), (datetime.datetime.now() + datetime.timedelta(days = 4)).date())
                
    def test_model(self):
        self.clear()
        self.prepare()
        self.ui_reader()
#        self.renew()

    def clear(self):
        fn_db.deleteTest()
        
    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelRenewTest2)
    unittest.TextTestRunner(verbosity = 2).run(suite)
