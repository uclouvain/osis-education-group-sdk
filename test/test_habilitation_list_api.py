"""
    Education Group Service

    A set of API endpoints that allow you to get, update, delete an education group.  # noqa: E501

    The version of the OpenAPI document: 1.08
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_education_group_sdk
from osis_education_group_sdk.api.habilitation_list_api import HabilitationListApi  # noqa: E501


class TestHabilitationListApi(unittest.TestCase):
    """HabilitationListApi unit test stubs"""

    def setUp(self):
        self.api = HabilitationListApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_habilitations_list(self):
        """Test case for habilitations_list

        """
        pass


if __name__ == '__main__':
    unittest.main()