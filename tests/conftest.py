"""Pytest configuration for sage-edge tests."""

import pytest


@pytest.fixture
def mock_gateway_app():
    """Mock Gateway app for testing."""
    from fastapi import FastAPI
    app = FastAPI(title="Mock Gateway")
    return app
