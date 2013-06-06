import unittest
import datetime
import mock
import sys
sys.path.append(r"F:\eclipsWorkSpace\pylibrary")

#sys.path.append(r"D:\eclipseWorkSpace\pylibrary")


from logic import model_renew

class ModelReNewTest1(unittest.TestCase):
    def setUp(self):
        pass

    def test_renew(self):
        model = model_renew.ModelRenew()
        model.get_borrnow = mock.Mock(return_value = None)
        self.assertFalse(model.renew("", ""))

        borrnow = mock.Mock()
        borrnow.borrexpdt = datetime.datetime.now() - datetime.timedelta(days = 1)
        model.get_borrnow = mock.Mock(return_value = borrnow)
        self.assertFalse(model.renew("", ""))

        borrnow.borrexpdt = datetime.datetime.now() + datetime.timedelta(days = 1)
        model.get_reader = mock.Mock(return_value = None)
        self.assertFalse(model.renew("", ""))

        reader = mock.Mock()
        reader.typrenewtimes = 1
        borrnow.renewtimes = 1
        model.get_reader = mock.Mock(return_value = reader)
        self.assertFalse(model.renew("", ""))

        reader.typrenewtimes = 2
        reader.typrenewterm = 10
        model.post_renew = mock.Mock()
        model.log = mock.Mock()

        self.assertTrue(model.renew("", ""))
        self.assertTrue(model.post_renew.called)
        self.assertTrue(model.log.called)

    def tearDown(self):
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ModelReNewTest1)
    unittest.TextTestRunner(verbosity = 2).run(suite)
