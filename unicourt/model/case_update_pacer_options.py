"""
    UniCourt Enterprise APIs

    <button><a href=\"/enterpriseapi/download/UniCourt-Enterprise-API-Spec.yaml\" >Download UniCourt Enterprise APIs Specification</a></button>   # noqa: E501

    The version of the OpenAPI document: 
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from unicourt.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from unicourt.exceptions import ApiAttributeError


def lazy_import():
    from unicourt.model.case_update_pacer_options_additional_page_array_inner import CaseUpdatePacerOptionsAdditionalPageArrayInner
    globals()['CaseUpdatePacerOptionsAdditionalPageArrayInner'] = CaseUpdatePacerOptionsAdditionalPageArrayInner


class CaseUpdatePacerOptions(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('refresh_type',): {
            'None': None,
            'FETCHNEWDOCKETENTRIES': "fetchNewDocketEntries",
            'FETCHALLDOCKETENTRIES': "fetchAllDocketEntries",
        },
    }

    validations = {
        ('pacer_user_id',): {
            'max_length': 40,
            'min_length': 6,
        },
        ('pacer_client_code',): {
            'max_length': 32,
            'min_length': 0,
        },
        ('fetch_participants_if_older_than_days',): {
            'inclusive_maximum': 100,
            'inclusive_minimum': 0,
        },
        ('refresh_type',): {
            'max_length': 21,
            'min_length': 21,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'pacer_user_id': (str,),  # noqa: E501
            'pacer_client_code': (str, none_type,),  # noqa: E501
            'fetch_participants_if_older_than_days': (int,),  # noqa: E501
            'refresh_type': (str, none_type,),  # noqa: E501
            'additional_page_array': ([CaseUpdatePacerOptionsAdditionalPageArrayInner], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'pacer_user_id': 'pacerUserId',  # noqa: E501
        'pacer_client_code': 'pacerClientCode',  # noqa: E501
        'fetch_participants_if_older_than_days': 'fetchParticipantsIfOlderThanDays',  # noqa: E501
        'refresh_type': 'refreshType',  # noqa: E501
        'additional_page_array': 'additionalPageArray',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, pacer_user_id, *args, **kwargs):  # noqa: E501
        """CaseUpdatePacerOptions - a model defined in OpenAPI

        Args:
            pacer_user_id (str): **Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.**

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            pacer_client_code (str, none_type): PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code.. [optional]  # noqa: E501
            fetch_participants_if_older_than_days (int): **Currently this option is only applicable for Federal PACER cases. You can limit how often parties and attorneys for a PACER case are fetched to reduce your PACER fees. If you are tracking cases daily or hourly you could easily end up with a large PACER bill.**  **Use Case: Cases are typically updated to check for new docket entry filings. However every update to PACER case costs money. Participants for a case change less often than docket entry filings. So fetching participants for every update might result in unnecessary PACER costs; especially on cases which have a lot of parties and attorneys. So instead of getting charged the minimum cost of $0.10 for an update which might have had few docket entries, you could end up spending $3 for every update because there were a lot of parties for that case that were also fetched.**  **With this option you can choose when to fetch parties for case based on when was it last fetched.** You can limit how often this participants are fetched in a PACER case to keep your PACER costs under control.  Min days is 0 and Max days is 100.  Example: 1.  Specifying a value of 0 ensures that participants are fetched from PACER for this case update irrespective of when the participants were last fetched. 2.  Specifying a value of 30 ensures that participants are fetched from PACER for this case update only if the last fetch was older than 30 days. . [optional] if omitted the server will use the default value of 0  # noqa: E501
            refresh_type (str, none_type): This flag determines whether to pull only new or pull all the docket entries for a PACER case being requested.  Only one of the two values is allowed: -   fetchNewDocketEntries:     >   Updates the PACER case with only new docket entries that have been added after the previous update of the case being requested. -   fetchAllDocketEntries:     >   Updates the PACER case by re-parsing all dockets from #1 till latest docket entry available. . [optional] if omitted the server will use the default value of "fetchNewDocketEntries"  # noqa: E501
            additional_page_array ([CaseUpdatePacerOptionsAdditionalPageArrayInner], none_type): Currently this option is only applicable for Federal PACER cases. The default behavior of the Case Update is to fetch the Docket Report from PACER which includes the parties and attorneys too.  However if you need to fetch information for other pages in PACER you will need to specify it here. - associatedCases: > This will fetch the Associated Cases page in PACER if available. This page consists of related cases especially applicable for Multi-District Litigation cases and Member Cases. Including this option will internally link all related cases in our system. Data from this page will be available via the Related Cases API. - caseSummary: > This will fetch the Case Summary page in PACER if available. This page consists of additional case info which is not present in the Docket Report page. Data from this page will be structured and available as response in the Case API’s ```additional_info``` field. - listOfCreditors: > This page will fetch the “List Of Creditors” page for PACER Bankruptcy cases of case type \"bk\". Note that this page cannot be extracted for Bankruptcy cases of case type \"ap\" (Adversary Proceedings). This page consists of the Creditor information like the name and address of the Creditors. Data from this page will be structured and available as response in the Case API. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.pacer_user_id = pacer_user_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, pacer_user_id, *args, **kwargs):  # noqa: E501
        """CaseUpdatePacerOptions - a model defined in OpenAPI

        Args:
            pacer_user_id (str): **Your PACER credentials username. This is mandatory when a PACER Case is being requested in the API. For Non PACER cases this is not mandatory. Suppose your request consists of Non PACER and PACER Cases then this needs to be passed becuase you are requesting a PACER case too.**

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            pacer_client_code (str, none_type): PACER Client Code. This is mandatory if your setting in PACER website is set to True for required client code.. [optional]  # noqa: E501
            fetch_participants_if_older_than_days (int): **Currently this option is only applicable for Federal PACER cases. You can limit how often parties and attorneys for a PACER case are fetched to reduce your PACER fees. If you are tracking cases daily or hourly you could easily end up with a large PACER bill.**  **Use Case: Cases are typically updated to check for new docket entry filings. However every update to PACER case costs money. Participants for a case change less often than docket entry filings. So fetching participants for every update might result in unnecessary PACER costs; especially on cases which have a lot of parties and attorneys. So instead of getting charged the minimum cost of $0.10 for an update which might have had few docket entries, you could end up spending $3 for every update because there were a lot of parties for that case that were also fetched.**  **With this option you can choose when to fetch parties for case based on when was it last fetched.** You can limit how often this participants are fetched in a PACER case to keep your PACER costs under control.  Min days is 0 and Max days is 100.  Example: 1.  Specifying a value of 0 ensures that participants are fetched from PACER for this case update irrespective of when the participants were last fetched. 2.  Specifying a value of 30 ensures that participants are fetched from PACER for this case update only if the last fetch was older than 30 days. . [optional] if omitted the server will use the default value of 0  # noqa: E501
            refresh_type (str, none_type): This flag determines whether to pull only new or pull all the docket entries for a PACER case being requested.  Only one of the two values is allowed: -   fetchNewDocketEntries:     >   Updates the PACER case with only new docket entries that have been added after the previous update of the case being requested. -   fetchAllDocketEntries:     >   Updates the PACER case by re-parsing all dockets from #1 till latest docket entry available. . [optional] if omitted the server will use the default value of "fetchNewDocketEntries"  # noqa: E501
            additional_page_array ([CaseUpdatePacerOptionsAdditionalPageArrayInner], none_type): Currently this option is only applicable for Federal PACER cases. The default behavior of the Case Update is to fetch the Docket Report from PACER which includes the parties and attorneys too.  However if you need to fetch information for other pages in PACER you will need to specify it here. - associatedCases: > This will fetch the Associated Cases page in PACER if available. This page consists of related cases especially applicable for Multi-District Litigation cases and Member Cases. Including this option will internally link all related cases in our system. Data from this page will be available via the Related Cases API. - caseSummary: > This will fetch the Case Summary page in PACER if available. This page consists of additional case info which is not present in the Docket Report page. Data from this page will be structured and available as response in the Case API’s ```additional_info``` field. - listOfCreditors: > This page will fetch the “List Of Creditors” page for PACER Bankruptcy cases of case type \"bk\". Note that this page cannot be extracted for Bankruptcy cases of case type \"ap\" (Adversary Proceedings). This page consists of the Creditor information like the name and address of the Creditors. Data from this page will be structured and available as response in the Case API. . [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.pacer_user_id = pacer_user_id
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")