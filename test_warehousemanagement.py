# test_warehousemanagement.py
"""
Tests for WarehouseManagement module.
"""

import unittest
from warehousemanagement import WarehouseManagement

class TestWarehouseManagement(unittest.TestCase):
    """Test cases for WarehouseManagement class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WarehouseManagement()
        self.assertIsInstance(instance, WarehouseManagement)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WarehouseManagement()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
