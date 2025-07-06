import logging
import os
from pathlib import Path

import pytest

from src.decorators import log


@pytest.fixture
def caplog(caplog: pytest.LogCaptureFixture) -> pytest.LogCaptureFixture:
    caplog.set_level(logging.DEBUG)
    return caplog


class TestLogDecorator:
    def setup_method(self) -> None:
        self.log_file_name = "test_log.txt"
        if os.path.exists(self.log_file_name):
            os.remove(self.log_file_name)

    def test_setup_with_existing_file(self) -> None:
        # Создаем файл, чтобы проверить удаление
        Path(self.log_file_name).touch()
        assert os.path.exists(self.log_file_name)
        self.setup_method()
        assert not os.path.exists(self.log_file_name)

    def test_setup_without_existing_file(self) -> None:
        # Убедимся, что файл изначально отсутствует
        if os.path.exists(self.log_file_name):
            os.remove(self.log_file_name)
        assert not os.path.exists(self.log_file_name)
        self.setup_method()
        assert not os.path.exists(self.log_file_name)

    def teardown_method(self) -> None:
        if os.path.exists(self.log_file_name):
            os.remove(self.log_file_name)

    def test_successful_execution_console_output(self, caplog: pytest.LogCaptureFixture) -> None:
        @log()
        def example_function() -> str:
            return "Success!"

        example_function()
        for record in caplog.records:
            assert "example_function ok" in record.message

    def test_error_handling_console_output(self, caplog: pytest.LogCaptureFixture) -> None:
        @log()
        def failing_function() -> None:
            raise ValueError("Test Error!")

        try:
            failing_function()
        except ValueError:
            pass
        finally:
            for record in caplog.records:
                assert "failing_function error:" in record.message

    def test_successful_execution_to_file(self) -> None:
        @log(filename=self.log_file_name)
        def another_example_function() -> str:
            return "Another Success!"

        another_example_function()
        with open(self.log_file_name, "r") as f:
            content = f.read()
            assert "another_example_function ok" in content

    def test_error_handling_in_file(self) -> None:
        @log(filename=self.log_file_name)
        def another_failing_function() -> None:
            raise TypeError("Test Type Error!")

        try:
            another_failing_function()
        except TypeError:
            pass
        finally:
            with open(self.log_file_name, "r") as f:
                content = f.read()
                assert "another_failing_function error:" in content
