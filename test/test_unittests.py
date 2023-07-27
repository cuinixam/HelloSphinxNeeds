#!/usr/bin/env python3

import unittest
import os.path
import json
from utils import run_process


class TestUnitTests(unittest.TestCase):

    def test_unit_tests_Flv1__Sys1(self):
        variant = 'Flv1/Sys1'
        self.build_unittests_and_expect_files(variant)

    def test_unit_tests_Flv1__Sys2(self):
        variant = 'Flv1/Sys2'
        self.build_unittests_and_expect_files(variant)

    def build_unittests_and_expect_files(self, variant):
        exit_code = run_process([
            'build.bat',
            '-variants', variant,
            '-target', 'unittests',
            '-reconfigure'
        ])

        """Unit tests execution shall pass."""
        self.assertEqual(0, exit_code)

        """Coverage report shall be created"""
        expected_file = f"build/{variant}/test/coverage/index.html"
        self.assertTrue(os.path.isfile(expected_file), f"File {expected_file} shall exist.")
