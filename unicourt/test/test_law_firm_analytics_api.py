from unicourt.sdk.LawFirmAnalytics import LawFirmAnalytics


class TestLawFirmAnalytics:
    def test_get_norm_attorneys_associated_with_norm_law_firm():
        return LawFirmAnalytics.get_norm_attorneys_associated_with_norm_law_firm(
            norm_law_firm_id='NORGrPmQyLdx9NGHcT',
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_norm_judges_associated_with_norm_law_firm():
        return LawFirmAnalytics.get_norm_judges_associated_with_norm_law_firm(
            norm_law_firm_id='NORGrPmQyLdx9NGHcT',
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_get_norm_law_firm_by_id():
        return LawFirmAnalytics.get_norm_law_firm_by_id(
            norm_law_firm_id='NORGDiJQPjeed2mtvx'
        )

    def test_get_norm_parties_associated_with_norm_law_firm():
        return LawFirmAnalytics.get_norm_parties_associated_with_norm_law_firm(
            norm_law_firm_id='NORGrPmQyLdx9NGHcT',
            page_number=1,
            q='caseTypeId:"CTYPATMYyaJekdgj2c" AND caseFiledDate:[2017-01-01T00:00:00+00:00TO2021-11-30T00:00:00+00:00]'
        )

    def test_search_normalized_law_firms():
        return LawFirmAnalytics.search_normalized_law_firms(
            q='NORGrPmQyLdx9NGHcT'
        )

    def test_search_normalized_law_firms_by_id():
        return LawFirmAnalytics.search_normalized_law_firms_by_id(
            norm_law_firm_search_id='LSRCeCT9pC3maopkW7'
        )


def main():
    TestLawFirmAnalytics().run()


if __name__ == "__main__":
    main()
