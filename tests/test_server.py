# -*- coding: utf-8 -*-
from black import patch_click
import pytest
from fastapi import FastAPI
from unittest.mock import Mock, patch

from hippo.server import Server
from typing import Any


class TestServer:
    @pytest.mark.parametrize(
        ["test_host", "test_port", "test_api"],
        [
            (1234, 1234, Mock(spec=FastAPI)),  # invalid host type, valid port type, valid app type
            ("localhost", "1234", Mock(spec=FastAPI)),  # valid host type, invalid port type, valid app type
            ("localhost", 1234, Mock()),  # valid host type, valid port type, invalid app type
        ],
    )
    def test_server_throws_errors_as_expected(self, test_host: str, test_port: int, test_api: Any) -> None:
        # setup, execute and assert
        with pytest.raises(AssertionError):
            _ = Server(app=test_api, host=test_host, port=test_port)

    @patch("hippo.server.threading.Thread")
    @patch("hippo.server.uvicorn.Config")
    @patch("hippo.server.Server.run")
    def test_server_initialises_config_and_thread_as_expected(
        self, mockUvicornServer: Mock, mockUvicornConfig: Mock, mockThread: Mock
    ) -> None:

        # setup
        mockAPP = Mock(spec=FastAPI)

        # execute
        Server(app=mockAPP, host="localhost", port=12345, log_level="info")

        # assert
        mockUvicornConfig.assert_called_once_with(mockAPP, host="localhost", port=12345, log_level="info")
        mockThread.assert_called_once_with(target=mockUvicornServer, daemon=False)

    @patch("hippo.server.threading.Thread.start")
    @patch("hippo.server.threading.Thread.join")
    def test_server_runs_thread_correctly(self, mockThreadjoin: Mock, mockThreadstart: Mock) -> None:

        # setup
        mockAPP = Mock(spec=FastAPI)
        server_instance = Server(app=mockAPP, host="localhost", port=12345, log_level="info")

        # execute
        server_instance.run()
        server_instance.stop()

        # assert
        assert server_instance.should_exit is True
        mockThreadstart.assert_called_once()
        mockThreadjoin.assert_called_once()
