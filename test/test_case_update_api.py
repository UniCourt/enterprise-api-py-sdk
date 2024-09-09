from unicourt.model.case_update_request import CaseUpdateRequest
from unicourt.sdk.CaseUpdate import CaseUpdate


class TestCaseUpdate:
    def test_update_case():
        return CaseUpdate.update_case(
            case_update_request=CaseUpdateRequest(
                case_id="CASEhq9d8b72d0800c"
            )
        )

    def test_get_case_update_by_case_id():
        return CaseUpdate.get_case_update_by_case_id(
            case_id="CASEhq9d8b72d0800c"
        )

    def test_get_case_updates():
        return CaseUpdate.get_case_updates(
            case_id="CASEak99a698ea5413",
            requested_date='2022-03-08T10:17:56+00:00',
            status="IN_PROGRESS",
            page_number=1,
        )
