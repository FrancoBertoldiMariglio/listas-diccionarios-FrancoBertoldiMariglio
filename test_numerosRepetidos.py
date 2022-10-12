import unittest
from numerosRepetidos import numRep


class TestNum(unittest.TestCase):

    def test_checkValid(self):
        clase = numRep(["a", "b", 1, 2])
        dict = clase.checkValid()
        self.assertEqual("La lista solo puede contener numeros", dict)

    def test_rep1(self):
        clase = numRep([0, 1, 2, 3])
        dict = clase.rep()
        self.assertEqual({0: 1, 1: 1, 2: 1, 3: 1}, dict)

    def test_rep2(self):
        clase = numRep([0, 0, 1, 2, 1, 3])
        dict = clase.rep()
        self.assertEqual({0: 2, 1: 2, 2: 1, 3: 1}, dict)


if __name__ == '__main__':
    unittest.main()
