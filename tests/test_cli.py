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
Unit tests for the cli module.
"""
from __future__ import print_function
from __future__ import division

import json
import unittest
import tempfile

import kingman.cli as cli


class TestInput(unittest.TestCase):
    """
    Test cases for the command line interface input for kingman.
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


class TestOutput(unittest.TestCase):
    """
    Test cases for the command line interface output for kingman
    """

    def verify_json_outout(self, sample_size, json_dict):
        self.assertEqual(len(json_dict), 2)
        parent = json_dict["parent"]
        time = json_dict["time"]
        self.assertEqual(len(parent), 2 * sample_size - 1)
        self.assertEqual(len(time), 2 * sample_size - 1)

    def test_sample_size(self):
        for sample_size in [2, 5, 10]:
            with tempfile.TemporaryFile("w+") as f:
                cli.run_simulation(sample_size, None, f)
                f.seek(0)
                result = json.load(f)
                self.verify_json_outout(sample_size, result)
