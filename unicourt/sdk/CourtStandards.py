from unicourt.api.court_standards_api import CourtStandardsApi
from unicourt import utils
class CourtStandards:

    @staticmethod
    def get_appeal_courts_for_court(
        court_id,
        **kwargs
    ):

        """Appeal Court Objects for given courtId.  


        Retrieve the appeals courts associated with the specified court.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_appeal_courts_for_court(
        court_id,
        **kwargs
    )

    @staticmethod
    def get_area_of_law(
        area_of_law_id,
        **kwargs
    ):

        """AreaOfLaw Object for the given AreaOfLaw Id.  


        Retrieve the specified area of law.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_area_of_law(
        area_of_law_id,
        **kwargs
    )

    @staticmethod
    def get_areas_of_law(
        **kwargs
    ):

        """AreaOfLaw Object.  


        The keyword expression targeting the desired area of law.   ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> AreaOfLawQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_areas_of_law(
        **kwargs
    )

    @staticmethod
    def get_attorney_representation_type(
        attorney_representation_type_id,
        **kwargs
    ):

        """Attorney Representation Type Object for the given attorneyRepresentationTypeId.  


        Retrieve the specified attorney representation type.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_attorney_representation_type(
        attorney_representation_type_id,
        **kwargs
    )

    @staticmethod
    def get_attorney_representation_types(
        **kwargs
    ):

        """Attorney Representation Type Object.  


        Retrieve an attorney representation type using a keyword expression. Keyword expressions should be constructed according to the rules given above. ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyRepresentationTypeQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_attorney_representation_types(
        **kwargs
    )

    @staticmethod
    def get_attorney_type(
        attorney_type_id,
        **kwargs
    ):

        """Attorney Type Object for given Attorney Type Id.  


        Retrieve a specified attorney type object.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_attorney_type(
        attorney_type_id,
        **kwargs
    )

    @staticmethod
    def get_attorney_types(
        **kwargs
    ):

        """Attorney Type Object.  


        Retrieve an attorney type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> AttorneyTypeQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_attorney_types(
        **kwargs
    )

    @staticmethod
    def get_case_class(
        case_class_id,
        **kwargs
    ):

        """Case Class Object for the given Case Class Id.  


        Retrieve the specified case class.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_class(
        case_class_id,
        **kwargs
    )

    @staticmethod
    def get_case_relationship_type(
        case_relationship_type_id,
        **kwargs
    ):

        """Case Relationship Type Object for the given caseRelationshipTypeId.  


        Retrieve the specified case relationship type.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_relationship_type(
        case_relationship_type_id,
        **kwargs
    )

    @staticmethod
    def get_case_relationship_types(
        **kwargs
    ):

        """Case Relationship Type Object.  


        Retrieve an case relationship type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseRelationshipTypeQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_relationship_types(
        **kwargs
    )

    @staticmethod
    def get_case_status(
        case_status_id,
        **kwargs
    ):

        """Returns the caseStatus information for the given caseStatusId.  


        Retrieve the specified case status.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_status(
        case_status_id,
        **kwargs
    )

    @staticmethod
    def get_case_status_group(
        case_status_group_id,
        **kwargs
    ):

        """Returns the caseStatusGroup information for the given caseStatusGroupId.  


        Retrieve the specified case status group.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_status_group(
        case_status_group_id,
        **kwargs
    )

    @staticmethod
    def get_case_status_groups(
        **kwargs
    ):

        """Case Status Group Object.  


        Retrieve a case status group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseStatusGroupQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_status_groups(
        **kwargs
    )

    @staticmethod
    def get_case_type(
        case_type_id,
        **kwargs
    ):

        """CaseType Object for given Case Type Id.  


        Retrieve the specified case type.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_type(
        case_type_id,
        **kwargs
    )

    @staticmethod
    def get_case_type_group(
        case_type_group_id,
        **kwargs
    ):

        """CaseType Group for the given CaseType Group Id.  


        Retrieve the specified case type group.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_type_group(
        case_type_group_id,
        **kwargs
    )

    @staticmethod
    def get_case_type_groups(
        **kwargs
    ):

        """CaseTypeGroup Object.  


        Retrieve one or more case type groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeGroupQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_type_groups(
        **kwargs
    )

    @staticmethod
    def get_case_types(
        **kwargs
    ):

        """Case Type Object.  


        Retrieve one or more case types using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseTypeQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_case_types(
        **kwargs
    )

    @staticmethod
    def get_cases_class(
        **kwargs
    ):

        """Case Class Object.  


        Retrieve one or more case classes using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CaseClassQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_cases_class(
        **kwargs
    )

    @staticmethod
    def get_cases_status(
        **kwargs
    ):

        """Case Status Object.  


        Retrieve a case status using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below Schema section. Schema --> CaseStatusQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_cases_status(
        **kwargs
    )

    @staticmethod
    def get_cause_of_action(
        cause_of_action_id,
        **kwargs
    ):

        """CauseOfAction Object for the given causeOfActionId.  


        Retrieve the specified cause of action.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_cause_of_action(
        cause_of_action_id,
        **kwargs
    )

    @staticmethod
    def get_cause_of_action_additional_data(
        cause_of_action_additional_data_id,
        **kwargs
    ):

        """CauseOfActionAdditionalData Object for the given causeOfActionAdditionalDataId.  


        Retrieve the specified cause of action additional data.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_cause_of_action_additional_data(
        cause_of_action_additional_data_id,
        **kwargs
    )

    @staticmethod
    def get_cause_of_action_group(
        cause_of_action_group_id,
        **kwargs
    ):

        """CauseOfActionGroup Object for the given causeOfActionGroupId.  


        Retrieve the specified cause of action group.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_cause_of_action_group(
        cause_of_action_group_id,
        **kwargs
    )

    @staticmethod
    def get_causes_of_action(
        **kwargs
    ):

        """CauseOfAction Object.  


        Retrieve a cause of action using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_causes_of_action(
        **kwargs
    )

    @staticmethod
    def get_causes_of_action_additional_data(
        **kwargs
    ):

        """CauseOfActionAdditionaData Object.  


        Retrieve a cause of action additional data using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionAdditionalDataQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_causes_of_action_additional_data(
        **kwargs
    )

    @staticmethod
    def get_causes_of_action_group(
        **kwargs
    ):

        """CauseOfActionGroup Object.  


        Retrieve a cause of action group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CauseOfActionGroupQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_causes_of_action_group(
        **kwargs
    )

    @staticmethod
    def get_charge(
        charge_id,
        **kwargs
    ):

        """Charge Object for the given chargeId.  


        Retrieve the specified charge.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charge(
        charge_id,
        **kwargs
    )

    @staticmethod
    def get_charge_additional_data(
        charge_additional_data_id,
        **kwargs
    ):

        """Charge Additional Data Object for the given chargeAdditionalDataId.  


        Retrieve the specified charge additional data.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charge_additional_data(
        charge_additional_data_id,
        **kwargs
    )

    @staticmethod
    def get_charge_degree(
        charge_degree_id,
        **kwargs
    ):

        """ChargeDegree Object for the given chargeDegreeId.  


        Retrieve the specified charge degree.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charge_degree(
        charge_degree_id,
        **kwargs
    )

    @staticmethod
    def get_charge_group(
        charge_group_id,
        **kwargs
    ):

        """Charge Group Object for the given chargeGroupId.  


        Retrieve the specified charge group.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charge_group(
        charge_group_id,
        **kwargs
    )

    @staticmethod
    def get_charge_groups(
        **kwargs
    ):

        """Charge Group Object.  


        Retrieve one or more charge groups using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeGroupQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charge_groups(
        **kwargs
    )

    @staticmethod
    def get_charge_severity(
        charge_severity_id,
        **kwargs
    ):

        """ChargeSeverity Object for the given chargeSeverityId.  


        Retrieve the specified charge severity.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charge_severity(
        charge_severity_id,
        **kwargs
    )

    @staticmethod
    def get_charges(
        **kwargs
    ):

        """Charge Object.  


        Retrieve one or more charges using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charges(
        **kwargs
    )

    @staticmethod
    def get_charges_additional_data(
        **kwargs
    ):

        """Charge Additional Data Object.  


        Retrieve additional information on a charge using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeAdditionalDataQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charges_additional_data(
        **kwargs
    )

    @staticmethod
    def get_charges_degree(
        **kwargs
    ):

        """ChargeDegree Object.  


        Retrieve a charge degree using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeDegreeQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charges_degree(
        **kwargs
    )

    @staticmethod
    def get_charges_severity(
        **kwargs
    ):

        """ChargeSeverity Object.  


        Retrieve a charge severity using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> ChargeSeverityQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_charges_severity(
        **kwargs
    )

    @staticmethod
    def get_court(
        court_id,
        **kwargs
    ):

        """Court Object for given courtId.  


        Retrieve information about a specified court.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court(
        court_id,
        **kwargs
    )

    @staticmethod
    def get_court_location(
        court_location_id,
        **kwargs
    ):

        """Courthouse Object for given Court Location Id.  


        Contains the Court Location Object.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court_location(
        court_location_id,
        **kwargs
    )

    @staticmethod
    def get_court_locations(
        **kwargs
    ):

        """Courthouse Object.  


        Retrieve the specified court location or court locations.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtLocationQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court_locations(
        **kwargs
    )

    @staticmethod
    def get_court_locations_for_court(
        court_id,
        **kwargs
    ):

        """Associated Court Location for given courtId.  


        Retrieve the court locations associated with the specified court.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court_locations_for_court(
        court_id,
        **kwargs
    )

    @staticmethod
    def get_court_service_status(
        court_service_status_id,
        **kwargs
    ):

        """Court Service Status Object for the given courtServiceStatusId.  


        Retrieve the court status of the specified court.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court_service_status(
        court_service_status_id,
        **kwargs
    )

    @staticmethod
    def get_court_system(
        court_system_id,
        **kwargs
    ):

        """Court System Object for given courtSystemId.  


        Retrieve the specified court system.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court_system(
        court_system_id,
        **kwargs
    )

    @staticmethod
    def get_court_systems(
        **kwargs
    ):

        """Court System Objects.  


        Retrieve information about the specified court system or court systems.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|          | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtSystemQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court_systems(
        **kwargs
    )

    @staticmethod
    def get_court_type(
        court_type_id,
        **kwargs
    ):

        """Court Type Object for given courtTypeId.  


        Retrieve the information concerning the specific court type.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court_type(
        court_type_id,
        **kwargs
    )

    @staticmethod
    def get_court_types(
        **kwargs
    ):

        """Court Type Objects.  


        Retrieve court types recognized by UniCourt.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|          | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtTypeQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_court_types(
        **kwargs
    )

    @staticmethod
    def get_courts(
        **kwargs
    ):

        """Court Objects.  


        Retrieve information about a specified court or courts.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------|          | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_courts(
        **kwargs
    )

    @staticmethod
    def get_courts_for_court_location(
        court_location_id,
        **kwargs
    ):

        """Associated Court for given Court Location.  


        Retrieve the courts associated with the specified court location.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_courts_for_court_location(
        court_location_id,
        **kwargs
    )

    @staticmethod
    def get_courts_for_jurisdiction_geo(
        jurisdiction_geo_id,
        **kwargs
    ):

        """Associated Court for given Jurisdiction Geo.  


        Returns Associated Court for given Jurisdiction Geo.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_courts_for_jurisdiction_geo(
        jurisdiction_geo_id,
        **kwargs
    )

    @staticmethod
    def get_courts_service_status(
        **kwargs
    ):

        """Court Service Status Object.  


        Retrieve the status of one or more courts using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> CourtServiceStatusQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_courts_service_status(
        **kwargs
    )

    @staticmethod
    def get_judge_type(
        judge_type_id,
        **kwargs
    ):

        """Judge Type Object for the given judgeTypeId.  


        Retrieve the specified judge type.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_judge_type(
        judge_type_id,
        **kwargs
    )

    @staticmethod
    def get_judge_types(
        **kwargs
    ):

        """Judge Type Object.  


        Retrieve a judge type using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JudgeTypeQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_judge_types(
        **kwargs
    )

    @staticmethod
    def get_jurisdiction_geo(
        jurisdiction_geo_id,
        **kwargs
    ):

        """Jurisdiction Geo Object for given Jurisdiction Geo Id.  


        Retrieve the specified jurisdiction geography.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_jurisdiction_geo(
        jurisdiction_geo_id,
        **kwargs
    )

    @staticmethod
    def get_jurisdiction_geo_for_court(
        court_id,
        **kwargs
    ):

        """Jurisdiction Geo Objects for given courtId.  


        Retrieve the jurisdiction geography object for the specified court.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_jurisdiction_geo_for_court(
        court_id,
        **kwargs
    )

    @staticmethod
    def get_jurisdictions_geo(
        **kwargs
    ):

        """Jurisdiction Geo Object.  


        Retrieve one or more jurisdiction geographies using a keyword expression.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> JurisdictionGeoQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_jurisdictions_geo(
        **kwargs
    )

    @staticmethod
    def get_party_role(
        party_role_id,
        **kwargs
    ):

        """Party Role Object.  


        Retrieve the specified party role.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_party_role(
        party_role_id,
        **kwargs
    )

    @staticmethod
    def get_party_role_group(
        party_role_group_id,
        **kwargs
    ):

        """Party Role Group Object.  


        Retrieve the specified party role group.   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_party_role_group(
        party_role_group_id,
        **kwargs
    )

    @staticmethod
    def get_party_role_groups(
        **kwargs
    ):

        """Party Role Group Object.  


        Retrieve a party role group using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleGroupQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_party_role_groups(
        **kwargs
    )

    @staticmethod
    def get_party_roles(
        **kwargs
    ):

        """Party Role Object.  


        Retrieve a party role using a keyword expression. Keyword expressions should be constructed according to the rules given above.  ## Logical Operators | Connector | Description  | Example | | ------| ------|------| | **AND** |Find data containing all connected terms.|**google AND facebook**| | **OR**  |Find data containing any connected term.| **order OR decision**| | **NOT** |Exclude data.| **google NOT apple**.| | **“[phrase]”** |Find an exact phrase.| **\"Google Inc”** | | **( … )** |Parenthesis may be used to group sets of terms of connectors.| **google (facebook OR apple)**.|  ### All Filter Query parameters supported for this API can be found in below schema section. Schema --> PartyRoleQueryObject   

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        """
        with utils.api_client() as api_client:
            return CourtStandardsApi(api_client).get_party_roles(
        **kwargs
    )
