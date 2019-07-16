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


class TableViewProperties(object):
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
        'shape': 'str',
        'type': 'str',
        'table_options': 'object',
        'field_options': 'list[RenamableField]',
        'time_format': 'str',
        'decimal_places': 'DecimalPlaces'
    }

    attribute_map = {
        'shape': 'shape',
        'type': 'type',
        'table_options': 'tableOptions',
        'field_options': 'fieldOptions',
        'time_format': 'timeFormat',
        'decimal_places': 'decimalPlaces'
    }

    def __init__(self, shape=None, type=None, table_options=None, field_options=None, time_format=None, decimal_places=None):  # noqa: E501
        """TableViewProperties - a model defined in OpenAPI"""  # noqa: E501

        self._shape = None
        self._type = None
        self._table_options = None
        self._field_options = None
        self._time_format = None
        self._decimal_places = None
        self.discriminator = None

        if shape is not None:
            self.shape = shape
        if type is not None:
            self.type = type
        if table_options is not None:
            self.table_options = table_options
        if field_options is not None:
            self.field_options = field_options
        if time_format is not None:
            self.time_format = time_format
        if decimal_places is not None:
            self.decimal_places = decimal_places

    @property
    def shape(self):
        """Gets the shape of this TableViewProperties.  # noqa: E501


        :return: The shape of this TableViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._shape

    @shape.setter
    def shape(self, shape):
        """Sets the shape of this TableViewProperties.


        :param shape: The shape of this TableViewProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["chronograf-v2"]  # noqa: E501
        if shape not in allowed_values:
            raise ValueError(
                "Invalid value for `shape` ({0}), must be one of {1}"  # noqa: E501
                .format(shape, allowed_values)
            )

        self._shape = shape

    @property
    def type(self):
        """Gets the type of this TableViewProperties.  # noqa: E501


        :return: The type of this TableViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TableViewProperties.


        :param type: The type of this TableViewProperties.  # noqa: E501
        :type: str
        """
        allowed_values = ["table"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def table_options(self):
        """Gets the table_options of this TableViewProperties.  # noqa: E501


        :return: The table_options of this TableViewProperties.  # noqa: E501
        :rtype: object
        """
        return self._table_options

    @table_options.setter
    def table_options(self, table_options):
        """Sets the table_options of this TableViewProperties.


        :param table_options: The table_options of this TableViewProperties.  # noqa: E501
        :type: object
        """

        self._table_options = table_options

    @property
    def field_options(self):
        """Gets the field_options of this TableViewProperties.  # noqa: E501

        fieldOptions represent the fields retrieved by the query with customization options  # noqa: E501

        :return: The field_options of this TableViewProperties.  # noqa: E501
        :rtype: list[RenamableField]
        """
        return self._field_options

    @field_options.setter
    def field_options(self, field_options):
        """Sets the field_options of this TableViewProperties.

        fieldOptions represent the fields retrieved by the query with customization options  # noqa: E501

        :param field_options: The field_options of this TableViewProperties.  # noqa: E501
        :type: list[RenamableField]
        """

        self._field_options = field_options

    @property
    def time_format(self):
        """Gets the time_format of this TableViewProperties.  # noqa: E501

        timeFormat describes the display format for time values according to moment.js date formatting  # noqa: E501

        :return: The time_format of this TableViewProperties.  # noqa: E501
        :rtype: str
        """
        return self._time_format

    @time_format.setter
    def time_format(self, time_format):
        """Sets the time_format of this TableViewProperties.

        timeFormat describes the display format for time values according to moment.js date formatting  # noqa: E501

        :param time_format: The time_format of this TableViewProperties.  # noqa: E501
        :type: str
        """

        self._time_format = time_format

    @property
    def decimal_places(self):
        """Gets the decimal_places of this TableViewProperties.  # noqa: E501


        :return: The decimal_places of this TableViewProperties.  # noqa: E501
        :rtype: DecimalPlaces
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this TableViewProperties.


        :param decimal_places: The decimal_places of this TableViewProperties.  # noqa: E501
        :type: DecimalPlaces
        """

        self._decimal_places = decimal_places

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
        if not isinstance(other, TableViewProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other