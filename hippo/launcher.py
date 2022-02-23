# -*- coding: utf-8 -*-
import uvicorn

from fastapi import FastAPI, APIRouter
from threading import Thread
from hippo import api, __version__
from hippo.server import Server
import time
import contextlib


class HippoServiceLauncher:
    """
    Class wrapper for Hippo FastAPI. The idea behind building the wrapper
    is to be able to launch the FastAPI server while also leaving the main thread
    unblocked.

    The recommended usage of FastAPI is main thread blocking, which prevents other
    python methods from running.

    The routes have been implemented as suggested by the FastAPI documentation.
    """

    def __init__(self, host: str, port: int) -> None:
        """
        Initialiser

        :param host: IP address host to launch service on.
        :param port: Port number to host service on.
        """
        # checks
        assert isinstance(host, str), f"Expected type string for arg: host, got type: {type(host)}"
        assert isinstance(port, int), f"Expected type int for arg: port, got type: {type(port)}"

        # dunder to mask properties (private)
        self.__host = host
        self.__port = port
        self.__app = self._build_fast_api_app()
        # An intance of the Server class, this is an abstraction of the uvicorn server to allow the starting and stopping of the server in a separate thread.
        self.__server = Server(app=self.__app, host=self.__host, port=self.__port)

    # region private API
    def _build_fast_api_app(self) -> FastAPI:
        """
        Private helper method that extracts all the APIRouter definitions
        defined under the API package and builds a FastAPI application
        that can be launched within a WSGI server.

        Improvement Note:
            This implementation does not follow the Single Responsibilty Principle. See SOLID code
            dev practices. The responsibility for creating the application should live within
            another component, and this class should be responsible for app launch and resource clean up.

            Patterns such as the Builder pattern, can be used to encapsulate the app construction
            into a separate class. This class can then be injected into the launcher
            (Inversion Principle via Dependency Injection).

        :return: FastAPI instance populated with the appropriate routes.
        """
        app = FastAPI(title="Hippo Diagnosis Service", version=__version__)
        # get all the properties of the hippo.api package (which includes the router instances)
        hashmap = vars(api)
        # store all properties that are of the APIRouter type
        routers = [hashmap[key] for key in hashmap.keys() if isinstance(hashmap[key], APIRouter)]
        # add all routers to the FastAPI app
        for router in routers:
            app.include_router(router)
        return app

    # endregion

    # region public API

    @property
    def host(self) -> str:
        return self.__host

    @property
    def port(self) -> int:
        return self.__port

    @property
    def app(self) -> FastAPI:
        # need to make public for development and testing purposes
        # protected as this is a new instance of the application - not the one stored within
        # the class property
        return self._build_fast_api_app()

    def start(self) -> None:
        """
        Method to start the app using an underlying uvicorn server.
        Note: This method runs the server inside subprocess / child daemon thread.
        """

        self.__server.run_thread()

    def stop(self) -> None:
        """
        Method to stop the apps uvicorn server.
        """
        self.__server.stop_thread()

    # endregion
