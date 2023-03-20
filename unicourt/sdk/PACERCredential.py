from unicourt.api.pacer_credential_api import PACERCredentialApi
from unicourt import utils
class PACERCredential:

    @staticmethod
    def add_pacer_credential(
        **kwargs
    ):

        """Add Pacer Credential.  


        Register PACER credentials with UniCourt.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERCredentialApi(api_client).add_pacer_credential(
        **kwargs
    )

    @staticmethod
    def get_pacer_credential(
        **kwargs
    ):

        """Get Pacer Credential List.  


        List registered PACER credentials.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERCredentialApi(api_client).get_pacer_credential(
        **kwargs
    )

    @staticmethod
    def get_pacer_credential_by_id(
        pacer_user_id,
        **kwargs
    ):

        """Get Pacer Credential for a requested pacer User Id.  


        Retrieve the PACER credentials for the specified PACER username.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERCredentialApi(api_client).get_pacer_credential_by_id(
        pacer_user_id,
        **kwargs
    )

    @staticmethod
    def remove_pacer_credential_by_id(
        pacer_user_id,
        **kwargs
    ):

        """Remove Pacer credential for a specific Pacer User Id.  


        De-register the PACER credentials for the specified PACER username.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERCredentialApi(api_client).remove_pacer_credential_by_id(
        pacer_user_id,
        **kwargs
    )
