"""
    Education Group Service

    A set of API endpoints that allow you to get, update, delete an education group.  # noqa: E501

    The version of the OpenAPI document: 1.12
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_education_group_sdk
from osis_education_group_sdk.model.mini_training import MiniTraining
from osis_education_group_sdk.model.paginated_mini_training_all_of import PaginatedMiniTrainingAllOf
from osis_education_group_sdk.model.pagination import Pagination
globals()['MiniTraining'] = MiniTraining
globals()['PaginatedMiniTrainingAllOf'] = PaginatedMiniTrainingAllOf
globals()['Pagination'] = Pagination
from osis_education_group_sdk.model.paginated_mini_training import PaginatedMiniTraining


class TestPaginatedMiniTraining(unittest.TestCase):
    """PaginatedMiniTraining unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedMiniTraining(self):
        """Test PaginatedMiniTraining"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedMiniTraining()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
