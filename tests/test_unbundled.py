# coding: utf-8
from __future__ import absolute_import

from tests.testserver.server import Server

from . import (
    urllib3_package,
    urllib3_unbundled_only,
)


@urllib3_unbundled_only
def test_unbundled_urllib3_util():
    """is unbundled correctly"""
    assert urllib3_package

    from urllib3 import util as urllib3_util
    from requests.packages.urllib3 import util as requests_urllib3_util
    assert id(urllib3_util) == id(requests_urllib3_util)
    assert urllib3_util.HAS_SNI == requests_urllib3_util.HAS_SNI
