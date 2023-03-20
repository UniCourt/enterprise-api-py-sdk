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



class CaseCountAnalyticsByCaseFiledDate(ModelNormal):
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
        ('grouped_by',): {
            'YEARLY': "Yearly",
            'QUARTERLY': "Quarterly",
            'MONTHLY': "Monthly",
            'WEEKLY': "Weekly",
        },
        ('quarter',): {
            'None': None,
            'Q1': "Q1",
            'Q2': "Q2",
            'Q3': "Q3",
            'Q4': "Q4",
            'NULL': "null",
        },
        ('month_string',): {
            'None': None,
            'JANUARY': "January",
            'FEBRUARY': "February",
            'MARCH': "March",
            'APRIL': "April",
            'MAY': "May",
            'JUNE': "June",
            'JULY': "July",
            'AUGUST': "August",
            'SEPTEMBER': "September",
            'OCTOBER': "October",
            'NOVEMBER': "November",
            'DECEMBER': "December",
            'NULL': "null",
        },
    }

    validations = {
        ('object',): {
            'max_length': 33,
        },
        ('case_search_api',): {
            'max_length': 255,
        },
        ('grouped_by',): {
            'max_length': 9,
        },
        ('quarter',): {
            'max_length': 4,
        },
        ('month_string',): {
            'max_length': 9,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
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
        return {
            'object': (str,),  # noqa: E501
            'case_count': (int,),  # noqa: E501
            'case_search_api': (str,),  # noqa: E501
            'grouped_by': (str,),  # noqa: E501
            'year': (int,),  # noqa: E501
            'quarter': (str, none_type,),  # noqa: E501
            'month_string': (str, none_type,),  # noqa: E501
            'month_int': (int, none_type,),  # noqa: E501
            'week_of_year': (int, none_type,),  # noqa: E501
            'week_of_month': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'object': 'object',  # noqa: E501
        'case_count': 'caseCount',  # noqa: E501
        'case_search_api': 'caseSearchAPI',  # noqa: E501
        'grouped_by': 'groupedBy',  # noqa: E501
        'year': 'year',  # noqa: E501
        'quarter': 'quarter',  # noqa: E501
        'month_string': 'monthString',  # noqa: E501
        'month_int': 'monthInt',  # noqa: E501
        'week_of_year': 'weekOfYear',  # noqa: E501
        'week_of_month': 'weekOfMonth',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, case_count, case_search_api, year, quarter, month_string, month_int, week_of_year, week_of_month, *args, **kwargs):  # noqa: E501
        """CaseCountAnalyticsByCaseFiledDate - a model defined in OpenAPI

        Args:
            case_count (int):
            case_search_api (str): Link to cases for this criteria.
            year (int):
            quarter (str, none_type):
            month_string (str, none_type):
            month_int (int, none_type):
            week_of_year (int, none_type):
            week_of_month (int, none_type):

        Keyword Args:
            object (str): defaults to "CaseCountAnalyticsByCaseFiledDate"  # noqa: E501
            grouped_by (str): defaults to "Yearly", must be one of ["Yearly", "Quarterly", "Monthly", "Weekly", ]  # noqa: E501
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

        object = kwargs.get('object', "CaseCountAnalyticsByCaseFiledDate")
        grouped_by = kwargs.get('grouped_by', "Yearly")
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
        self.case_count = case_count
        self.case_search_api = case_search_api
        self.grouped_by = grouped_by
        self.year = year
        self.quarter = quarter
        self.month_string = month_string
        self.month_int = month_int
        self.week_of_year = week_of_year
        self.week_of_month = week_of_month
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
    def __init__(self, case_count, case_search_api, year, quarter, month_string, month_int, week_of_year, week_of_month, *args, **kwargs):  # noqa: E501
        """CaseCountAnalyticsByCaseFiledDate - a model defined in OpenAPI

        Args:
            case_count (int):
            case_search_api (str): Link to cases for this criteria.
            year (int):
            quarter (str, none_type):
            month_string (str, none_type):
            month_int (int, none_type):
            week_of_year (int, none_type):
            week_of_month (int, none_type):

        Keyword Args:
            object (str): defaults to "CaseCountAnalyticsByCaseFiledDate"  # noqa: E501
            grouped_by (str): defaults to "Yearly", must be one of ["Yearly", "Quarterly", "Monthly", "Weekly", ]  # noqa: E501
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

        object = kwargs.get('object', "CaseCountAnalyticsByCaseFiledDate")
        grouped_by = kwargs.get('grouped_by', "Yearly")
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
        self.case_count = case_count
        self.case_search_api = case_search_api
        self.grouped_by = grouped_by
        self.year = year
        self.quarter = quarter
        self.month_string = month_string
        self.month_int = month_int
        self.week_of_year = week_of_year
        self.week_of_month = week_of_month
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
