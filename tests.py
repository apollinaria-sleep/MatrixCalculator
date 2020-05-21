import unittest
import lib


class TestLastMatrix(unittest.TestCase):
    def test_amount(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 3, '1 2 3', 1, 3, '3 2 1')
        amount = last_matrix.amount()

        self.assertEqual(amount, '[[4 4 4]]')

    def test_difference(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 3, '1 2 3', 1, 3, '3 2 1')
        difference = last_matrix.difference()

        self.assertEqual(difference, '[[-2  0  2]]')

    def test_multiplication(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 3, '1 2 3', 1, 3, '3 2 1')
        multiplication = last_matrix.multiplication()

        self.assertEqual(multiplication, '[[3 4 3]]')

    def test_unamount(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 2, '1 2', 1, 3, '3 2 1')
        amount = last_matrix.amount()

        self.assertEqual(amount, 'Incompatible matrices!')

    def test_undifference(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 2, '1 2', 1, 3, '3 2 1')
        difference = last_matrix.difference()

        self.assertEqual(difference, 'Incompatible matrices!')

    def test_unmultiplication(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 3, '1 2 3', 3, 1, '3 2 1')
        multiplication = last_matrix.multiplication()

        self.assertEqual(multiplication, 'Incompatible matrices!')

    def test_bad_object_type(self):
        last_matrix = lib.LastMatrix()

        with self.assertRaises(AttributeError):
            last_matrix.add_matrix(1, 2, [1, 2], 1, 2, [1, 2])

