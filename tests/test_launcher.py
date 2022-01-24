# -*- coding: utf-8 -*-
from fastapi import APIRouter
import pytest

from unittest.mock import Mock, patch

from hippo import api
from hippo.launcher import HippoServiceLauncher


class TestServiceLauncher:
    @pytest.mark.parametrize(
        ["test_host", "test_port"],
        [
            (1234, 1234),  # invalid host type, valid port type
            ("localhost", "1234"),  # valid host type, invalid port type
        ],
    )
    def test_launcher_throws_errors_as_expected(self, test_host, test_port) -> None:  # type: ignore
        # setup, execute and assert
        with pytest.raises(AssertionError):
            _ = HippoServiceLauncher(host=test_host, port=test_port)

    @patch.object(HippoServiceLauncher, "_build_fast_api_app")
    def test_launcher_initialises_as_expected(self, mock_helper_method: Mock) -> None:
        # setup
        host, port = "localhost", 12345

        # execute
        launcher = HippoServiceLauncher(host=host, port=port)

        # assert
        assert launcher.host == host
        assert launcher.port == port
        assert mock_helper_method.call_count == 1

    @patch("hippo.launcher.FastAPI")
    def test_launcher_builds_app_correctly(self, mockFastAPI: Mock) -> None:
        """
        Note:
            this is a whitebox test - to ensure that the build includes all routers in the api
            package.
        """
        # setup
        hashmap = vars(api)
        routers = [hashmap[key] for key in hashmap.keys() if isinstance(hashmap[key], APIRouter)]

        # execute
        launcher = HippoServiceLauncher(host="localhost", port=12345)

        # assert
        assert mockFastAPI.call_count == 1
        assert len(routers) == mockFastAPI.return_value.include_router.call_count
        for idx, expected_router in enumerate(routers):
            # this is a white box test as the order matters
            assert expected_router == mockFastAPI.return_value.include_router.call_args[0][idx]
        assert launcher._HippoServiceLauncher__app == mockFastAPI.return_value  # type: ignore

    @patch("hippo.launcher.uvicorn")
    def test_launcher_runs_server_as_expected(self, mock_uvicorn: Mock) -> None:
        # setup
        launcher = HippoServiceLauncher(host="localhost", port=12345)

        # execute
        launcher.start()

        # assert
        assert mock_uvicorn.run.call_count == 1
        assert mock_uvicorn.run.call_args[1]["app"] == launcher._HippoServiceLauncher__app  # type: ignore
        assert mock_uvicorn.run.call_args[1]["host"] == "localhost"
        assert mock_uvicorn.run.call_args[1]["port"] == 12345
