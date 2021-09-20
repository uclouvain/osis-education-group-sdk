"""
    Education Group Service

    A set of API endpoints that allow you to get, update, delete an education group.  # noqa: E501

    The version of the OpenAPI document: 1.08
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_education_group_sdk
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
from osis_education_group_sdk.model.node import Node


class TestNode(unittest.TestCase):
    """Node unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNode(self):
        """Test Node"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Node()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()