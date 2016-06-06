# coding: utf-8
import pytest
from requests.compat import urljoin


def prepare_url(value):
    # Issue #1483: Make sure the URL always has a trailing slash
    httpbin_url = value.url.rstrip('/') + '/'

    def inner(*suffix):
        return urljoin(httpbin_url, '/'.join(suffix))

    return inner


@pytest.fixture
def httpbin(httpbin):
    return prepare_url(httpbin)


@pytest.fixture
def httpbin_secure(httpbin_secure):
    return prepare_url(httpbin_secure)


def pytest_addoption(parser):
    parser.addoption("--import-urllib3", action="store_true",
                     default=None,
                     help="Import urllib3 before tests")

    parser.addoption("--inject-openssl", action="store_true",
                     default=None,
                     help="Inject openssl in urllib3")


def pytest_configure(config):
    if config.getvalue('import_urllib3'):
        try:
            import urllib3
        except ImportError:
            urllib3 = None
        if urllib3 and config.getvalue('import_urllib3'):
            print('importing urllib3')
            try:
                from urllib3.contrib.pyopenssl import inject_into_urllib3
            except ImportError:
                inject_into_urllib3 = None

            if inject_into_urllib3:
                print('injecting openssl')
                inject_into_urllib3()
