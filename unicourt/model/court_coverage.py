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
    from unicourt.model.case_class_coverage import CaseClassCoverage
    from unicourt.model.court import Court
    globals()['CaseClassCoverage'] = CaseClassCoverage
    globals()['Court'] = Court


class CourtCoverage(ModelNormal):
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
    }

    validations = {
        ('object',): {
            'max_length': 13,
            'min_length': 13,
        },
        ('last_update_count_date',): {
            'max_length': 25,
            'min_length': 25,
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

    _nullable = True

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
            'object': (str,),  # noqa: E501
            'last_update_count_date': (str,),  # noqa: E501
            'court': (Court,),  # noqa: E501
            'total_case_count': (int,),  # noqa: E501
            'total_cases_in_last_thirty_days_count': (int,),  # noqa: E501
            'total_free_case_document_count': (int,),  # noqa: E501
            'total_free_case_documents_in_last_thirty_days_count': (int,),  # noqa: E501
            'total_paid_case_document_count': (int,),  # noqa: E501
            'total_paid_case_documents_in_last_thirty_days_count': (int,),  # noqa: E501
            'total_case_document_in_library_count': (int,),  # noqa: E501
            'total_case_document_in_library_in_last_thirty_days_count': (int,),  # noqa: E501
            'case_class_coverage_array': ([CaseClassCoverage],),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'object': 'object',  # noqa: E501
        'last_update_count_date': 'lastUpdateCountDate',  # noqa: E501
        'court': 'court',  # noqa: E501
        'total_case_count': 'totalCaseCount',  # noqa: E501
        'total_cases_in_last_thirty_days_count': 'totalCasesInLastThirtyDaysCount',  # noqa: E501
        'total_free_case_document_count': 'totalFreeCaseDocumentCount',  # noqa: E501
        'total_free_case_documents_in_last_thirty_days_count': 'totalFreeCaseDocumentsInLastThirtyDaysCount',  # noqa: E501
        'total_paid_case_document_count': 'totalPaidCaseDocumentCount',  # noqa: E501
        'total_paid_case_documents_in_last_thirty_days_count': 'totalPaidCaseDocumentsInLastThirtyDaysCount',  # noqa: E501
        'total_case_document_in_library_count': 'totalCaseDocumentInLibraryCount',  # noqa: E501
        'total_case_document_in_library_in_last_thirty_days_count': 'totalCaseDocumentInLibraryInLastThirtyDaysCount',  # noqa: E501
        'case_class_coverage_array': 'caseClassCoverageArray',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, last_update_count_date, court, total_case_count, total_cases_in_last_thirty_days_count, total_free_case_document_count, total_free_case_documents_in_last_thirty_days_count, total_paid_case_document_count, total_paid_case_documents_in_last_thirty_days_count, total_case_document_in_library_count, total_case_document_in_library_in_last_thirty_days_count, case_class_coverage_array, *args, **kwargs):  # noqa: E501
        """CourtCoverage - a model defined in OpenAPI

        Args:
            last_update_count_date (str): Date when it was last updated.
            court (Court):
            total_case_count (int): Total Cases for a specific court.
            total_cases_in_last_thirty_days_count (int): Total Cases in last 30 days that were added to UniCourt
            total_free_case_document_count (int): Total Free Case Documents for a specific court.
            total_free_case_documents_in_last_thirty_days_count (int): Total Free Case Documents in last 30 days that were added to UniCourt
            total_paid_case_document_count (int): Total Paid Case Documents for a specific court.
            total_paid_case_documents_in_last_thirty_days_count (int): Total Paid Case Documents in last 30 days that were added to UniCourt
            total_case_document_in_library_count (int): Count of total Case Documents added in UniCourt Library.
            total_case_document_in_library_in_last_thirty_days_count (int): Count of total Case Documents added in UniCourt Library in last 30 days
            case_class_coverage_array ([CaseClassCoverage]):

        Keyword Args:
            object (str): Name of the object. defaults to "CourtCoverage"  # noqa: E501
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
        """

        object = kwargs.get('object', "CourtCoverage")
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

        self.object = object
        self.last_update_count_date = last_update_count_date
        self.court = court
        self.total_case_count = total_case_count
        self.total_cases_in_last_thirty_days_count = total_cases_in_last_thirty_days_count
        self.total_free_case_document_count = total_free_case_document_count
        self.total_free_case_documents_in_last_thirty_days_count = total_free_case_documents_in_last_thirty_days_count
        self.total_paid_case_document_count = total_paid_case_document_count
        self.total_paid_case_documents_in_last_thirty_days_count = total_paid_case_documents_in_last_thirty_days_count
        self.total_case_document_in_library_count = total_case_document_in_library_count
        self.total_case_document_in_library_in_last_thirty_days_count = total_case_document_in_library_in_last_thirty_days_count
        self.case_class_coverage_array = case_class_coverage_array
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
    def __init__(self, last_update_count_date, court, total_case_count, total_cases_in_last_thirty_days_count, total_free_case_document_count, total_free_case_documents_in_last_thirty_days_count, total_paid_case_document_count, total_paid_case_documents_in_last_thirty_days_count, total_case_document_in_library_count, total_case_document_in_library_in_last_thirty_days_count, case_class_coverage_array, *args, **kwargs):  # noqa: E501
        """CourtCoverage - a model defined in OpenAPI

        Args:
            last_update_count_date (str): Date when it was last updated.
            court (Court):
            total_case_count (int): Total Cases for a specific court.
            total_cases_in_last_thirty_days_count (int): Total Cases in last 30 days that were added to UniCourt
            total_free_case_document_count (int): Total Free Case Documents for a specific court.
            total_free_case_documents_in_last_thirty_days_count (int): Total Free Case Documents in last 30 days that were added to UniCourt
            total_paid_case_document_count (int): Total Paid Case Documents for a specific court.
            total_paid_case_documents_in_last_thirty_days_count (int): Total Paid Case Documents in last 30 days that were added to UniCourt
            total_case_document_in_library_count (int): Count of total Case Documents added in UniCourt Library.
            total_case_document_in_library_in_last_thirty_days_count (int): Count of total Case Documents added in UniCourt Library in last 30 days
            case_class_coverage_array ([CaseClassCoverage]):

        Keyword Args:
            object (str): Name of the object. defaults to "CourtCoverage"  # noqa: E501
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
        """

        object = kwargs.get('object', "CourtCoverage")
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

        self.object = object
        self.last_update_count_date = last_update_count_date
        self.court = court
        self.total_case_count = total_case_count
        self.total_cases_in_last_thirty_days_count = total_cases_in_last_thirty_days_count
        self.total_free_case_document_count = total_free_case_document_count
        self.total_free_case_documents_in_last_thirty_days_count = total_free_case_documents_in_last_thirty_days_count
        self.total_paid_case_document_count = total_paid_case_document_count
        self.total_paid_case_documents_in_last_thirty_days_count = total_paid_case_documents_in_last_thirty_days_count
        self.total_case_document_in_library_count = total_case_document_in_library_count
        self.total_case_document_in_library_in_last_thirty_days_count = total_case_document_in_library_in_last_thirty_days_count
        self.case_class_coverage_array = case_class_coverage_array
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