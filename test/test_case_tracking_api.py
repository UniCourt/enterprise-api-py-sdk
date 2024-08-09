from unicourt.model.case_track_request import CaseTrackRequest
from unicourt.model.case_track_schedule import CaseTrackSchedule
from unicourt.model.case_update_request import CaseUpdateRequest
from unicourt.sdk.CaseTracking import CaseTracking


class TestCaseTracking:
    def test_track_case():
        return CaseTracking.track_case(
            case_track_request=CaseTrackRequest(
                case_track_params=CaseUpdateRequest(
                    case_id="CASEhq9d8b72d0800c"
                ),
                schedule=CaseTrackSchedule(
                    type="weekly",
                    days=[1, 3, 5],
                ),
            )
        )

    def test_get_case_track_by_id():
        return CaseTracking.get_case_track_by_id(
            case_id="CASEhq9d8b72d0800c"
        )

    def test_get_case_tracks():
        return CaseTracking.get_case_tracks(
            last_fetch_date='2022-03-08T10:17:56+00:00',
            last_fetch_date_with_updates='2022-03-08T10:17:56+00:00',
            page_number=1
        )

    def get_remove_case_track_by_id():
        return CaseTracking.remove_case_track_by_id(
            case_id="CASEhq9d8b72d0800c"
        )
