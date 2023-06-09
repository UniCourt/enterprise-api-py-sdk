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
    from unicourt.model.source_charge_additional_data import SourceChargeAdditionalData
    globals()['SourceChargeAdditionalData'] = SourceChargeAdditionalData


class SourceCharge(ModelNormal):
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
            'max_length': 12,
            'min_length': 12,
        },
        ('source_charge_raw',): {
            'max_length': 255,
        },
        ('source_charge',): {
            'max_length': 255,
        },
        ('source_statute',): {
            'max_length': 50,
        },
        ('source_charge_degree',): {
            'max_length': 255,
        },
        ('source_charge_severity',): {
            'max_length': 255,
        },
        ('first_fetch_date',): {
            'max_length': 25,
            'min_length': 25,
        },
        ('last_fetch_date',): {
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
            'source_charge_raw': (str,),  # noqa: E501
            'source_charge': (str, none_type,),  # noqa: E501
            'is_visible': (bool,),  # noqa: E501
            'source_statute': (str, none_type,),  # noqa: E501
            'source_charge_degree': (str, none_type,),  # noqa: E501
            'source_charge_severity': (str, none_type,),  # noqa: E501
            'source_charge_additional_data_array': ([SourceChargeAdditionalData],),  # noqa: E501
            'first_fetch_date': (str,),  # noqa: E501
            'last_fetch_date': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'object': 'object',  # noqa: E501
        'source_charge_raw': 'sourceChargeRaw',  # noqa: E501
        'source_charge': 'sourceCharge',  # noqa: E501
        'is_visible': 'isVisible',  # noqa: E501
        'source_statute': 'sourceStatute',  # noqa: E501
        'source_charge_degree': 'sourceChargeDegree',  # noqa: E501
        'source_charge_severity': 'sourceChargeSeverity',  # noqa: E501
        'source_charge_additional_data_array': 'sourceChargeAdditionalDataArray',  # noqa: E501
        'first_fetch_date': 'firstFetchDate',  # noqa: E501
        'last_fetch_date': 'lastFetchDate',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, source_charge_raw, source_charge, is_visible, source_statute, source_charge_degree, source_charge_severity, source_charge_additional_data_array, first_fetch_date, last_fetch_date, *args, **kwargs):  # noqa: E501
        """SourceCharge - a model defined in OpenAPI

        Args:
            source_charge_raw (str): Raw charge data from the source site.
            source_charge (str, none_type): Charge data from the source site.
            is_visible (bool): Signifies if the charge is currently isVisible or not for the case.
            source_statute (str, none_type): Statute of a charge.
            source_charge_degree (str, none_type): Charge degree data from the source site.
            source_charge_severity (str, none_type): Charge severity data from the source site.
            source_charge_additional_data_array ([SourceChargeAdditionalData]): Additional data related to the charge which is available in the source site.
            first_fetch_date (str): When this charge was first fetched from the court site.
            last_fetch_date (str): When this charge was last fetched from the court site.

        Keyword Args:
            object (str): Name of the object. defaults to "SourceCharge"  # noqa: E501
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

        object = kwargs.get('object', "SourceCharge")
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
        self.source_charge_raw = source_charge_raw
        self.source_charge = source_charge
        self.is_visible = is_visible
        self.source_statute = source_statute
        self.source_charge_degree = source_charge_degree
        self.source_charge_severity = source_charge_severity
        self.source_charge_additional_data_array = source_charge_additional_data_array
        self.first_fetch_date = first_fetch_date
        self.last_fetch_date = last_fetch_date
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
    def __init__(self, source_charge_raw, source_charge, is_visible, source_statute, source_charge_degree, source_charge_severity, source_charge_additional_data_array, first_fetch_date, last_fetch_date, *args, **kwargs):  # noqa: E501
        """SourceCharge - a model defined in OpenAPI

        Args:
            source_charge_raw (str): Raw charge data from the source site.
            source_charge (str, none_type): Charge data from the source site.
            is_visible (bool): Signifies if the charge is currently isVisible or not for the case.
            source_statute (str, none_type): Statute of a charge.
            source_charge_degree (str, none_type): Charge degree data from the source site.
            source_charge_severity (str, none_type): Charge severity data from the source site.
            source_charge_additional_data_array ([SourceChargeAdditionalData]): Additional data related to the charge which is available in the source site.
            first_fetch_date (str): When this charge was first fetched from the court site.
            last_fetch_date (str): When this charge was last fetched from the court site.

        Keyword Args:
            object (str): Name of the object. defaults to "SourceCharge"  # noqa: E501
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

        object = kwargs.get('object', "SourceCharge")
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
        self.source_charge_raw = source_charge_raw
        self.source_charge = source_charge
        self.is_visible = is_visible
        self.source_statute = source_statute
        self.source_charge_degree = source_charge_degree
        self.source_charge_severity = source_charge_severity
        self.source_charge_additional_data_array = source_charge_additional_data_array
        self.first_fetch_date = first_fetch_date
        self.last_fetch_date = last_fetch_date
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
