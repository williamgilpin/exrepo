#!/usr/bin/env python
import os
import unittest

WORKING_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(WORKING_DIR)

import sys

sys.path.insert(1, os.path.join(WORKING_DIR, "exrepo"))
from exrepo.core import random_walk, ornstein_uhlenbeck


class TestModels(unittest.TestCase):
    """
    Tests integration and models
    """
    def test_random_walk(self):
        """
        Test generating a trajectory
        """
        traj = random_walk(0.1, 100)
        assert len(traj) == 100, "Generated trajectory has the wrong shape"
        
    def test_ornstein_uhlenbeck(self):
        """
        Test generating a trajectory with stochasticity
        """
        traj = ornstein_uhlenbeck(0.1, 100)
        assert len(traj) == 100, "Generated trajectory has the wrong shape"

if __name__ == "__main__":
    unittest.main()