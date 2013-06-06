import unittest
import datetime
import mock
import sys
sys.path.append(r"F:\eclipsWorkSpace\pylibrary")
#sys.path.append(r"D:\eclipseWorkSpace\pylibrary")

from logic import model_borrow

class ModelBorrowTest1(unittest.TestCase):
    def setUp(self):
        pass

    def test_check_readercard(self):
        borrowModel = model_borrow.ModelBorrow()
        reader = mock.Mock()
        reader.cardsts = '1'
        self.assertFalse(borrowModel.check_readercard(reader))

        reader.cardsts = '0'
        reader.expdt = datetime.datetime.strptime("2001-01-01", "%Y-%m-%d")
        self.assertFalse(borrowModel.check_readercard(reader))

        reader.expdt = datetime.datetime.strptime("2099-01-01", "%Y-%m-%d")
        self.assertTrue(borrowModel.check_readercard(reader))

    def test_check_reader(self):
        borrowModel = model_borrow.ModelBorrow()
        reader = mock.Mock()
        reader.quantity = 10
        reader.typquantity = 10
        self.assertFalse(borrowModel.check_reader(reader))

        reader.typquantity = 11
        reader.deposit = 99.0
        reader.typdeposit = 100.0
        self.assertFalse(borrowModel.check_reader(reader))

        reader.deposit = 100.0
        self.assertTrue(borrowModel.check_reader(reader))

    def test_check_overdue(self):
        borrowModel = model_borrow.ModelBorrow()

        query_borrnow = mock.Mock()
        borrowModel.query_borrnow = query_borrnow
        reader = mock.Mock()

        query_borrnow.return_value = []
        self.assertFalse(borrowModel.check_overdue(reader))

        borrnow1 = mock.Mock()
        borrnow1.borrexpdt = datetime.datetime.strptime("2099-01-01", "%Y-%m-%d")
        query_borrnow.return_value = [borrnow1]
        self.assertFalse(borrowModel.check_overdue(reader))

        borrnow2 = mock.Mock()
        borrnow2.borrexpdt = datetime.datetime.strptime("2099-01-01", "%Y-%m-%d")
        query_borrnow.return_value = [borrnow1, borrnow2]
        self.assertFalse(borrowModel.check_overdue(reader))

        borrnow3 = mock.Mock()
        borrnow3.expdt = datetime.datetime.strptime("2001-01-01", "%Y-%m-%d")
        query_borrnow.return_value = [borrnow1, borrnow2, borrnow3]
        self.assertTrue(borrowModel.check_overdue(reader))


    def test_borrow(self):
        borrowModel = model_borrow.ModelBorrow()

        borrowModel.get_reader = mock.Mock(return_value = None)
        self.assertFalse(borrowModel.borrow("", "", ""))

        reader = mock.Mock()
        borrowModel.get_reader = mock.Mock(return_value = reader)

        borrowModel.check_readercard = mock.Mock(return_value = False)
        self.assertFalse(borrowModel.borrow("", "", ""))

        borrowModel.check_readercard = mock.Mock(return_value = True)
        borrowModel.check_reader = mock.Mock(return_value = False)
        self.assertFalse(borrowModel.borrow("", "", ""))

        borrowModel.check_reader = mock.Mock(return_value = True)
        borrowModel.check_overdue = mock.Mock(return_value = True)
        self.assertFalse(borrowModel.borrow("", "", ""))

        borrowModel.check_overdue = mock.Mock(return_value = False)
        borrowModel.get_bookins = mock.Mock(return_value = None)
        self.assertFalse(borrowModel.borrow("", "", ""))

        bookins = mock.Mock()
        borrowModel.get_bookins = mock.Mock(return_value = bookins)
        borrowModel.check_book = mock.Mock(return_value = False)
        self.assertFalse(borrowModel.borrow("", "", ""))

        borrowModel.check_book = mock.Mock(return_value = True)
        borrowModel.check_borrcat = mock.Mock(return_value = False)
        self.assertFalse(borrowModel.borrow("", "", ""))

        borrowModel.check_borrcat = mock.Mock(return_value = True)
        borrowModel.post_borrow = mock.Mock()
        borrowModel.log = mock.Mock()
        self.assertTrue(borrowModel.borrow("", "", ""))


    def tearDown(self):
        pass


if __name__ == '__main__':
#    unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelBorrowTest1)
    unittest.TextTestRunner(verbosity = 2).run(suite)
