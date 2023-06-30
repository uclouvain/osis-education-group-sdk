"""
    Education Group Service

    A set of API endpoints that allow you to get, update, delete an education group.  # noqa: E501

    The version of the OpenAPI document: 1.12
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_education_group_sdk
from osis_education_group_sdk.model.campus import Campus
from osis_education_group_sdk.model.constraint_type_enum import ConstraintTypeEnum
from osis_education_group_sdk.model.group_type_enum import GroupTypeEnum
globals()['Campus'] = Campus
globals()['ConstraintTypeEnum'] = ConstraintTypeEnum
globals()['GroupTypeEnum'] = GroupTypeEnum
from osis_education_group_sdk.model.group_detailed import GroupDetailed


class TestGroupDetailed(unittest.TestCase):
    """GroupDetailed unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGroupDetailed(self):
        """Test GroupDetailed"""
        # FIXME: construct object with mandatory attributes with example values
        # model = GroupDetailed()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
