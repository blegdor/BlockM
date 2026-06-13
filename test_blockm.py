# test_blockm.py
"""
Tests for BlockM module.
"""

import unittest
from blockm import BlockM

class TestBlockM(unittest.TestCase):
    """Test cases for BlockM class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockM()
        self.assertIsInstance(instance, BlockM)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockM()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
