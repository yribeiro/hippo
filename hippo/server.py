# -*- coding: utf-8 -*-
import threading
from fastapi import FastAPI
import uvicorn


class Server(uvicorn.Server):
    """Class wrapper for the uvicron server. The idea behind building the wrapper
    is to be able to launch the uvicorn server in a separate thread. The purpose is to not block the main thread.

    The class is based on the comments found at this address:
    https://github.com/encode/uvicorn/issues/742#issuecomment-674411676

    The class inherits from the uvicorn.Server class.
    """

    def __init__(self, app: FastAPI, host: str = "localhost", port: int = 8000, log_level: str = "info") -> None:
        """
        Initiliser

        Args:
            app ( [FastAPI] ): The FastAPI server we want to run.
            host (str, optional): IP address host to launch service on. Defaults to 'localhost'.
            port (int, optional): Port number to host service on. Defaults to 8000.
            log_level (str, optional):The level of logging we want the server to have. Defaults to 'info'.

        """
        assert isinstance(host, str), f"Expected type string for arg: host, got type: {type(host)}"
        assert isinstance(port, int), f"Expected type int for arg: port, got type: {type(port)}"
        assert isinstance(app, FastAPI), f"Expected type FastAPI for arg: app, got type: {type(app)}"

        self.__config = uvicorn.Config(app, host=host, port=port, log_level=log_level)

        super().__init__(self.__config)

        # define the thread as a class property/parameter so that the "run_in_thread" and "stop_thread" can be run on the same thread.
        self.__thread = threading.Thread(target=self.run, daemon=False)

    def run(self) -> None:
        """Method for starting the thread containing the uvicorn server"""
        self.__thread.start()

    def stop(self, timeout: int = 5) -> None:
        """
        Method for stopping the thread containing the uvicorn server

        :param timeout: Timeout when exiting the launcher for child threads to exit, defaults to 5
        """

        self.should_exit = True

        # wait for thead to terminate, this is used to ensure that the thread has been terminated.
        self.__thread.join(timeout=timeout)

        # check if the thread is still alive - this is needed because the join method always returns None even if it timedout.
        assert self.__thread.is_alive() is False, "Thread didn't close properly. The method thread.join() has timedout."
