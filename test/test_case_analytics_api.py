from unicourt.sdk.CaseAnalytics import CaseAnalytics


class TestCaseAnalytics:
    def test_get_case_count_analytics_by_area_of_law():
        return CaseAnalytics.get_case_count_analytics_by_area_of_law(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_case_class():
        return CaseAnalytics.get_case_count_analytics_by_case_class(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_case_filed_date():
        return CaseAnalytics.get_case_count_analytics_by_case_filed_date(
            page_number=1,
            group_by='Yearly',
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_case_type():
        return CaseAnalytics.get_case_count_analytics_by_case_type(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_case_type_group():
        return CaseAnalytics.get_case_count_analytics_by_case_type_group(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_court():
        return CaseAnalytics.get_case_count_analytics_by_court(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_court_location():
        return CaseAnalytics.get_case_count_analytics_by_court_location(
            page_number=1,
            q='courtId:"CORTV4vCEaKrhystBz" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_court_system():
        return CaseAnalytics.get_case_count_analytics_by_court_system(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_court_type():
        return CaseAnalytics.get_case_count_analytics_by_court_type(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_jurisdiction_geo():
        return CaseAnalytics.get_case_count_analytics_by_jurisdiction_geo(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_norm_attorney():
        return CaseAnalytics.get_case_count_analytics_by_norm_attorney(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_norm_judge():
        return CaseAnalytics.get_case_count_analytics_by_norm_judge(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_norm_law_firm():
        return CaseAnalytics.get_case_count_analytics_by_norm_law_firm(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_norm_party():
        return CaseAnalytics.get_case_count_analytics_by_norm_party(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_opposing_norm_attorney_for_a_norm_attorney():
        return CaseAnalytics.get_case_count_analytics_by_opposing_norm_attorney_for_a_norm_attorney(
            norm_attorney_id='NATYfwmXwRHS279WPY',
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm():
        return CaseAnalytics.get_case_count_analytics_by_opposing_norm_law_firm_for_a_norm_law_firm(
            norm_law_firm_id='NORGVHdWCDN7D6Ayn3',
            page_number=1,
            q='caseTypeId:"CTYPNjbKTN7Yfo2wdb" AND caseFiledDate:[2017-01-01T00:00:00+00:00 TO 2025-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_opposing_norm_party_for_a_norm_party():
        return CaseAnalytics.get_case_count_analytics_by_opposing_norm_party_for_a_norm_party(
            norm_party_id='NORGaSAiNLuy6J4uy5',
            page_number=1,
            q='caseTypeId:"CTYPiVk7MPJoRXGqMP" AND caseFiledDate:[2017-01-01T00:00:00+00:00 TO 2025-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_party_role():
        return CaseAnalytics.get_case_count_analytics_by_party_role(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_case_count_analytics_by_party_role_group():
        return CaseAnalytics.get_case_count_analytics_by_party_role_group(
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )
