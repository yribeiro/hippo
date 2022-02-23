# -*- coding: utf-8 -*-
import pytest

from unittest.mock import Mock, patch

from hippo.server import Server


class TestServer:
    @pytest.mark.parametrize(
        ["test_host", "test_port"],
        [
            (1234, 1234),  # invalid host type, valid port type
            ("localhost", "1234"),  # valid host type, invalid port type
        ],
    )
    @patch("hippo.server.FastAPI")
    def test_server_throws_errors_as_expected(self, mockFastApi: Mock, test_host, test_port) -> None:  # type: ignore
        # test if the server class
        with pytest.raises(AssertionError):
            _ = Server(app=mockFastApi, host=test_host, port=test_port)

    @patch("hippo.server.threading.Thread")
    @patch("hippo.server.uvicorn.Config")
    @patch("hippo.server.uvicorn.Server.run")
    def test_server_initialises_config_and_thread_as_expected(
        self, mockUvicornServer: Mock, mockUvicorn: Mock, mockThread: Mock
    ) -> None:

        Server(app="hippo.main:DEVAPP", host="localhost", port=12345, log_level="info")

        mockUvicorn.assert_called_once_with("hippo.main:DEVAPP", host="localhost", port=12345, log_level="info")
        mockThread.assert_called_once_with(target=mockUvicornServer, daemon=True)
