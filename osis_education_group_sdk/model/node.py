"""
    Education Group Service

    A set of API endpoints that allow you to get, update, delete an education group.  # noqa: E501

    The version of the OpenAPI document: 1.08
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from osis_education_group_sdk.model_utils import (  # noqa: F401
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
)

def lazy_import():
    from osis_education_group_sdk.model.constraint_type_enum import ConstraintTypeEnum
    from osis_education_group_sdk.model.node_link_type_enum import NodeLinkTypeEnum
    from osis_education_group_sdk.model.node_sub_type_enum import NodeSubTypeEnum
    from osis_education_group_sdk.model.node_type_enum import NodeTypeEnum
    from osis_education_group_sdk.model.periodicity_enum import PeriodicityEnum
    from osis_education_group_sdk.model.proposal_type_enum import ProposalTypeEnum
    from osis_education_group_sdk.model.quadrimester_enum import QuadrimesterEnum
    globals()['ConstraintTypeEnum'] = ConstraintTypeEnum
    globals()['NodeLinkTypeEnum'] = NodeLinkTypeEnum
    globals()['NodeSubTypeEnum'] = NodeSubTypeEnum
    globals()['NodeTypeEnum'] = NodeTypeEnum
    globals()['PeriodicityEnum'] = PeriodicityEnum
    globals()['ProposalTypeEnum'] = ProposalTypeEnum
    globals()['QuadrimesterEnum'] = QuadrimesterEnum


class Node(ModelNormal):
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
        ('min_constraint',): {
            'inclusive_minimum': 1,
        },
        ('max_constraint',): {
            'inclusive_minimum': 1,
        },
    }

    additional_properties_type = None

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
            'url': (str,),  # noqa: E501
            'code': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'node_type': (NodeTypeEnum,),  # noqa: E501
            'subtype': (NodeSubTypeEnum,),  # noqa: E501
            'is_mandatory': (bool,),  # noqa: E501
            'block': ([int],),  # noqa: E501
            'access_condition': (bool,),  # noqa: E501
            'comment': (str,),  # noqa: E501
            'remark': (str,),  # noqa: E501
            'remark_en': (str,),  # noqa: E501
            'link_type': (NodeLinkTypeEnum,),  # noqa: E501
            'link_type_text': (str,),  # noqa: E501
            'children': ([Node],),  # noqa: E501
            'acronym': (str,),  # noqa: E501
            'title_en': (str,),  # noqa: E501
            'partial_title': (str,),  # noqa: E501
            'partial_title_en': (str,),  # noqa: E501
            'credits': (float,),  # noqa: E501
            'lecturing_volume': (float,),  # noqa: E501
            'practical_exercise_volume': (float,),  # noqa: E501
            'proposal_type': (ProposalTypeEnum,),  # noqa: E501
            'status': (bool,),  # noqa: E501
            'quadrimester': (QuadrimesterEnum,),  # noqa: E501
            'periodicity': (PeriodicityEnum,),  # noqa: E501
            'comment_en': (str,),  # noqa: E501
            'with_prerequisite': (bool,),  # noqa: E501
            'min_constraint': (int,),  # noqa: E501
            'max_constraint': (int,),  # noqa: E501
            'constraint_type': (ConstraintTypeEnum,),  # noqa: E501
            'version_name': (str,),  # noqa: E501
            'language': (str,),  # noqa: E501
            'french_friendly': (bool,),  # noqa: E501
            'english_friendly': (bool,),  # noqa: E501
            'exchange_students': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'url': 'url',  # noqa: E501
        'code': 'code',  # noqa: E501
        'title': 'title',  # noqa: E501
        'node_type': 'node_type',  # noqa: E501
        'subtype': 'subtype',  # noqa: E501
        'is_mandatory': 'is_mandatory',  # noqa: E501
        'block': 'block',  # noqa: E501
        'access_condition': 'access_condition',  # noqa: E501
        'comment': 'comment',  # noqa: E501
        'remark': 'remark',  # noqa: E501
        'remark_en': 'remark_en',  # noqa: E501
        'link_type': 'link_type',  # noqa: E501
        'link_type_text': 'link_type_text',  # noqa: E501
        'children': 'children',  # noqa: E501
        'acronym': 'acronym',  # noqa: E501
        'title_en': 'title_en',  # noqa: E501
        'partial_title': 'partial_title',  # noqa: E501
        'partial_title_en': 'partial_title_en',  # noqa: E501
        'credits': 'credits',  # noqa: E501
        'lecturing_volume': 'lecturing_volume',  # noqa: E501
        'practical_exercise_volume': 'practical_exercise_volume',  # noqa: E501
        'proposal_type': 'proposal_type',  # noqa: E501
        'status': 'status',  # noqa: E501
        'quadrimester': 'quadrimester',  # noqa: E501
        'periodicity': 'periodicity',  # noqa: E501
        'comment_en': 'comment_en',  # noqa: E501
        'with_prerequisite': 'with_prerequisite',  # noqa: E501
        'min_constraint': 'min_constraint',  # noqa: E501
        'max_constraint': 'max_constraint',  # noqa: E501
        'constraint_type': 'constraint_type',  # noqa: E501
        'version_name': 'version_name',  # noqa: E501
        'language': 'language',  # noqa: E501
        'french_friendly': 'french_friendly',  # noqa: E501
        'english_friendly': 'english_friendly',  # noqa: E501
        'exchange_students': 'exchange_students',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, url, code, title, node_type, subtype, is_mandatory, block, access_condition, comment, remark, remark_en, link_type, link_type_text, children, *args, **kwargs):  # noqa: E501
        """Node - a model defined in OpenAPI

        Args:
            url (str):
            code (str):
            title (str):
            node_type (NodeTypeEnum):
            subtype (NodeSubTypeEnum):
            is_mandatory (bool):
            block ([int]):
            access_condition (bool):
            comment (str):
            remark (str):
            remark_en (str):
            link_type (NodeLinkTypeEnum):
            link_type_text (str):
            children ([Node]):

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
            acronym (str): [optional]  # noqa: E501
            title_en (str): [optional]  # noqa: E501
            partial_title (str): [optional]  # noqa: E501
            partial_title_en (str): [optional]  # noqa: E501
            credits (float): [optional]  # noqa: E501
            lecturing_volume (float): [optional]  # noqa: E501
            practical_exercise_volume (float): [optional]  # noqa: E501
            proposal_type (ProposalTypeEnum): [optional]  # noqa: E501
            status (bool): [optional]  # noqa: E501
            quadrimester (QuadrimesterEnum): [optional]  # noqa: E501
            periodicity (PeriodicityEnum): [optional]  # noqa: E501
            comment_en (str): [optional]  # noqa: E501
            with_prerequisite (bool): [optional]  # noqa: E501
            min_constraint (int): [optional]  # noqa: E501
            max_constraint (int): [optional]  # noqa: E501
            constraint_type (ConstraintTypeEnum): [optional]  # noqa: E501
            version_name (str): [optional]  # noqa: E501
            language (str): The language code according to ISO 639-1 specification (https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) . [optional]  # noqa: E501
            french_friendly (bool): [optional]  # noqa: E501
            english_friendly (bool): [optional]  # noqa: E501
            exchange_students (bool): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
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

        self.url = url
        self.code = code
        self.title = title
        self.node_type = node_type
        self.subtype = subtype
        self.is_mandatory = is_mandatory
        self.block = block
        self.access_condition = access_condition
        self.comment = comment
        self.remark = remark
        self.remark_en = remark_en
        self.link_type = link_type
        self.link_type_text = link_type_text
        self.children = children
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
