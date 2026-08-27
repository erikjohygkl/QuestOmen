# test_questomen.py
"""
Tests for QuestOmen module.
"""

import unittest
from questomen import QuestOmen

class TestQuestOmen(unittest.TestCase):
    """Test cases for QuestOmen class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = QuestOmen()
        self.assertIsInstance(instance, QuestOmen)
        
    def test_run_method(self):
        """Test the run method."""
        instance = QuestOmen()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
