from unicourt.sdk.Usage import Usage


class TestUsageAPI:
    def test_get_billing_cycles():
        return Usage.get_billing_cycles()

    def test_get_billing_usage_by_billing_cycle():
        return Usage.get_billing_usage_by_billing_cycle(
            billing_cycle="2023-01-25to2023-02-25")

    def test_get_daily_usage_by_date():
        # Get daily usage
        return Usage.get_daily_usage_by_date(date='2023-02-21')
