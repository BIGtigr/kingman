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
Unit tests for the kingman package. These are intended to be run
using nose.
"""
from __future__ import print_function
from __future__ import division

import unittest

import kingman.cli as cli


class TestCli(unittest.TestCase):
    """
    Test cases for the command line interface for kingman.
    """

    def test_sample_size(self):
        parser = cli.get_parser()
        for sample_size in ["2", "10", "100"]:
            args = parser.parse_args([sample_size])
            self.assertEqual(args.sample_size, int(sample_size))
            # random seed is not specified, so should be None
            self.assertEqual(args.random_seed, None)

    def test_random_seed(self):
        parser = cli.get_parser()
        args = parser.parse_args(["2", "--random-seed=10"])
        self.assertEqual(args.sample_size, 2)
        self.assertEqual(args.random_seed, 10)
        args = parser.parse_args(["2", "-s", "100"])
        self.assertEqual(args.sample_size, 2)
        self.assertEqual(args.random_seed, 100)
