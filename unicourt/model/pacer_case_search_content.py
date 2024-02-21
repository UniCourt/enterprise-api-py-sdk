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



class PACERCaseSearchContent(ModelNormal):
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
        ('pcl_jurisdiction_type',): {
            'None': None,
            'APPELLATE': "Appellate",
            'BANKRUPTCY': "Bankruptcy",
            'CRIMINAL': "Criminal",
            'CIVIL': "Civil",
            'MULTI-DISTRICT_LITIGATION': "Multi-district Litigation",
            'NULL': "null",
        },
    }

    validations = {
        ('object',): {
            'max_length': 22,
            'min_length': 22,
        },
        ('pcl_case_link',): {
            'max_length': 255,
        },
        ('pcl_case_number_full',): {
            'max_length': 50,
        },
        ('pcl_case_title',): {
            'max_length': 255,
        },
        ('pcl_case_office',): {
            'max_length': 2,
        },
        ('pcl_case_type',): {
            'max_length': 6,
        },
        ('pcl_court_id',): {
            'max_length': 6,
        },
        ('pcl_date_filed',): {
            'max_length': 10,
        },
        ('pcl_mdl_court_id',): {
            'max_length': 10,
        },
        ('pcl_mdl_date_ordered',): {
            'max_length': 10,
        },
        ('pcl_mdl_date_received',): {
            'max_length': 10,
        },
        ('pcl_mdl_extension',): {
            'max_length': 50,
        },
        ('pcl_mdl_judge_last_name',): {
            'max_length': 50,
        },
        ('pcl_mdl_littype',): {
            'max_length': 50,
        },
        ('pcl_mdl_status',): {
            'max_length': 50,
        },
        ('pcl_mdl_transferee',): {
            'max_length': 50,
        },
        ('pcl_mdl_transferee_district',): {
            'max_length': 50,
        },
        ('pcl_civil_cto_number',): {
            'max_length': 50,
        },
        ('pcl_civil_date_disposition',): {
            'max_length': 10,
        },
        ('pcl_civil_date_initiated',): {
            'max_length': 10,
        },
        ('pcl_civil_date_terminated',): {
            'max_length': 10,
        },
        ('pcl_civil_stat_disposition',): {
            'max_length': 50,
        },
        ('pcl_civil_stat_initiated',): {
            'max_length': 50,
        },
        ('pcl_civil_stat_terminated',): {
            'max_length': 50,
        },
        ('pcl_civil_transferee',): {
            'max_length': 50,
        },
        ('pcl_bankruptcy_chapter',): {
            'max_length': 50,
        },
        ('pcl_date_discharged',): {
            'max_length': 10,
        },
        ('pcl_date_dismissed',): {
            'max_length': 10,
        },
        ('pcl_date_reopened',): {
            'max_length': 10,
        },
        ('pcl_date_termed',): {
            'max_length': 10,
        },
        ('pcl_disposition',): {
            'max_length': 100,
        },
        ('pcl_disposition_method',): {
            'max_length': 100,
        },
        ('pcl_joint_bankruptcy_flag',): {
            'max_length': 50,
        },
        ('pcl_joint_discharged_date',): {
            'max_length': 10,
        },
        ('pcl_joint_dismissed_date',): {
            'max_length': 10,
        },
        ('pcl_joint_disposition_method',): {
            'max_length': 100,
        },
        ('pcl_nature_of_suit',): {
            'max_length': 50,
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
            'pcl_case_link': (str, none_type,),  # noqa: E501
            'pcl_jurisdiction_type': (str, none_type,),  # noqa: E501
            'pcl_case_id': (int,),  # noqa: E501
            'pcl_case_number_full': (str, none_type,),  # noqa: E501
            'pcl_case_title': (str, none_type,),  # noqa: E501
            'pcl_case_office': (str, none_type,),  # noqa: E501
            'pcl_case_number': (int,),  # noqa: E501
            'pcl_case_type': (str, none_type,),  # noqa: E501
            'pcl_case_year': (int,),  # noqa: E501
            'pcl_court_id': (str, none_type,),  # noqa: E501
            'pcl_date_filed': (str, none_type,),  # noqa: E501
            'pcl_jpml_number': (int, none_type,),  # noqa: E501
            'pcl_mdl_court_id': (str, none_type,),  # noqa: E501
            'pcl_mdl_date_ordered': (str, none_type,),  # noqa: E501
            'pcl_mdl_date_received': (str, none_type,),  # noqa: E501
            'pcl_mdl_extension': (str, none_type,),  # noqa: E501
            'pcl_mdl_judge_last_name': (str, none_type,),  # noqa: E501
            'pcl_mdl_littype': (str, none_type,),  # noqa: E501
            'pcl_mdl_status': (str, none_type,),  # noqa: E501
            'pcl_mdl_transferee': (str, none_type,),  # noqa: E501
            'pcl_mdl_transferee_district': (str, none_type,),  # noqa: E501
            'pcl_civil_cto_number': (str, none_type,),  # noqa: E501
            'pcl_civil_date_disposition': (str, none_type,),  # noqa: E501
            'pcl_civil_date_initiated': (str, none_type,),  # noqa: E501
            'pcl_civil_date_terminated': (str, none_type,),  # noqa: E501
            'pcl_civil_stat_disposition': (str, none_type,),  # noqa: E501
            'pcl_civil_stat_initiated': (str, none_type,),  # noqa: E501
            'pcl_civil_stat_terminated': (str, none_type,),  # noqa: E501
            'pcl_civil_transferee': (str, none_type,),  # noqa: E501
            'pcl_bankruptcy_chapter': (str, none_type,),  # noqa: E501
            'pcl_date_discharged': (str, none_type,),  # noqa: E501
            'pcl_date_dismissed': (str, none_type,),  # noqa: E501
            'pcl_date_reopened': (str, none_type,),  # noqa: E501
            'pcl_date_termed': (str, none_type,),  # noqa: E501
            'pcl_disposition': (str, none_type,),  # noqa: E501
            'pcl_disposition_method': (str, none_type,),  # noqa: E501
            'pcl_joint_bankruptcy_flag': (str, none_type,),  # noqa: E501
            'pcl_joint_discharged_date': (str, none_type,),  # noqa: E501
            'pcl_joint_dismissed_date': (str, none_type,),  # noqa: E501
            'pcl_joint_disposition_method': (str, none_type,),  # noqa: E501
            'pcl_nature_of_suit': (str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'object': 'object',  # noqa: E501
        'pcl_case_link': 'pclCaseLink',  # noqa: E501
        'pcl_jurisdiction_type': 'pclJurisdictionType',  # noqa: E501
        'pcl_case_id': 'pclCaseId',  # noqa: E501
        'pcl_case_number_full': 'pclCaseNumberFull',  # noqa: E501
        'pcl_case_title': 'pclCaseTitle',  # noqa: E501
        'pcl_case_office': 'pclCaseOffice',  # noqa: E501
        'pcl_case_number': 'pclCaseNumber',  # noqa: E501
        'pcl_case_type': 'pclCaseType',  # noqa: E501
        'pcl_case_year': 'pclCaseYear',  # noqa: E501
        'pcl_court_id': 'pclCourtId',  # noqa: E501
        'pcl_date_filed': 'pclDateFiled',  # noqa: E501
        'pcl_jpml_number': 'pclJpmlNumber',  # noqa: E501
        'pcl_mdl_court_id': 'pclMdlCourtId',  # noqa: E501
        'pcl_mdl_date_ordered': 'pclMdlDateOrdered',  # noqa: E501
        'pcl_mdl_date_received': 'pclMdlDateReceived',  # noqa: E501
        'pcl_mdl_extension': 'pclMdlExtension',  # noqa: E501
        'pcl_mdl_judge_last_name': 'pclMdlJudgeLastName',  # noqa: E501
        'pcl_mdl_littype': 'pclMdlLittype',  # noqa: E501
        'pcl_mdl_status': 'pclMdlStatus',  # noqa: E501
        'pcl_mdl_transferee': 'pclMdlTransferee',  # noqa: E501
        'pcl_mdl_transferee_district': 'pclMdlTransfereeDistrict',  # noqa: E501
        'pcl_civil_cto_number': 'pclCivilCtoNumber',  # noqa: E501
        'pcl_civil_date_disposition': 'pclCivilDateDisposition',  # noqa: E501
        'pcl_civil_date_initiated': 'pclCivilDateInitiated',  # noqa: E501
        'pcl_civil_date_terminated': 'pclCivilDateTerminated',  # noqa: E501
        'pcl_civil_stat_disposition': 'pclCivilStatDisposition',  # noqa: E501
        'pcl_civil_stat_initiated': 'pclCivilStatInitiated',  # noqa: E501
        'pcl_civil_stat_terminated': 'pclCivilStatTerminated',  # noqa: E501
        'pcl_civil_transferee': 'pclCivilTransferee',  # noqa: E501
        'pcl_bankruptcy_chapter': 'pclBankruptcyChapter',  # noqa: E501
        'pcl_date_discharged': 'pclDateDischarged',  # noqa: E501
        'pcl_date_dismissed': 'pclDateDismissed',  # noqa: E501
        'pcl_date_reopened': 'pclDateReopened',  # noqa: E501
        'pcl_date_termed': 'pclDateTermed',  # noqa: E501
        'pcl_disposition': 'pclDisposition',  # noqa: E501
        'pcl_disposition_method': 'pclDispositionMethod',  # noqa: E501
        'pcl_joint_bankruptcy_flag': 'pclJointBankruptcyFlag',  # noqa: E501
        'pcl_joint_discharged_date': 'pclJointDischargedDate',  # noqa: E501
        'pcl_joint_dismissed_date': 'pclJointDismissedDate',  # noqa: E501
        'pcl_joint_disposition_method': 'pclJointDispositionMethod',  # noqa: E501
        'pcl_nature_of_suit': 'pclNatureOfSuit',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, pcl_case_link, pcl_jurisdiction_type, pcl_case_id, pcl_case_number_full, pcl_case_title, pcl_case_office, pcl_case_number, pcl_case_type, pcl_case_year, pcl_court_id, pcl_date_filed, pcl_jpml_number, pcl_mdl_court_id, pcl_mdl_date_ordered, pcl_mdl_date_received, pcl_mdl_extension, pcl_mdl_judge_last_name, pcl_mdl_littype, pcl_mdl_status, pcl_mdl_transferee, pcl_mdl_transferee_district, pcl_civil_cto_number, pcl_civil_date_disposition, pcl_civil_date_initiated, pcl_civil_date_terminated, pcl_civil_stat_disposition, pcl_civil_stat_initiated, pcl_civil_stat_terminated, pcl_civil_transferee, pcl_bankruptcy_chapter, pcl_date_discharged, pcl_date_dismissed, pcl_date_reopened, pcl_date_termed, pcl_disposition, pcl_disposition_method, pcl_joint_bankruptcy_flag, pcl_joint_discharged_date, pcl_joint_dismissed_date, pcl_joint_disposition_method, pcl_nature_of_suit, *args, **kwargs):  # noqa: E501
        """PACERCaseSearchContent - a model defined in OpenAPI

        Args:
            pcl_case_link (str, none_type): Link to case in the case management/electronic case files (CM/ECF) system at the court.
            pcl_jurisdiction_type (str, none_type): Link to case in the case management/electronic case files (CM/ECF) system at the court.
            pcl_case_id (int): Sequentially generated number that identifies the case.
            pcl_case_number_full (str, none_type): Case Number.
            pcl_case_title (str, none_type): Title of the case.
            pcl_case_office (str, none_type): The divisional office in which the case was filed.
            pcl_case_number (int): The sequence number of the case.
            pcl_case_type (str, none_type): Code that identifies the type of case.
            pcl_case_year (int): The year in which the case falls. Could be two or four digit.
            pcl_court_id (str, none_type): The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B
            pcl_date_filed (str, none_type): Filing date of the case.
            pcl_jpml_number (int, none_type): JPML Case Seed number.
            pcl_mdl_court_id (str, none_type): Which court does this mdl belongs too.
            pcl_mdl_date_ordered (str, none_type): This parameter represents the mdl date ordered of the case when it is present
            pcl_mdl_date_received (str, none_type): This parameter represents the mdl date received of the case when it is present
            pcl_mdl_extension (str, none_type): This parameter represents the mdl extension of the case when it is present
            pcl_mdl_judge_last_name (str, none_type): This parameter represents the mdl judge lastname of the case when it is present
            pcl_mdl_littype (str, none_type): This parameter represents the mdl lit type of the case when it is present
            pcl_mdl_status (str, none_type): This parameter represents the mdl status of the case when it is present
            pcl_mdl_transferee (str, none_type): This parameter represents the mdl transferee of the case when it is present
            pcl_mdl_transferee_district (str, none_type): This parameter represents the mdl transferee district of the case when it is present
            pcl_civil_cto_number (str, none_type): This parameter represents the civil cto number of the case when it is present
            pcl_civil_date_disposition (str, none_type): This parameter represents the civil disposition date of the case when it is present
            pcl_civil_date_initiated (str, none_type): This parameter represents the civil initiated date of the case when it is present
            pcl_civil_date_terminated (str, none_type): This parameter represents the civil terminated date of the case when it is present
            pcl_civil_stat_disposition (str, none_type): This parameter represents the civil stat disposition of the case when it is present
            pcl_civil_stat_initiated (str, none_type): This parameter represents the civil stat initiated of the case when it is present
            pcl_civil_stat_terminated (str, none_type): This parameter represents the civil stat terminated of the case when it is present
            pcl_civil_transferee (str, none_type): This parameter represents the civil transferee of the case when it is present
            pcl_bankruptcy_chapter (str, none_type): This parameter represents the bankruptcy chapter of the case when it is present
            pcl_date_discharged (str, none_type): This parameter represents the date discharged of the case when it is present
            pcl_date_dismissed (str, none_type): This parameter represents the date dismissed of the case when it is present
            pcl_date_reopened (str, none_type): This parameter represents the date reopened of the case when it is present
            pcl_date_termed (str, none_type): This parameter represents the date termed of the case when it is present
            pcl_disposition (str, none_type): This parameter represents the disposition of the case when it is present
            pcl_disposition_method (str, none_type): This parameter represents the disposition method of the case when it is present
            pcl_joint_bankruptcy_flag (str, none_type): This parameter represents the joint bankruptcy flag of the case when it is present
            pcl_joint_discharged_date (str, none_type): This parameter represents the joint discharged date of the case when it is present
            pcl_joint_dismissed_date (str, none_type): This parameter represents the joint dismissed date of the case when it is present
            pcl_joint_disposition_method (str, none_type): This parameter represents the joint disposition method of the case when it is present
            pcl_nature_of_suit (str, none_type): This parameter represents the nature of suit of the case when it is present

        Keyword Args:
            object (str): Name of the object. defaults to "PACERCaseSearchContent"  # noqa: E501
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

        object = kwargs.get('object', "PACERCaseSearchContent")
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
        self.pcl_case_link = pcl_case_link
        self.pcl_jurisdiction_type = pcl_jurisdiction_type
        self.pcl_case_id = pcl_case_id
        self.pcl_case_number_full = pcl_case_number_full
        self.pcl_case_title = pcl_case_title
        self.pcl_case_office = pcl_case_office
        self.pcl_case_number = pcl_case_number
        self.pcl_case_type = pcl_case_type
        self.pcl_case_year = pcl_case_year
        self.pcl_court_id = pcl_court_id
        self.pcl_date_filed = pcl_date_filed
        self.pcl_jpml_number = pcl_jpml_number
        self.pcl_mdl_court_id = pcl_mdl_court_id
        self.pcl_mdl_date_ordered = pcl_mdl_date_ordered
        self.pcl_mdl_date_received = pcl_mdl_date_received
        self.pcl_mdl_extension = pcl_mdl_extension
        self.pcl_mdl_judge_last_name = pcl_mdl_judge_last_name
        self.pcl_mdl_littype = pcl_mdl_littype
        self.pcl_mdl_status = pcl_mdl_status
        self.pcl_mdl_transferee = pcl_mdl_transferee
        self.pcl_mdl_transferee_district = pcl_mdl_transferee_district
        self.pcl_civil_cto_number = pcl_civil_cto_number
        self.pcl_civil_date_disposition = pcl_civil_date_disposition
        self.pcl_civil_date_initiated = pcl_civil_date_initiated
        self.pcl_civil_date_terminated = pcl_civil_date_terminated
        self.pcl_civil_stat_disposition = pcl_civil_stat_disposition
        self.pcl_civil_stat_initiated = pcl_civil_stat_initiated
        self.pcl_civil_stat_terminated = pcl_civil_stat_terminated
        self.pcl_civil_transferee = pcl_civil_transferee
        self.pcl_bankruptcy_chapter = pcl_bankruptcy_chapter
        self.pcl_date_discharged = pcl_date_discharged
        self.pcl_date_dismissed = pcl_date_dismissed
        self.pcl_date_reopened = pcl_date_reopened
        self.pcl_date_termed = pcl_date_termed
        self.pcl_disposition = pcl_disposition
        self.pcl_disposition_method = pcl_disposition_method
        self.pcl_joint_bankruptcy_flag = pcl_joint_bankruptcy_flag
        self.pcl_joint_discharged_date = pcl_joint_discharged_date
        self.pcl_joint_dismissed_date = pcl_joint_dismissed_date
        self.pcl_joint_disposition_method = pcl_joint_disposition_method
        self.pcl_nature_of_suit = pcl_nature_of_suit
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
    def __init__(self, pcl_case_link, pcl_jurisdiction_type, pcl_case_id, pcl_case_number_full, pcl_case_title, pcl_case_office, pcl_case_number, pcl_case_type, pcl_case_year, pcl_court_id, pcl_date_filed, pcl_jpml_number, pcl_mdl_court_id, pcl_mdl_date_ordered, pcl_mdl_date_received, pcl_mdl_extension, pcl_mdl_judge_last_name, pcl_mdl_littype, pcl_mdl_status, pcl_mdl_transferee, pcl_mdl_transferee_district, pcl_civil_cto_number, pcl_civil_date_disposition, pcl_civil_date_initiated, pcl_civil_date_terminated, pcl_civil_stat_disposition, pcl_civil_stat_initiated, pcl_civil_stat_terminated, pcl_civil_transferee, pcl_bankruptcy_chapter, pcl_date_discharged, pcl_date_dismissed, pcl_date_reopened, pcl_date_termed, pcl_disposition, pcl_disposition_method, pcl_joint_bankruptcy_flag, pcl_joint_discharged_date, pcl_joint_dismissed_date, pcl_joint_disposition_method, pcl_nature_of_suit, *args, **kwargs):  # noqa: E501
        """PACERCaseSearchContent - a model defined in OpenAPI

        Args:
            pcl_case_link (str, none_type): Link to case in the case management/electronic case files (CM/ECF) system at the court.
            pcl_jurisdiction_type (str, none_type): Link to case in the case management/electronic case files (CM/ECF) system at the court.
            pcl_case_id (int): Sequentially generated number that identifies the case.
            pcl_case_number_full (str, none_type): Case Number.
            pcl_case_title (str, none_type): Title of the case.
            pcl_case_office (str, none_type): The divisional office in which the case was filed.
            pcl_case_number (int): The sequence number of the case.
            pcl_case_type (str, none_type): Code that identifies the type of case.
            pcl_case_year (int): The year in which the case falls. Could be two or four digit.
            pcl_court_id (str, none_type): The general geographical region or specific court district. The court ID is the abbreviation of the court location combined with the court type (dc or bk). Please refer the Appendix B
            pcl_date_filed (str, none_type): Filing date of the case.
            pcl_jpml_number (int, none_type): JPML Case Seed number.
            pcl_mdl_court_id (str, none_type): Which court does this mdl belongs too.
            pcl_mdl_date_ordered (str, none_type): This parameter represents the mdl date ordered of the case when it is present
            pcl_mdl_date_received (str, none_type): This parameter represents the mdl date received of the case when it is present
            pcl_mdl_extension (str, none_type): This parameter represents the mdl extension of the case when it is present
            pcl_mdl_judge_last_name (str, none_type): This parameter represents the mdl judge lastname of the case when it is present
            pcl_mdl_littype (str, none_type): This parameter represents the mdl lit type of the case when it is present
            pcl_mdl_status (str, none_type): This parameter represents the mdl status of the case when it is present
            pcl_mdl_transferee (str, none_type): This parameter represents the mdl transferee of the case when it is present
            pcl_mdl_transferee_district (str, none_type): This parameter represents the mdl transferee district of the case when it is present
            pcl_civil_cto_number (str, none_type): This parameter represents the civil cto number of the case when it is present
            pcl_civil_date_disposition (str, none_type): This parameter represents the civil disposition date of the case when it is present
            pcl_civil_date_initiated (str, none_type): This parameter represents the civil initiated date of the case when it is present
            pcl_civil_date_terminated (str, none_type): This parameter represents the civil terminated date of the case when it is present
            pcl_civil_stat_disposition (str, none_type): This parameter represents the civil stat disposition of the case when it is present
            pcl_civil_stat_initiated (str, none_type): This parameter represents the civil stat initiated of the case when it is present
            pcl_civil_stat_terminated (str, none_type): This parameter represents the civil stat terminated of the case when it is present
            pcl_civil_transferee (str, none_type): This parameter represents the civil transferee of the case when it is present
            pcl_bankruptcy_chapter (str, none_type): This parameter represents the bankruptcy chapter of the case when it is present
            pcl_date_discharged (str, none_type): This parameter represents the date discharged of the case when it is present
            pcl_date_dismissed (str, none_type): This parameter represents the date dismissed of the case when it is present
            pcl_date_reopened (str, none_type): This parameter represents the date reopened of the case when it is present
            pcl_date_termed (str, none_type): This parameter represents the date termed of the case when it is present
            pcl_disposition (str, none_type): This parameter represents the disposition of the case when it is present
            pcl_disposition_method (str, none_type): This parameter represents the disposition method of the case when it is present
            pcl_joint_bankruptcy_flag (str, none_type): This parameter represents the joint bankruptcy flag of the case when it is present
            pcl_joint_discharged_date (str, none_type): This parameter represents the joint discharged date of the case when it is present
            pcl_joint_dismissed_date (str, none_type): This parameter represents the joint dismissed date of the case when it is present
            pcl_joint_disposition_method (str, none_type): This parameter represents the joint disposition method of the case when it is present
            pcl_nature_of_suit (str, none_type): This parameter represents the nature of suit of the case when it is present

        Keyword Args:
            object (str): Name of the object. defaults to "PACERCaseSearchContent"  # noqa: E501
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

        object = kwargs.get('object', "PACERCaseSearchContent")
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
        self.pcl_case_link = pcl_case_link
        self.pcl_jurisdiction_type = pcl_jurisdiction_type
        self.pcl_case_id = pcl_case_id
        self.pcl_case_number_full = pcl_case_number_full
        self.pcl_case_title = pcl_case_title
        self.pcl_case_office = pcl_case_office
        self.pcl_case_number = pcl_case_number
        self.pcl_case_type = pcl_case_type
        self.pcl_case_year = pcl_case_year
        self.pcl_court_id = pcl_court_id
        self.pcl_date_filed = pcl_date_filed
        self.pcl_jpml_number = pcl_jpml_number
        self.pcl_mdl_court_id = pcl_mdl_court_id
        self.pcl_mdl_date_ordered = pcl_mdl_date_ordered
        self.pcl_mdl_date_received = pcl_mdl_date_received
        self.pcl_mdl_extension = pcl_mdl_extension
        self.pcl_mdl_judge_last_name = pcl_mdl_judge_last_name
        self.pcl_mdl_littype = pcl_mdl_littype
        self.pcl_mdl_status = pcl_mdl_status
        self.pcl_mdl_transferee = pcl_mdl_transferee
        self.pcl_mdl_transferee_district = pcl_mdl_transferee_district
        self.pcl_civil_cto_number = pcl_civil_cto_number
        self.pcl_civil_date_disposition = pcl_civil_date_disposition
        self.pcl_civil_date_initiated = pcl_civil_date_initiated
        self.pcl_civil_date_terminated = pcl_civil_date_terminated
        self.pcl_civil_stat_disposition = pcl_civil_stat_disposition
        self.pcl_civil_stat_initiated = pcl_civil_stat_initiated
        self.pcl_civil_stat_terminated = pcl_civil_stat_terminated
        self.pcl_civil_transferee = pcl_civil_transferee
        self.pcl_bankruptcy_chapter = pcl_bankruptcy_chapter
        self.pcl_date_discharged = pcl_date_discharged
        self.pcl_date_dismissed = pcl_date_dismissed
        self.pcl_date_reopened = pcl_date_reopened
        self.pcl_date_termed = pcl_date_termed
        self.pcl_disposition = pcl_disposition
        self.pcl_disposition_method = pcl_disposition_method
        self.pcl_joint_bankruptcy_flag = pcl_joint_bankruptcy_flag
        self.pcl_joint_discharged_date = pcl_joint_discharged_date
        self.pcl_joint_dismissed_date = pcl_joint_dismissed_date
        self.pcl_joint_disposition_method = pcl_joint_disposition_method
        self.pcl_nature_of_suit = pcl_nature_of_suit
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
