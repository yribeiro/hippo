# -*- coding: utf-8 -*-
import argparse

import uvicorn
from fastapi import FastAPI
from hippo.launcher import HippoServiceLauncher

# region entry point

# global variable used for debug purposes
# Since this DEVAPP is used when the --reload option is run,
# it is imported fresh into a new subprocess, as a result
# it needs to be filled with a new FastAPI class everytime

# Note:
#   The host and port here is ignored as the server is launched in the main method
#   not within the launcher
DEVAPP: FastAPI = HippoServiceLauncher(host="ignored", port=99999).app


def main() -> None:
    """
    Main method that provides the entrypoint for the service.
    """
    parser = argparse.ArgumentParser(description="Hippo Diagnosis Service Launcher")
    parser.add_argument("--host", default="0.0.0.0", help="Address to launch service on")
    parser.add_argument("--port", default=8000, type=int, help="Port to expose service over")
    parser.add_argument("--reload", action="store_true", help="Flag to run hot-reload for development purposes")
    args = parser.parse_args()

    launcher = HippoServiceLauncher(host=args.host, port=args.port)

    if not args.reload:
        launcher.start()
    else:
        # this code path is to be used for development purposes only!
        # the app needs to be picklable as it is running in a subprocess!
        # as a result, the app needs to be passed in as a string so that
        # everytime a reload occurs a new import can be run in the new subprocess
        uvicorn.run("hippo.main:DEVAPP", host=args.host, port=args.port, reload=True)


if __name__ == "__main__":
    main()

# endregion
