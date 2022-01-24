# -*- coding: utf-8 -*-
import pyexpat
from fastapi import FastAPI
from fastapi.testclient import TestClient

from hippo.main import DEVAPP

import pytest


class TestAPIIndexEndpoint:
    """
    Test suite to check the index GET and POST methods.

    This test uses the FastAPI convention for testing routes. See the following link:
    https://fastapi.tiangolo.com/tutorial/testing/
    """

    @pytest.mark.parametrize("test_method", ["get", "post"])
    def test_get_method_works_on_index_endpoint(self, test_method: str) -> None:
        # setup
        client = TestClient(app=DEVAPP)

        # execute
        if test_method == "get":
            resp = client.get("/")
        else:
            resp = client.post("/")

        # assert
        assert resp.status_code == 200
        assert "Welcome" in resp.json()["message"]
        assert "Hippo" in resp.json()["message"]
