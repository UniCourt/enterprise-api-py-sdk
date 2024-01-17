"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button>   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.case import Case
from openapi_client.model.case_update_pacer_options_response import CaseUpdatePacerOptionsResponse
from openapi_client.model.last_tracked_details import LastTrackedDetails
from openapi_client.model.schedule import Schedule
globals()['Case'] = Case
globals()['CaseUpdatePacerOptionsResponse'] = CaseUpdatePacerOptionsResponse
globals()['LastTrackedDetails'] = LastTrackedDetails
globals()['Schedule'] = Schedule
from openapi_client.model.case_track import CaseTrack


class TestCaseTrack(unittest.TestCase):
    """CaseTrack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCaseTrack(self):
        """Test CaseTrack"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CaseTrack()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()