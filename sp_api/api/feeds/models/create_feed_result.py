# coding: utf-8

"""
    Selling Partner API for Feeds

    The Selling Partner API for Feeds lets you upload data to Amazon on behalf of a selling partner.  # noqa: E501

    OpenAPI spec version: 2020-09-04
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class CreateFeedResult(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'feed_id': 'str'
    }

    attribute_map = {
        'feed_id': 'feedId'
    }

    def __init__(self, feed_id=None):  # noqa: E501
        """CreateFeedResult - a model defined in Swagger"""  # noqa: E501
        self._feed_id = None
        self.discriminator = None
        self.feed_id = feed_id

    @property
    def feed_id(self):
        """Gets the feed_id of this CreateFeedResult.  # noqa: E501

        The identifier for the feed. This identifier is unique only in combination with a seller ID.  # noqa: E501

        :return: The feed_id of this CreateFeedResult.  # noqa: E501
        :rtype: str
        """
        return self._feed_id

    @feed_id.setter
    def feed_id(self, feed_id):
        """Sets the feed_id of this CreateFeedResult.

        The identifier for the feed. This identifier is unique only in combination with a seller ID.  # noqa: E501

        :param feed_id: The feed_id of this CreateFeedResult.  # noqa: E501
        :type: str
        """
        if feed_id is None:
            raise ValueError("Invalid value for `feed_id`, must not be `None`")  # noqa: E501

        self._feed_id = feed_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(CreateFeedResult, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateFeedResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
