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
