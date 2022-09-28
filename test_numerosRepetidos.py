import unittest
from numerosRepetidos import numRep


class TestNum(unittest.TestCase):

    def test_1(self):
        dict = numRep([0, 1, 2, 3])
        self.assertEqual({0: 1, 1: 1, 2: 1, 3: 1}, dict)

    def test_2(self):
        dict = numRep([0, 0, 1, 2, 1, 3])
        self.assertEqual({0: 2, 1: 2, 2: 1, 3: 1}, dict)

    def test_3(self):
        dict = numRep(["a", "b", 1, 2])
        self.assertEqual("La lista solo puede contener numeros", dict)


if __name__ == '__main__':
    unittest.main()
