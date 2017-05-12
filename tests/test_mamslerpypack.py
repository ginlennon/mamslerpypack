#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_mamslerpypack
----------------------------------

Tests for `mamslerpypack` module.
"""


import sys
import unittest
from contextlib import contextmanager
from click.testing import CliRunner

from mamslerpypack import mamslerpypack
from mamslerpypack import cli



class TestMamslerpypack(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_000_something(self):
        pass

    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'mamslerpypack.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output