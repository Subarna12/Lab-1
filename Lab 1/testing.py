import unittest
from binarysearch import iterative_binary_search
from binarysearch import recursive_binary_search
from linear_search import linear_search 

class SearchTestcase(unittest.TestCase):
    def test_iterative_binary_search(self):

        A = list(range(7))

        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 0), 0)
        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 1), 1)
        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 2), 2)
        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 3), 3)
        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 4), 4)
        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 5), 5)
        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 6), 6)


        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 100), -1)
        self.assertEqual(iterative_binary_search(A, 0, len(A) - 1, 98), -1)

    def test_recursive_binary_search(self):
    

        A = list(range(7))

        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 0), 0)
        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 1), 1)
        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 2), 2)
        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 3), 3)
        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 4), 4)
        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 5), 5)
        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 6), 6)


        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 100), -1)
        self.assertEqual(recursive_binary_search(A, 0, len(A) - 1, 98), -1)

    def test_linear_search(self):
        
        A = list(range(7))

        self.assertEqual(linear_search(A, 0), 0)
        self.assertEqual(linear_search(A, 1), 1)
        self.assertEqual(linear_search(A, 2), 2)
        self.assertEqual(linear_search(A, 3), 3)
        self.assertEqual(linear_search(A, 4), 4)
        self.assertEqual(linear_search(A, 5), 5)
        self.assertEqual(linear_search(A, 6), 6)


        self.assertEqual(linear_search(A, 90), -1)
        self.assertEqual(linear_search(A, 90), -1)

if __name__ == "__main__":
    unittest.main()
    

