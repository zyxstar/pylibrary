import unittest
import datetime
import mock
import sys
sys.path.append(r"F:\eclipsWorkSpace\pylibrary")

#sys.path.append(r"D:\eclipseWorkSpace\pylibrary")


from logic import model_giveback

class ModelGivebackTest1(unittest.TestCase):
    def setUp(self):
        pass

    def test_calc_overdays(self):
        model = model_giveback.ModelGiveback()
        borrnow = mock.Mock()
        days = 12
        borrnow.borrexpdt = datetime.datetime.now() + datetime.timedelta(days=days)
        self.assertEqual(0 - days, model.calc_overdays(borrnow))

        borrnow.borrexpdt = datetime.datetime.now() - datetime.timedelta(days=days)
        self.assertEqual(days, model.calc_overdays(borrnow))

    def test_calc_overprice(self):
        model = model_giveback.ModelGiveback()
        self.assertEqual(0, model.calc_overprice(0, None))
        self.assertEqual(0, model.calc_overprice(-1, None))
        overdays = 12
        reader = mock.Mock(typoverprice=0.3)
        self.assertEqual(12 * 0.3, model.calc_overprice(overdays, reader))

    def test_giveback(self):
        model = model_giveback.ModelGiveback()
        model.get_borrnow = mock.Mock(return_value=None)
        self.assertFalse(model.giveback("", ""))
        
        borrnow = mock.Mock()
        model.get_borrnow = mock.Mock(return_value=borrnow)
        model.get_bookins = mock.Mock(return_value=None)
        self.assertFalse(model.giveback("", ""))
        self.assertEqual(borrnow, model.borrnow)
        
        bookins = mock.Mock()
        model.get_bookins = mock.Mock(return_value=bookins)
        model.get_reader = mock.Mock(return_value=None)
        self.assertFalse(model.giveback("", ""))
        self.assertEqual(bookins, model.bookins)       
        
        reader = mock.Mock()
        model.get_reader = mock.Mock(return_value=reader)
        model.calc_overdays = mock.Mock(return_value=0)
        model.calc_overprice = mock.Mock(return_value=0)
        model.post_giveback = mock.Mock()
        model.log = mock.Mock()
        
        self.assertTrue(model.giveback("", ""))
        self.assertEqual(reader, model.reader) 
        self.assertTrue(model.post_giveback.called)
        self.assertTrue(model.log.called)
       
    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelGivebackTest1)
    unittest.TextTestRunner(verbosity=2).run(suite)
