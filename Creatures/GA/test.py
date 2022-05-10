import unittest
import numpy as np

class MyTest (unittest.TestCase):

    def test_mean(self):
        mean = np.mean([1, 2, 3])
        self.assertEqual(mean, 2)

unittest.main()