import os
import sys
from io import StringIO
from unittest.mock import patch
from src.decorators import log
import logging
import pytest


@pytest.fixture
def caplog(caplog):
    caplog.set_level(logging.DEBUG)
    return caplog


class TestLogDecorator:
    def setup_method(self):
        self.log_file_name = "test_log.txt"
        if os.path.exists(self.log_file_name):
            os.remove(self.log_file_name)

    def teardown_method(self):
        if os.path.exists(self.log_file_name):
            os.remove(self.log_file_name)

    def test_successful_execution_console_output(self, caplog):
        @log()
        def example_function():
            return "Success!"

        example_function()
        for record in caplog.records:
            assert "example_function ok" in record.message

    def test_error_handling_console_output(self, caplog):
        @log()
        def failing_function():
            raise ValueError("Test Error!")

        try:
            failing_function()
        except ValueError:
            pass
        finally:
            for record in caplog.records:
                assert "failing_function error:" in record.message

    def test_successful_execution_to_file(self):
        @log(filename=self.log_file_name)
        def another_example_function():
            return "Another Success!"

        another_example_function()
        with open(self.log_file_name, 'r') as f:
            content = f.read()
            assert "another_example_function ok" in content

    def test_error_handling_in_file(self):
        @log(filename=self.log_file_name)
        def another_failing_function():
            raise TypeError("Test Type Error!")

        try:
            another_failing_function()
        except TypeError:
            pass
        finally:
            with open(self.log_file_name, 'r') as f:
                content = f.read()
                assert "another_failing_function error:" in content