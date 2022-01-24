# -*- coding: utf-8 -*-
from typing import Dict
from fastapi import APIRouter

# Note: the prefix here indicates it is the root path i.e. http://service:port/
router = APIRouter(tags=["index"], prefix="")


@router.get("/")
def index_get() -> Dict[str, str]:
    """Exemplar GET endpoint for the API service. Simply returns a welcome message."""
    return {"message": "Welcome to the Hippo diagnosis service!"}


@router.post("/")
def index_post() -> Dict[str, str]:
    """Exemplar POST endpoint for the API service. Simply returns a welcome message."""
    return {"message": "Welcome to the Hippo diagnosis service!"}
