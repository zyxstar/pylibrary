#coding: utf-8
import model_borrow_mock_Test
import model_borrow_db_Test
import model_giveback_mock_Test
import model_giveback_db_Test
import unittest

suite1 = unittest.TestLoader().loadTestsFromTestCase(model_borrow_mock_Test.ModelBorrowTest1)
suite2 = unittest.TestLoader().loadTestsFromTestCase(model_borrow_db_Test.ModelBorrowTest2)
suite3 = unittest.TestLoader().loadTestsFromTestCase(model_giveback_mock_Test.ModelGivebackTest1)
suite4 = unittest.TestLoader().loadTestsFromTestCase(model_giveback_db_Test.ModelGivebackTest2)


alltests = unittest.TestSuite([ suite1,suite2,suite3,suite4])
unittest.TextTestRunner(verbosity=2).run(alltests)



