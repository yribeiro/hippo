# -*- coding: utf-8 -*-
from unittest.mock import Mock, patch

import pytest

from hippo.main import main


class TestMainEntryPoint:
    @pytest.fixture(scope="class")
    def mockArgs(self) -> Mock:
        args = Mock()
        args.host = "local"
        args.port = 1234
        args.reload = False
        return args

    @patch("hippo.main.HippoServiceLauncher")
    @patch("hippo.main.argparse.ArgumentParser")
    def test_main_runs_as_expected_if_reload_is_false(
        self, mockArgumentParser: Mock, mockServiceLauncher: Mock, mockArgs: Mock
    ) -> None:
        # setup
        mockArgumentParser.return_value.parse_args.return_value = mockArgs

        # excute
        main()

        # assert
        assert mockArgumentParser.call_count == 1
        assert mockServiceLauncher.call_count == 1
        assert mockServiceLauncher.return_value.start.call_count == 1

    @patch("hippo.main.uvicorn")
    @patch("hippo.main.HippoServiceLauncher")
    @patch("hippo.main.argparse.ArgumentParser")
    def test_main_runs_uvicorn_if_reload_is_true(
        self, mockArgumentParser: Mock, mockServiceLauncher: Mock, mock_uvicorn: Mock, mockArgs: Mock
    ) -> None:
        # setup
        mockArgs.reload = True
        mockArgumentParser.return_value.parse_args.return_value = mockArgs

        # excute
        main()

        # assert
        assert mockArgumentParser.call_count == 1
        assert mockServiceLauncher.call_count == 1
        assert mockServiceLauncher.return_value.start.call_count == 0
        assert mock_uvicorn.run.call_count == 1
        assert "main:DEVAPP" in mock_uvicorn.run.call_args[0][0]
        assert mock_uvicorn.run.call_args[1]["host"] == mockArgs.host
        assert mock_uvicorn.run.call_args[1]["port"] == mockArgs.port
