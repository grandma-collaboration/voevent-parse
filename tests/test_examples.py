"""Check the syntax in example files is valid"""

import os
import sys
import tempfile
from unittest import TestCase


class TestExamples(TestCase):
    def setUp(self):
        # Run in a tempdir, in case the examples dump any output
        self.orig_dir = os.getcwd()
        self.tempdir = tempfile.mkdtemp()
        os.chdir(self.tempdir)

        repo_topdir = os.path.join(
            os.path.dirname(__file__),  # voevent-parse/tests
            os.pardir,  # voevent-parse/
        )
        self.examples_dir = os.path.join(repo_topdir, "examples")
        sys.path.insert(0, self.examples_dir)

    def tearDown(self):
        os.chdir(self.orig_dir)
        sys.path.pop(0)

    def test_basic_usage(self):
        pass

    def test_new_voevent(self):
        pass
