# coding: utf-8
import warnings

import pytest

try:
    import urllib3 as urllib3_package
except ImportError:
    urllib3_package = False

from requests.packages import urllib3 as urllib3_bundle

if urllib3_package is urllib3_bundle:
    from urllib3.exceptions import SNIMissingWarning
else:
    from requests.packages.urllib3.exceptions import SNIMissingWarning

# urllib3 sets this to only go off once, but we need it to
# always fire for test_requests.test_https_warnings to work
warnings.simplefilter('always', SNIMissingWarning)

urllib3_unbundled_only = pytest.mark.skipif(
    urllib3_package != urllib3_bundle,
    reason="urllib3 not unbundled")
