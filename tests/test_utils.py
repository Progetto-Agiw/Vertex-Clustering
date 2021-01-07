import unittest
from core.utils import shingle_cover
from core.ShingleVectorFactory import create_shingle_vector
from core.shingleVector import ShingleVector
from core.utils import k_shingle_cover

class UtilsTest(unittest.TestCase):

    
    def setUp(self):
        self.shingle_vector = ShingleVector("boh",[1,2,3])
        self.shingle_vector_content = self.shingle_vector.getContent()
        
    def test_empty_shingle(self):
        self.assertTrue(shingle_cover([], []))

    def test_generic_shingles(self):
        self.assertTrue(
                shingle_cover(
                [20, 50, 88, 244], 
                [20, 50, 88, 244]
            )
        )

    def test_different_shingles(self):
        self.assertFalse(
            shingle_cover(
                [1, 50, 88, 244], 
                [20, 50, 88, 244]
            )
        )

    def test_masked_shingles(self):
        self.assertTrue(
            shingle_cover(
                [77, None, 5, 10],
                [None, 2, 5, 10]
            )
        )

    def test_wrong_masked_shingle(self):
        self.assertFalse(
            shingle_cover(
                [15, 99, 255, 0],
                [None, 222, 255, 0]
            )
        )
    
    def test_wrong_k_shingle_cover(self):
        self.assertEqual([], k_shingle_cover(self.shingle_vector_content,4))
        
    def test_6_shingle_cover(self):
        self.assertEqual([[None,None,3],[None,2,None],[1,None,None],[None,2,3],[1,None,3],[1,2,None],[1,2,3]], k_shingle_cover(self.shingle_vector_content,6))
    
    def test_7_shingle_cover(self):
        self.assertEqual([[None,2,3],[1,None,3],[1,2,None],[1,2,3]], k_shingle_cover(self.shingle_vector_content,7))
        
    def test_8_shingle_cover(self):
        self.assertEqual([[1,2,3]], k_shingle_cover(self.shingle_vector_content,8))