import unittest
import lib


class TestLastMatrix(unittest.TestCase):
    def test_amount(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 3, '1 2 3\n', 1, 3, '3 2 1\n')
        amount = last_matrix.amount()

        self.assertEqual(amount, '[[4 4 4]]')

    def test_difference(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 3, '1 2 3\n', 1, 3, '3 2 1\n')
        difference = last_matrix.difference()

        self.assertEqual(difference, '[[-2  0  2]]')

    def test_composition(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 3, '1 2 3\n', 1, 3, '3 2 1\n')
        composition = last_matrix.composition()

        self.assertEqual(composition, '[[3 4 3]]')

    def test_unamount(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 2, '1 2\n', 1, 3, '3 2 1\n')
        amount = last_matrix.amount()

        self.assertEqual(amount, 'Incompatible matrices!')

    def test_undifference(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 2, '1 2\n', 1, 3, '3 2 1\n')
        difference = last_matrix.difference()

        self.assertEqual(difference, 'Incompatible matrices!')

    def test_uncomposition(self):
        last_matrix = lib.LastMatrix()
        last_matrix.add_matrix(1, 3, '1 2 3\n', 3, 1, '3\n2\n1\n')
        composition = last_matrix.composition()

        self.assertEqual(composition, 'Incompatible matrices!')

    def test_bad_object_type(self):
        last_matrix = lib.LastMatrix()

        with self.assertRaises(AttributeError):
            last_matrix.add_matrix(1, 2, [1, 2], 1, 2, [1, 2])
