from unicourt.sdk.AttorneyAnalytics import AttorneyAnalytics


class TestAttorneyAnalytics:
    def test_get_norm_attorney_by_id():
        return AttorneyAnalytics.get_norm_attorney_by_id(
            norm_attorney_id="NATYs4P6kDBkhKL8CF")

    def test_get_norm_law_firms_associated_with_norm_attorney():
        return AttorneyAnalytics.get_norm_law_firms_associated_with_norm_attorney(
            norm_attorney_id="NATYfwmXwRHS279WPY",
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_norm_judges_associated_with_norm_attorney():
        return AttorneyAnalytics.get_norm_judges_associated_with_norm_attorney(
            norm_attorney_id="NATYfwmXwRHS279WPY",
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_norm_parties_associated_with_norm_attorney():
        return AttorneyAnalytics.get_norm_parties_associated_with_norm_attorney(
            norm_attorney_id='NATYfwmXwRHS279WPY',
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_search_normalized_attorneys():
        return AttorneyAnalytics.search_normalized_attorneys(
            q='normAttorneyId:"NATYhUvNaef3b2iP8D"',
            page_number=1
        )

    def test_search_normalized_attorneys_by_id():
        return AttorneyAnalytics.search_normalized_attorneys_by_id(
            norm_attorney_search_id='ASRCJxUHYsgddr4Hc5',
            page_number=1
        )
