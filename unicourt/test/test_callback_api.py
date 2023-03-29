from unicourt.sdk.Callback import Callback


class TestCallBack:
    def test_get_callbacks():
        return Callback.get_callbacks(
            date='2022-03-08T00:00:00+00:00',
            status='IN_PROGRESS'
        )
