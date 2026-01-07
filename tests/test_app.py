"""Tests for sage.edge.app module."""

import pytest
from sage.edge.app import create_app


def test_create_app_no_llm():
    """Test creating app without LLM gateway."""
    app = create_app(mount_llm=False)
    assert app.title == "SAGE Edge"
    assert "/healthz" in [route.path for route in app.router.routes]


def test_create_app_with_llm_default_mount():
    """Test creating app with LLM gateway at default path."""
    # This test requires Gateway to be installed
    pytest.skip("Requires isage-llm-gateway")


def test_create_app_with_llm_custom_prefix():
    """Test creating app with LLM gateway at custom prefix."""
    # This test requires Gateway to be installed
    pytest.skip("Requires isage-llm-gateway")
