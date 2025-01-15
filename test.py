import unittest
from main import create_3d_matrix, calculate_sum

class TestMatrix(unittest.TestCase):
    def test_create_3d_matrix(self):
        size = 3
        matrix = create_3d_matrix(size)
        self.assertEqual(len(matrix), size)
        self.assertEqual(len(matrix[0]), size)
        self.assertEqual(len(matrix[0][0]), size)
    
    def test_calculate_sum(self):
        matrix = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
        self.assertEqual(calculate_sum(matrix), 36)

if __name__ == "__main__":
    unittest.main()
