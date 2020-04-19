import unittest
from Regex import panameno

class TestRegex(unittest.TestCase):

    def test_1(self):
        text="Z-9102-2112"
        result=panameno(text)
        self.assertEqual(result,"\nCedula Invalida")

    def test_2(self):
        text="8-913-2413"
        result=panameno(text)
        self.assertEqual(result,"\nExcelente! Esta cedula es valida.")

    def test_3(self):
        text="8913ckfkwfk2413"
        result=panameno(text)
        self.assertEqual(result,"\nCedula Invalida")

if __name__=="__main__":
    unittest.main()