"""
    Education Group Service

    A set of API endpoints that allow you to get, update, delete an education group.  # noqa: E501

    The version of the OpenAPI document: 1.08
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_education_group_sdk
from osis_education_group_sdk.model.paginated_training_all_of import PaginatedTrainingAllOf
from osis_education_group_sdk.model.pagination import Pagination
from osis_education_group_sdk.model.training import Training
globals()['PaginatedTrainingAllOf'] = PaginatedTrainingAllOf
globals()['Pagination'] = Pagination
globals()['Training'] = Training
from osis_education_group_sdk.model.paginated_training import PaginatedTraining


class TestPaginatedTraining(unittest.TestCase):
    """PaginatedTraining unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedTraining(self):
        """Test PaginatedTraining"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedTraining()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()