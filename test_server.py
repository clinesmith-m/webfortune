import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


def test_slash(app, client):
    res = client.get("/")
    assert res.status_code == 302


def test_cowsay(app, client):
    # Base test
    message = "Test"
    res = client.get("/cowsay/%s/" % message)
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert message in page_output
    # Same test, but the string has whitespace
    message = "Test with spaces"
    res = client.get("/cowsay/%s/" % message)
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert message in page_output


def test_fortune(app, client):
    res = client.get("/fortune/")
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert page_output.startswith("<pre>")
    assert page_output.endswith("</pre>")
    assert len(page_output.lstrip("<pre>").rstrip("</pre>")) > 0

def test_cowfortune(app, client):
    res = client.get("/cowfortune/")
    assert res.status_code == 200
    page_output = res.get_data(as_text=True)
    assert page_output.startswith("<pre>")
    assert page_output.endswith("</pre>")
    assert len(page_output.lstrip("<pre>").rstrip("</pre>")) > 0
