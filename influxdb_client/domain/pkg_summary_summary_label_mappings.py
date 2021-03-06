# coding: utf-8

"""
    Influx API Service

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class PkgSummarySummaryLabelMappings(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'resource_name': 'str',
        'resource_id': 'str',
        'resource_type': 'str',
        'label_name': 'str',
        'label_id': 'str'
    }

    attribute_map = {
        'resource_name': 'resourceName',
        'resource_id': 'resourceID',
        'resource_type': 'resourceType',
        'label_name': 'labelName',
        'label_id': 'labelID'
    }

    def __init__(self, resource_name=None, resource_id=None, resource_type=None, label_name=None, label_id=None):  # noqa: E501
        """PkgSummarySummaryLabelMappings - a model defined in OpenAPI"""  # noqa: E501

        self._resource_name = None
        self._resource_id = None
        self._resource_type = None
        self._label_name = None
        self._label_id = None
        self.discriminator = None

        if resource_name is not None:
            self.resource_name = resource_name
        if resource_id is not None:
            self.resource_id = resource_id
        if resource_type is not None:
            self.resource_type = resource_type
        if label_name is not None:
            self.label_name = label_name
        if label_id is not None:
            self.label_id = label_id

    @property
    def resource_name(self):
        """Gets the resource_name of this PkgSummarySummaryLabelMappings.  # noqa: E501


        :return: The resource_name of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        """Sets the resource_name of this PkgSummarySummaryLabelMappings.


        :param resource_name: The resource_name of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :type: str
        """

        self._resource_name = resource_name

    @property
    def resource_id(self):
        """Gets the resource_id of this PkgSummarySummaryLabelMappings.  # noqa: E501


        :return: The resource_id of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this PkgSummarySummaryLabelMappings.


        :param resource_id: The resource_id of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :type: str
        """

        self._resource_id = resource_id

    @property
    def resource_type(self):
        """Gets the resource_type of this PkgSummarySummaryLabelMappings.  # noqa: E501


        :return: The resource_type of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this PkgSummarySummaryLabelMappings.


        :param resource_type: The resource_type of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :type: str
        """

        self._resource_type = resource_type

    @property
    def label_name(self):
        """Gets the label_name of this PkgSummarySummaryLabelMappings.  # noqa: E501


        :return: The label_name of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        """Sets the label_name of this PkgSummarySummaryLabelMappings.


        :param label_name: The label_name of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :type: str
        """

        self._label_name = label_name

    @property
    def label_id(self):
        """Gets the label_id of this PkgSummarySummaryLabelMappings.  # noqa: E501


        :return: The label_id of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :rtype: str
        """
        return self._label_id

    @label_id.setter
    def label_id(self, label_id):
        """Sets the label_id of this PkgSummarySummaryLabelMappings.


        :param label_id: The label_id of this PkgSummarySummaryLabelMappings.  # noqa: E501
        :type: str
        """

        self._label_id = label_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PkgSummarySummaryLabelMappings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
