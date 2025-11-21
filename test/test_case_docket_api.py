from unicourt.sdk.CaseDocket import CaseDocket


class TestCaseDocket:
    def test_get_attorney_associated_parties():
        return CaseDocket.get_attorney_associated_parties(
            attorney_id='ATTYgu01be2e4de654'
        )

    def test_get_attorney_by_id():
        return CaseDocket.get_attorney_by_id(
            attorney_id='ATTYgu01be2e4de654'
        )

    def test_get_case():
        return CaseDocket.get_case(
            case_id='CASEgfe4e3a490fe24',
        )

    def test_get_case_attorneys():
        return CaseDocket.get_case_attorneys(
            case_id='CASEgq5943bd47a6d2',
            is_visible=True
        )

    def test_get_case_docket_entries():
        return CaseDocket.get_case_docket_entries(
            case_id='CASEgle0bf14b74a96'
        )

    def test_get_case_hearings():
        return CaseDocket.get_case_hearings(
            case_id='CASEar3c45901ef267'
        )

    def test_get_case_judges():
        return CaseDocket.get_case_judges(
            case_id='CASEgq6e6ea66cd91d',
            is_visible=True
        )

    def test_get_case_parties():
        return CaseDocket.get_case_parties(
            case_id='CASEgq8f4cea2d8e1a',
            is_visible=True
        )

    def test_get_case_related_cases():
        return CaseDocket.get_case_related_cases(
            case_id='CASEba328623913f9f'
        )

    def test_get_judge_by_id():
        return CaseDocket.get_judge_by_id(
            judge_id='JUDGgue04d2894de7a'
        )

    def test_get_party_associated_attorneys():
        return CaseDocket.get_party_associated_attorneys(
            party_id='PRTYgu537f3901f406',
        )

    def test_get_party_by_id():
        return CaseDocket.get_party_by_id(
            party_id='PRTYgla171a8952aed'
        )

    def test_get_primary_documents_for_docket_entries():
        return CaseDocket.get_primary_documents_for_docket_entries(
            case_id='CASEgued96d541f794',
            docket_number=1
        )

    def test_get_secondary_documents_for_docket_entries():
        return CaseDocket.get_secondary_documents_for_docket_entries(
            case_id='CASEgq5da86597e9a4',
            docket_number=1
        )
