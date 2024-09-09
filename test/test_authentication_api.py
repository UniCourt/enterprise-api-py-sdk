
from unicourt.sdk.Authentication import Authentication


class TestAuthentication:
    def test_list_all_token_ids():
        return Authentication.list_all_token_ids()

    def test_generate_new_token():
        response = Authentication.generate_new_token()
        Authentication.invalidate_token(token_id=response[0].token_id)
        return response

    def test_invalidate_token():
        response = Authentication.generate_new_token()
        return Authentication.invalidate_token(token_id=response[0].token_id)

    def test_invalidate_all_tokens():
        return Authentication.invalidate_all_tokens()
