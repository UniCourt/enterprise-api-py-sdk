"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button>   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.case_count_analytics_by_court_geo import CaseCountAnalyticsByCourtGeo
from openapi_client.model.court import Court
from openapi_client.model.court_location import CourtLocation
globals()['CaseCountAnalyticsByCourtGeo'] = CaseCountAnalyticsByCourtGeo
globals()['Court'] = Court
globals()['CourtLocation'] = CourtLocation
from openapi_client.model.case_count_analytics_by_court_location import CaseCountAnalyticsByCourtLocation


class TestCaseCountAnalyticsByCourtLocation(unittest.TestCase):
    """CaseCountAnalyticsByCourtLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCaseCountAnalyticsByCourtLocation(self):
        """Test CaseCountAnalyticsByCourtLocation"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CaseCountAnalyticsByCourtLocation()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
