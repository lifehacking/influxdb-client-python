# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import influxdb2
from influxdb2.api.dashboards_api import DashboardsApi  # noqa: E501
from influxdb2.rest import ApiException


class TestDashboardsApi(unittest.TestCase):
    """DashboardsApi unit test stubs"""

    def setUp(self):
        self.api = influxdb2.api.dashboards_api.DashboardsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_dashboards_id(self):
        """Test case for delete_dashboards_id

        Delete a dashboard  # noqa: E501
        """
        pass

    def test_delete_dashboards_id_cells_id(self):
        """Test case for delete_dashboards_id_cells_id

        Delete a dashboard cell  # noqa: E501
        """
        pass

    def test_delete_dashboards_id_labels_id(self):
        """Test case for delete_dashboards_id_labels_id

        delete a label from a dashboard  # noqa: E501
        """
        pass

    def test_delete_dashboards_id_members_id(self):
        """Test case for delete_dashboards_id_members_id

        removes a member from an dashboard  # noqa: E501
        """
        pass

    def test_delete_dashboards_id_owners_id(self):
        """Test case for delete_dashboards_id_owners_id

        removes an owner from a dashboard  # noqa: E501
        """
        pass

    def test_get_dashboards(self):
        """Test case for get_dashboards

        Get all dashboards  # noqa: E501
        """
        pass

    def test_get_dashboards_id(self):
        """Test case for get_dashboards_id

        Get a single Dashboard  # noqa: E501
        """
        pass

    def test_get_dashboards_id_cells_id_view(self):
        """Test case for get_dashboards_id_cells_id_view

        Retrieve the view for a cell in a dashboard  # noqa: E501
        """
        pass

    def test_get_dashboards_id_labels(self):
        """Test case for get_dashboards_id_labels

        list all labels for a dashboard  # noqa: E501
        """
        pass

    def test_get_dashboards_id_logs(self):
        """Test case for get_dashboards_id_logs

        Retrieve operation logs for a dashboard  # noqa: E501
        """
        pass

    def test_get_dashboards_id_members(self):
        """Test case for get_dashboards_id_members

        List all dashboard members  # noqa: E501
        """
        pass

    def test_get_dashboards_id_owners(self):
        """Test case for get_dashboards_id_owners

        List all dashboard owners  # noqa: E501
        """
        pass

    def test_patch_dashboards_id(self):
        """Test case for patch_dashboards_id

        Update a single dashboard  # noqa: E501
        """
        pass

    def test_patch_dashboards_id_cells_id(self):
        """Test case for patch_dashboards_id_cells_id

        Update the non positional information related to a cell (because updates to a single cells positional data could cause grid conflicts)  # noqa: E501
        """
        pass

    def test_patch_dashboards_id_cells_id_view(self):
        """Test case for patch_dashboards_id_cells_id_view

        Update the view for a cell  # noqa: E501
        """
        pass

    def test_post_dashboards(self):
        """Test case for post_dashboards

        Create a dashboard  # noqa: E501
        """
        pass

    def test_post_dashboards_id_cells(self):
        """Test case for post_dashboards_id_cells

        Create a dashboard cell  # noqa: E501
        """
        pass

    def test_post_dashboards_id_labels(self):
        """Test case for post_dashboards_id_labels

        add a label to a dashboard  # noqa: E501
        """
        pass

    def test_post_dashboards_id_members(self):
        """Test case for post_dashboards_id_members

        Add dashboard member  # noqa: E501
        """
        pass

    def test_post_dashboards_id_owners(self):
        """Test case for post_dashboards_id_owners

        Add dashboard owner  # noqa: E501
        """
        pass

    def test_put_dashboards_id_cells(self):
        """Test case for put_dashboards_id_cells

        Replace a dashboards cells  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()