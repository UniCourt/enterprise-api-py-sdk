from unicourt.sdk.PartyAnalytics import PartyAnalytics


class TestPartyAnalytics:
    def test_get_norm_attorneys_associated_with_norm_party():
        return PartyAnalytics.get_norm_attorneys_associated_with_norm_party(
            q='caseTypeId:"CTYPMrcrvoUeZHmsgk" AND caseFiledDate:[2017-01-01T00:00:00+00:00 TO 2025-11-30T00:00:00+00:00]',
            norm_party_id='NORGVppBo6fB829yV9',
            page_number=1
        )

    def test_get_norm_judges_associated_with_norm_party():
        return PartyAnalytics.get_norm_judges_associated_with_norm_party(
            norm_party_id='NORGVppBo6fB829yV9',
            page_number=1,
            q='caseTypeId:"CTYPMrcrvoUeZHmsgk" AND caseFiledDate:[2017-01-01T00:00:00+00:00 TO 2025-11-30T00:00:00+00:00]',
        )

    def test_get_norm_law_firms_associated_with_norm_party():
        return PartyAnalytics.get_norm_law_firms_associated_with_norm_party(
            norm_party_id='NORGVppBo6fB829yV9',
            page_number=1,
            q='caseTypeId:"CTYPMrcrvoUeZHmsgk" AND caseFiledDate:[2017-01-01T00:00:00+00:00 TO 2025-11-30T00:00:00+00:00]',
        )

    def test_get_norm_party_by_id():
        return PartyAnalytics.get_norm_party_by_id(
            norm_party_id='NORGVppBo6fB829yV9'
        )

    def test_search_normalized_parties():
        return PartyAnalytics.search_normalized_parties(
            q='normPartyId:"NORGJWPpNLekV7dKTm"'
        )

    def test_search_normalized_parties_by_id():
        return PartyAnalytics.search_normalized_parties_by_id(
            norm_party_search_id='PSRCUoacNCGj9ezvqf'
        )
