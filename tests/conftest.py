"""No test opens a socket.

A test that quietly reaches the internet passes or fails on someone else's uptime, and
the failure looks like a bug here. So any attempt to open an HTTP connection during a
test fails at once and names the URL: pass ``SyntheticInfo`` or a stub opener instead.
"""

from __future__ import annotations

import urllib.request

import pytest


class NetworkAccessDuringTest(AssertionError):
    """A test tried to make a real request."""


@pytest.fixture(autouse=True)
def _no_network(monkeypatch):
    def blocked(request, *args, **kwargs):
        url = getattr(request, "full_url", request)
        raise NetworkAccessDuringTest(
            f"a test tried to reach {url}. The suite runs offline: pass SyntheticInfo "
            "or a stub opener."
        )

    monkeypatch.setattr(urllib.request, "urlopen", blocked)
