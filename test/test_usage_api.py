from unicourt.sdk.Usage import Usage


class TestUsageAPI:
    def test_get_billing_cycles():
        return Usage.get_billing_cycles()

    def test_get_billing_usage_by_billing_cycle():
        billing_obj, _ = Usage.get_billing_cycles()
        billing_cycle_date = billing_obj.billing_cycle_array[0]
        return Usage.get_billing_usage_by_billing_cycle(
            billing_cycle=billing_cycle_date)

    def test_get_daily_usage_by_date():
        return Usage.get_daily_usage_by_date(date='2023-02-21')
