from unicourt.sdk.CourtAvailability import CourtAvailability


class TestCourtAvailability:
    def test_get_court_coverage():
        return CourtAvailability.get_court_coverage(
            court_id="CORTV4vCEaKrhystBz"
        )
