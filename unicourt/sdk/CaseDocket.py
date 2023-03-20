from unicourt.api.case_docket_api import CaseDocketApi
from unicourt import utils
class CaseDocket:

    @staticmethod
    def get_attorney_associated_parties(
        attorney_id,
        **kwargs
    ):

        """Gets Associated Party details for a requested Attorney ID.  


        Retrieve the parties represented by the attorney with the specified attorneyId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_attorney_associated_parties(
        attorney_id,
        **kwargs
    )

    @staticmethod
    def get_attorney_by_id(
        attorney_id,
        **kwargs
    ):

        """Gets details for a requested Attorney ID.  


        Retrieve the attorney with the specified attorneyId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_attorney_by_id(
        attorney_id,
        **kwargs
    )

    @staticmethod
    def get_case(
        case_id,
        **kwargs
    ):

        """Gets case information for a requested Case ID.  


        Retrieve the case with the specified caseId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_case(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_attorneys(
        case_id,
        **kwargs
    ):

        """Gets Attorneys for a requested Case ID.  


        Retrieve the attorneys in the case with the specified caseId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_case_attorneys(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_docket_entries(
        case_id,
        **kwargs
    ):

        """Gets Docket Entries for a requested Case ID.  


        Retrieve the docket entries in the case with the specified caseId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_case_docket_entries(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_hearings(
        case_id,
        **kwargs
    ):

        """Gets Hearings for a requested Case ID.  


        Gets Hearings for a requested Case ID.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_case_hearings(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_judges(
        case_id,
        **kwargs
    ):

        """Gets Judges for a requested Case ID.  


        Retrieve the judges involved in the specified case.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_case_judges(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_parties(
        case_id,
        **kwargs
    ):

        """Gets Parties for a requested Case ID.  


        Retrieve the parties involved in the case with the specified caseId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_case_parties(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_case_related_cases(
        case_id,
        **kwargs
    ):

        """Gets Related Cases for a requested Case ID.  


        Retrieve cases that UniCourt has identified as related to the case with the specified caseId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_case_related_cases(
        case_id,
        **kwargs
    )

    @staticmethod
    def get_judge_by_id(
        judge_id,
        **kwargs
    ):

        """Gets details for a requested Judge ID.  


        Retrieve the judge with the specified judgeId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_judge_by_id(
        judge_id,
        **kwargs
    )

    @staticmethod
    def get_party_associated_attorneys(
        party_id,
        **kwargs
    ):

        """Gets Associated Attorney details for a requested Party ID.  


        Retrieve the attorneys in the case with the specified partyId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_party_associated_attorneys(
        party_id,
        **kwargs
    )

    @staticmethod
    def get_party_by_id(
        party_id,
        **kwargs
    ):

        """Gets details for a requested Party ID.  


        Retrieve the party with the specified partyId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_party_by_id(
        party_id,
        **kwargs
    )

    @staticmethod
    def get_primary_documents_for_docket_entries(
        case_id,
        docket_number,
        **kwargs
    ):

        """Gets Primary Documents of Docket Entries.  


        Retrieve the primary documents in the case with the specified caseId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_primary_documents_for_docket_entries(
        case_id,
        docket_number,
        **kwargs
    )

    @staticmethod
    def get_secondary_documents_for_docket_entries(
        case_id,
        docket_number,
        **kwargs
    ):

        """Gets Secondary Documents of Docket Entries.  


        Retrieve the secondary documents in the case with the specified caseId value.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CaseDocketApi(api_client).get_secondary_documents_for_docket_entries(
        case_id,
        docket_number,
        **kwargs
    )
