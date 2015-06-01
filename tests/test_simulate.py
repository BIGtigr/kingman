#
# Copyright (C) 2015 Jerome Kelleher <jerome.kelleher@well.ox.ac.uk>
#
# This file is part of kingman.
#
# kingman is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# kingman is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kingman.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Unit tests for the simulate module.
"""
from __future__ import print_function
from __future__ import division

import unittest

import kingman


class TestInput(unittest.TestCase):
    """
    Tests the input of the simulate function.
    """

    def test_bad_sample_size(self):
        for n in [-100, -1, 0, 1]:
            self.assertRaises(ValueError, kingman.simulate, n)


class TestOutput(unittest.TestCase):

    def verify_oriented_forest(self, sample_size, parent, time):
        """
        Verifies that that the specified oriented forest
        (parent, time) is valid for the specified sample_size.
        """
        self.assertEqual(len(parent), 2 * sample_size)
        self.assertEqual(len(time), 2 * sample_size)
        self.assertEqual(parent[0], -1)
        self.assertEqual(time[0], -1)
        self.assertEqual(parent[-1], 0)
        for j in range(1, sample_size + 1):
            self.assertEqual(time[j], 0)
            u = j
            while parent[u] != 0:
                u = parent[u]
            self.assertEqual(u, 2 * sample_size - 1)

    def test_sample_size(self):
        for sample_size in [2, 3, 5, 10]:
            parent, time = kingman.simulate(sample_size)
            self.verify_oriented_forest(sample_size, parent, time)

    def test_random_seed(self):
        # We should get the same result using the same seed
        r1 = kingman.simulate(10, 1)
        r2 = kingman.simulate(10, 1)
        self.assertEqual(r1, r2)
        # We should get different results with different seeds
        self.assertNotEqual(r1, kingman.simulate(10))
        self.assertNotEqual(r1, kingman.simulate(10, 2))
