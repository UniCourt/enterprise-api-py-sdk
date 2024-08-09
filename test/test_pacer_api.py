import os
from unicourt.sdk.PACER import PACER


class TestPacer:
    def test_all_courts_pacer_case_locator_case_search():
        return PACER.all_courts_pacer_case_locator_case_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            case_number="12-1234")

    def test_all_courts_pacer_case_locator_party_search():
        return PACER.all_courts_pacer_case_locator_party_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            last_name="smith",
            case_number="21-119"
        )

    def test_appeal_courts_pacer_case_locator_case_search():
        return PACER.appeal_courts_pacer_case_locator_case_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            case_number="12-1234"
        )

    def test_appeal_courts_pacer_case_locator_party_search():
        return PACER.appeal_courts_pacer_case_locator_party_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            last_name="12-1234"
        )

    def test_bankruptcy_courts_pacer_case_locator_case_search():
        return PACER.bankruptcy_courts_pacer_case_locator_case_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            case_number="12-1234"
        )

    def test_bankruptcy_courts_pacer_case_locator_party_search():
        return PACER.bankruptcy_courts_pacer_case_locator_party_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            last_name="smith"
        )

    def test_civil_courts_pacer_case_locator_case_search():
        return PACER.civil_courts_pacer_case_locator_case_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            case_number="12-1234"
        )

    def test_civil_courts_pacer_case_locator_party_search():
        return PACER.civil_courts_pacer_case_locator_party_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            last_name="smith"
        )

    def test_criminal_courts_pacer_case_locator_case_search():
        return PACER.criminal_courts_pacer_case_locator_case_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            case_number="12-1234"
        )

    def test_criminal_courts_pacer_case_locator_party_search():
        return PACER.criminal_courts_pacer_case_locator_party_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            last_name="smith"
        )

    def test_import_pacer_case_by_court_using_case_number():
        return PACER.import_pacer_case_by_court_using_case_number(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            case_number="2:15-mc-12345",
            court_id="CORTjF63b8Z4d2i9UB"
        )

    def test_multi_district_courts_pacer_case_locator_case_search():
        return PACER.multi_district_courts_pacer_case_locator_case_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            case_number="12-1234"
        )

    def test_multi_district_courts_pacer_case_locator_party_search():
        return PACER.multi_district_courts_pacer_case_locator_party_search(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            last_name="smith"
        )
