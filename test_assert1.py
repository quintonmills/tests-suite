import unittest
class youDontWantSmoke(unittest.TestCase):
    def test_exampleOne(self):
        statementOne = "IDGAFAWABGTSAM"
        statementTwo = "Boy if you dont"
        self.assertNotEqual(statementOne,statementTwo)
    def test_exampleTwo(self):
        numberOne = 69
        numberTwo = 420
        self.assertNotEqual(numberOne,numberTwo)
    def test_exampleThree(self):
        dict1 = {'big':'small','up':'down','black':'white'}
        dict2 = {'big':'small','up':'down','black':'white'}
        self.assertDictEqual(dict1,dict2)
    if __name__ == '__main__':
        unittest.main(verbosity=1)




