import os
from unicourt.model.pacer_credential_request import PacerCredentialRequest
from unicourt.sdk.PACERCredential import PACERCredential


class TestPacerCredentials:
    def test_add_pacer_credential():
        pacer_credential_request = PacerCredentialRequest(
            pacer_user_id=os.getenv("PACER_USER_ID"),
            default_pacer_client_code=os.getenv("PACER_CLIENT_CODE"),
            password="TEST_PASSWORD",
        )
        return PACERCredential.add_pacer_credential(
            pacer_credential_request=pacer_credential_request)

    def test_get_pacer_credential():
        return PACERCredential.get_pacer_credential(
            page_number=1)

    def test_get_pacer_credential_by_id():
        return PACERCredential.get_pacer_credential_by_id(
            pacer_user_id=os.getenv("PACER_USER_ID"),
        )

    def test_remove_pacer_credential_by_id():
        return PACERCredential.remove_pacer_credential_by_id(
            pacer_user_id=os.getenv("PACER_USER_ID")
        )
