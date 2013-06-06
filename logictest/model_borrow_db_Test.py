#coding:utf-8
import unittest
import datetime
import sys

sys.path.append(r"F:\eclipsWorkSpace\pylibrary")

#sys.path.append(r"D:\eclipseWorkSpace\pylibrary")

from logic import fn_db, model_borrow

class ModelBorrowTest2(unittest.TestCase):
    def setUp(self):
        pass

    def prepare(self):
        fn_db.ins("LIM_READERCARD", readercardno = "T_C01", readerid = "T_R01",
                   cardsts = "1", expdt = datetime.datetime.strptime("2001-01-01", "%Y-%m-%d"))

        fn_db.ins("LIM_READER", readerid = "T_R01", readername = "ZYX",
                   readercardno = "T_C01", readertypcd = "T_TYP1", orgcd = 'SD',
                   gender = 'M', quantity = 50, deposit = 90.0)

        fn_db.ins("LIC_READERTYP", readertypcd = "T_TYP1", typname = 'NORMAL',
                   typquantity = 50, typdtlimit = 10, typoverprice = 0.2,
                   typdeposit = 100.0, typborrcat = "A1,A2", typrenewtimes = 1,
                   typrenewterm = 5, typlostpay = 2.0)

        fn_db.ins("LIM_BOOKCLS", bookclsid = "T_BC1", bookname = u"计步器",
                   isbn = '9781234567123', auth = 'auth1', pubcd = 'P1',
                   price = 23.6, catcd = "A3")
        fn_db.ins("LIM_BOOKCLS", bookclsid = "T_BC2", bookname = u"心电设备",
                   isbn = '9781234567124', auth = 'auth1', pubcd = 'P2',
                   price = 53.6, catcd = "A1")

        fn_db.ins("LIM_BOOKINS", bookinsid = "T_BI1", bookclsid = "T_BC1",
                  inssts = "1", placecd = "P1")
        fn_db.ins("LIM_BOOKINS", bookinsid = "T_BI2", bookclsid = "T_BC2",
                  inssts = "0", placecd = "P1")

        fn_db.ins("LIT_BORRNOW", readerid = "T_R01", borrexpdt = datetime.datetime.strptime("2001-01-01", "%Y-%m-%d"),
                  readercardno = "T_C01", bookinsid = "T_BI4")

    def check_readercard(self):
        model = model_borrow.ModelBorrow()
        self.assertFalse(model.check_readercard(model.get_reader("T_C01")))

        fn_db.upd("LIM_READERCARD", "readercardno", "T_C01", cardsts = "0")
        self.assertFalse(model.check_readercard(model.get_reader("T_C01")))

        fn_db.upd("LIM_READERCARD", "readercardno", "T_C01", expdt = datetime.datetime.strptime("2099-01-01", "%Y-%m-%d"))
        self.assertTrue(model.check_readercard(model.get_reader("T_C01")))

    def check_reader(self):
        model = model_borrow.ModelBorrow()
        self.assertFalse(model.check_reader(model.get_reader("T_C01")))

        fn_db.upd("LIM_READER", "readerid", "T_R01", quantity = 30)
        self.assertFalse(model.check_reader(model.get_reader("T_C01")))

        fn_db.upd("LIM_READER", "readerid", "T_R01", deposit = 100.0)
        self.assertTrue(model.check_reader(model.get_reader("T_C01")))

    def check_overdue(self):
        model = model_borrow.ModelBorrow()
        fn_db.delete("LIT_BORRNOW", "bookinsid", "T_BI4")
        self.assertFalse(model.check_overdue(model.get_reader("T_C01")))
        fn_db.ins("LIT_BORRNOW", readerid = "T_R01", borrexpdt = datetime.datetime.strptime("2099-01-01", "%Y-%m-%d"),
                  readercardno = "T_C01", bookinsid = "T_BI3")
        self.assertFalse(model.check_overdue(model.get_reader("T_C01")))
        fn_db.ins("LIT_BORRNOW", readerid = "T_R01", borrexpdt = datetime.datetime.strptime("2001-01-01", "%Y-%m-%d"),
                  readercardno = "T_C01", bookinsid = "T_BI4")
        self.assertTrue(model.check_overdue(model.get_reader("T_C01")))
        fn_db.db.update("LIT_BORRNOW", where = "readerid=$readerid and bookinsid=$bookinsid",
                        vars = dict(readerid = "T_R01", bookinsid = "T_BI4"),
                        borrexpdt = datetime.datetime.strptime("2099-01-01", "%Y-%m-%d"))
        self.assertFalse(model.check_overdue(model.get_reader("T_C01")))

    def check_book(self):
        model = model_borrow.ModelBorrow()
        self.assertFalse(model.check_book(model.get_bookins("T_BI1")))

        fn_db.upd("LIM_BOOKINS", "bookinsid", "T_BI1", inssts = "0")
        self.assertTrue(model.check_book(model.get_bookins("T_BI1")))

    def check_borrcat(self):
        model = model_borrow.ModelBorrow()
        reader = model.get_reader("T_C01")
        bookins = model.get_bookins("T_BI1")
        self.assertFalse(model.check_borrcat(reader, bookins))

        fn_db.upd("LIM_BOOKCLS", "bookclsid", "T_BC1", catcd = "A2")
        bookins = model.get_bookins("T_BI1")
        self.assertTrue(model.check_borrcat(reader, bookins))

    def preborrow(self):
        fn_db.upd("LIM_READER", "readerid", "T_R01", quantity = 48)
        fn_db.upd("LIC_READERTYP", "readertypcd", "T_TYP1", typdtlimit = 20)

    def borrow(self):
        model = model_borrow.ModelBorrow()
        self.assertTrue(model.borrow("operator", "T_C01", "T_BI1"))

    def postborrowe(self):
        afterquantity = fn_db.get("LIM_READER", "readerid", "T_R01").quantity
        self.assertEqual(49, afterquantity)        
        
        bookins = fn_db.get("LIM_BOOKINS", "bookinsid", "T_BI1")
        self.assertEqual(bookins.inssts, "1")
        self.assertEqual(bookins.readerid, "T_R01")
        
        borrnow = fn_db.db.select("LIT_BORRNOW", where = "readerid=$readerid and bookinsid=$bookinsid",
                        vars = dict(readerid = "T_R01", bookinsid = "T_BI1"))[0]
        self.assertEqual(borrnow.readerid, "T_R01")
        self.assertEqual(borrnow.readercardno, "T_C01")
        self.assertEqual(borrnow.bookinsid, "T_BI1")
        
        dtlimit = datetime.datetime.now() + datetime.timedelta(days = 20)
        self.assertEqual(borrnow.borrexpdt.date(), dtlimit.date())

    def test_model(self):
        self.clear()
        self.prepare()
        self.check_readercard()
        self.check_reader()
        self.check_overdue()
        self.check_book()
        self.check_borrcat()
        self.preborrow()
#        self.borrow()
#        self.postborrowe()

    def clear(self):
        fn_db.deleteTest()

    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelBorrowTest2)
    unittest.TextTestRunner(verbosity = 2).run(suite)
