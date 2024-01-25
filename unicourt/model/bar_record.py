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
    from unicourt.model.bar_source_data import BarSourceData
    from unicourt.model.contact import Contact
    globals()['BarSourceData'] = BarSourceData
    globals()['Contact'] = Contact


class BarRecord(ModelNormal):
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
        ('status',): {
            'ACTIVE': "Active",
            'INACTIVE': "Inactive",
            'NOT_CLASSIFIED': "Not Classified",
            'UNKNOWN': "Unknown",
        },
    }

    validations = {
        ('object',): {
            'max_length': 9,
        },
        ('bar_number',): {
            'max_length': 250,
        },
        ('bar_source_type',): {
            'max_length': 70,
        },
        ('admitted_date',): {
            'max_length': 25,
        },
        ('state_code',): {
            'max_length': 2,
        },
        ('status',): {
            'max_length': 15,
        },
        ('inactivation_date',): {
            'max_length': 25,
        },
        ('first_fetch_date',): {
            'max_length': 25,
        },
        ('last_fetch_date',): {
            'max_length': 25,
        },
        ('last_fetch_date_with_updates',): {
            'max_length': 25,
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
            'object': (str,),  # noqa: E501
            'bar_number': (str, none_type,),  # noqa: E501
            'bar_source_type': (str,),  # noqa: E501
            'admitted_date': (datetime, none_type,),  # noqa: E501
            'state_code': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'inactivation_date': (datetime, none_type,),  # noqa: E501
            'bar_source_data': (BarSourceData,),  # noqa: E501
            'contact': (Contact,),  # noqa: E501
            'first_fetch_date': (datetime,),  # noqa: E501
            'last_fetch_date': (datetime,),  # noqa: E501
            'last_fetch_date_with_updates': (datetime,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'object': 'object',  # noqa: E501
        'bar_number': 'barNumber',  # noqa: E501
        'bar_source_type': 'barSourceType',  # noqa: E501
        'admitted_date': 'admittedDate',  # noqa: E501
        'state_code': 'stateCode',  # noqa: E501
        'status': 'status',  # noqa: E501
        'inactivation_date': 'inactivationDate',  # noqa: E501
        'bar_source_data': 'barSourceData',  # noqa: E501
        'contact': 'contact',  # noqa: E501
        'first_fetch_date': 'firstFetchDate',  # noqa: E501
        'last_fetch_date': 'lastFetchDate',  # noqa: E501
        'last_fetch_date_with_updates': 'lastFetchDateWithUpdates',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, bar_number, bar_source_type, admitted_date, state_code, status, inactivation_date, bar_source_data, contact, first_fetch_date, last_fetch_date, last_fetch_date_with_updates, *args, **kwargs):  # noqa: E501
        """BarRecord - a model defined in OpenAPI

        Args:
            bar_number (str, none_type):
            bar_source_type (str):
            admitted_date (datetime, none_type): The admittedDate is the date when an attorney was admitted to the bar of a given state.
            state_code (str):
            status (str):
            inactivation_date (datetime, none_type):
            bar_source_data (BarSourceData):
            contact (Contact):
            first_fetch_date (datetime):
            last_fetch_date (datetime):
            last_fetch_date_with_updates (datetime): Last Fetch Date of the Attorney Update.

        Keyword Args:
            object (str): defaults to "BarRecord"  # noqa: E501
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

        object = kwargs.get('object', "BarRecord")
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
        self.bar_number = bar_number
        self.bar_source_type = bar_source_type
        self.admitted_date = admitted_date
        self.state_code = state_code
        self.status = status
        self.inactivation_date = inactivation_date
        self.bar_source_data = bar_source_data
        self.contact = contact
        self.first_fetch_date = first_fetch_date
        self.last_fetch_date = last_fetch_date
        self.last_fetch_date_with_updates = last_fetch_date_with_updates
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
    def __init__(self, bar_number, bar_source_type, admitted_date, state_code, status, inactivation_date, bar_source_data, contact, first_fetch_date, last_fetch_date, last_fetch_date_with_updates, *args, **kwargs):  # noqa: E501
        """BarRecord - a model defined in OpenAPI

        Args:
            bar_number (str, none_type):
            bar_source_type (str):
            admitted_date (datetime, none_type): The admittedDate is the date when an attorney was admitted to the bar of a given state.
            state_code (str):
            status (str):
            inactivation_date (datetime, none_type):
            bar_source_data (BarSourceData):
            contact (Contact):
            first_fetch_date (datetime):
            last_fetch_date (datetime):
            last_fetch_date_with_updates (datetime): Last Fetch Date of the Attorney Update.

        Keyword Args:
            object (str): defaults to "BarRecord"  # noqa: E501
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

        object = kwargs.get('object', "BarRecord")
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
        self.bar_number = bar_number
        self.bar_source_type = bar_source_type
        self.admitted_date = admitted_date
        self.state_code = state_code
        self.status = status
        self.inactivation_date = inactivation_date
        self.bar_source_data = bar_source_data
        self.contact = contact
        self.first_fetch_date = first_fetch_date
        self.last_fetch_date = last_fetch_date
        self.last_fetch_date_with_updates = last_fetch_date_with_updates
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