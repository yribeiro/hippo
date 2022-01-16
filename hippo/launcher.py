# -*- coding: utf-8 -*-
import uvicorn

from fastapi import FastAPI, APIRouter

from hippo import api


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
        # dunder to mask properties (private)
        self.__host = host
        self.__port = port
        self.__app = self._build_fast_api_app()

    # region private API
    def _build_fast_api_app(self) -> FastAPI:
        """
        Private helper method that extracts all the APIRouter definitions
        defined under the API package and builds a FastAPI application
        that can be launched within a WSGI server.

        :return: FastAPI instance populated with the appropriate routes.
        """
        app = FastAPI()
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
        Note:
            This method is main thread blocking.
            TODO: Implementation is required to run this server inside subprocess / child daemon thread.
        """
        uvicorn.run(app=self.__app, host=self.__host, port=self.__port)

    # endregion
