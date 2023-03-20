from unicourt.api.pacer_api import PACERApi
from unicourt import utils
class PACER:

    @staticmethod
    def all_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search all courts within the PACER system for a particular case.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).all_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def all_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for the specified party across all PACER case filings.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).all_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def appeal_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for PACER cases filed in U.S. Courts of Appeals.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).appeal_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def appeal_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for the specified party across all PACER appeals cases.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).appeal_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def bankruptcy_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for Bankruptcy Courts.  


        Search for PACER cases filed in U.S. Bankruptcy Courts.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).bankruptcy_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def bankruptcy_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for the specified party in PACER bankruptcy filings.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).bankruptcy_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def civil_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for civil cases filed in PACER.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).civil_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def civil_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for the specified party in civil cases filed in PACER.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).civil_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def criminal_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for criminal cases in PACER.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).criminal_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def criminal_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for the specified party in PACER criminal cases.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).criminal_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def import_pacer_case_by_court_using_case_number(
        pacer_user_id,
        pacer_client_code,
        case_number,
        court_id,
        **kwargs
    ):

        """Find PACER Case for a requested Case Number and Court.  


        Import the specified case from PACER.    Workflow:     1.This API will return the Find Case results from the court site in a form of array of UniCourt Case Objects. These case objects will consists only Meta information of the case if not already present in the UniCourt Database.     2.To get the full updated case information one will have to request the caseUpdate API by passing the caseId.    Note:     1.Charges for Find Case in District, Bankruptcy and National Courts is free. Find case for Appeal Courts will be charged at minimum rate of $0.1. The fee charged by the court for find case can be found in the response of this API in the field courtFee.     2.The results of the search has less Meta information in case objects compared to the Meta information of cases found using the PCL search APIs.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).import_pacer_case_by_court_using_case_number(
        pacer_user_id,
        pacer_client_code,
        case_number,
        court_id,
        **kwargs
    )

    @staticmethod
    def multi_district_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for multidistrict litigation in PACER.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).multi_district_courts_pacer_case_locator_case_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )

    @staticmethod
    def multi_district_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    ):

        """PACER Case Locator Search API for All Courts.  


        Search for the specified party in multidistrict litigation in PACER.  

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return PACERApi(api_client).multi_district_courts_pacer_case_locator_party_search(
        pacer_user_id,
        pacer_client_code,
        **kwargs
    )
