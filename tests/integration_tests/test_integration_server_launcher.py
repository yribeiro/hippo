# -*- coding: utf-8 -*-

from hippo.launcher import HippoServiceLauncher
import requests  # type: ignore

# we ignore the requests type since mypy gives an error when commiting even if types-requests is installed


class TestIntegrationServer:
    def test_uvicorn_server_start(self) -> None:
        # setup
        # instantiate the server instance
        launcher = HippoServiceLauncher(host="localhost", port=12345)

        # setup the url - given the test the url could be hardcoded but I put this here in case we want to change that in the future
        url_string = "http://{}:{}/".format(launcher.host, launcher.port)

        # execute
        with launcher.run_in_thread():  # start server

            get_response = requests.get(url_string)  # send GET request to url
            post_response = requests.post(url_string)  # send POST request to url

        # assert
        assert get_response.status_code == 200  # check if the get request was succesful
        assert get_response.json() == {
            "message": "Welcome to the Hippo diagnosis service!"
        }  # additional check to ensure the GET request came from our server and not another server

        assert post_response.status_code == 200  # check if the get request was succesful
        assert post_response.json() == {
            "message": "Welcome to the Hippo diagnosis service!"
        }  # additional check to ensure the POST request came from our server and not another server

    def test_uvicorn_server_stop(self) -> None:

        # setup
        launcher = HippoServiceLauncher(host="localhost", port=12345)

        # setup the url - given the test the url could be hardcoded but I put this here in case we want to change that in the future
        url_string = "http://{}:{}/".format(launcher.host, launcher.port)

        # execute
        launcher.start()  # start FastAPI server

        server_off = False  # set server_off variable to false

        launcher.stop()  # stop server

        # assert

        # check if server was stopped by sending a request to the srver and seeing if the request retuns a connection error or a timeout
        try:
            r = requests.get(url_string)
            r.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xxx
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            # if a connection error or a timeout was raised set server_off variable to true
            server_off = True

        # check if server_off variable is true
        assert server_off is True, "Server didn't shut down."


# End of file
