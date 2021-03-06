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


class User(object):
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
        'id': 'str',
        'oauth_id': 'str',
        'name': 'str',
        'status': 'str',
        'links': 'UserLinks'
    }

    attribute_map = {
        'id': 'id',
        'oauth_id': 'oauthID',
        'name': 'name',
        'status': 'status',
        'links': 'links'
    }

    def __init__(self, id=None, oauth_id=None, name=None, status='active', links=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501

        self._id = None
        self._oauth_id = None
        self._name = None
        self._status = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if oauth_id is not None:
            self.oauth_id = oauth_id
        self.name = name
        if status is not None:
            self.status = status
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501


        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.


        :param id: The id of this User.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def oauth_id(self):
        """Gets the oauth_id of this User.  # noqa: E501


        :return: The oauth_id of this User.  # noqa: E501
        :rtype: str
        """
        return self._oauth_id

    @oauth_id.setter
    def oauth_id(self, oauth_id):
        """Sets the oauth_id of this User.


        :param oauth_id: The oauth_id of this User.  # noqa: E501
        :type: str
        """

        self._oauth_id = oauth_id

    @property
    def name(self):
        """Gets the name of this User.  # noqa: E501


        :return: The name of this User.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this User.


        :param name: The name of this User.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def status(self):
        """Gets the status of this User.  # noqa: E501

        If inactive the user is inactive.  # noqa: E501

        :return: The status of this User.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this User.

        If inactive the user is inactive.  # noqa: E501

        :param status: The status of this User.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def links(self):
        """Gets the links of this User.  # noqa: E501


        :return: The links of this User.  # noqa: E501
        :rtype: UserLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this User.


        :param links: The links of this User.  # noqa: E501
        :type: UserLinks
        """

        self._links = links

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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
