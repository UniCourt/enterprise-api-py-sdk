"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button>   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.case_analytics_api import CaseAnalyticsAPI
from openapi_client.model.law_firm_analytics_api import LawFirmAnalyticsAPI
from openapi_client.model.norm_organization import NormOrganization
globals()['CaseAnalyticsAPI'] = CaseAnalyticsAPI
globals()['LawFirmAnalyticsAPI'] = LawFirmAnalyticsAPI
globals()['NormOrganization'] = NormOrganization
from openapi_client.model.norm_law_firm import NormLawFirm


class TestNormLawFirm(unittest.TestCase):
    """NormLawFirm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNormLawFirm(self):
        """Test NormLawFirm"""
        # FIXME: construct object with mandatory attributes with example values
        # model = NormLawFirm()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
