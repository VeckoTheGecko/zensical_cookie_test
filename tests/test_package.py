from __future__ import annotations

import importlib.metadata

import zensical_cookie_test as m


def test_version():
    assert importlib.metadata.version("zensical_cookie_test") == m.__version__
