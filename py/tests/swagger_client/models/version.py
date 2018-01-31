# coding: utf-8

"""
    Aeternity Epoch

    This is the [Aeternity](https://www.aeternity.com/) Epoch API.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@aeternity.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Version(object):
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
        'version': 'str',
        'revision': 'str',
        'genesis_hash': 'str'
    }

    attribute_map = {
        'version': 'version',
        'revision': 'revision',
        'genesis_hash': 'genesis_hash'
    }

    def __init__(self, version=None, revision=None, genesis_hash=None):  # noqa: E501
        """Version - a model defined in Swagger"""  # noqa: E501

        self._version = None
        self._revision = None
        self._genesis_hash = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if revision is not None:
            self.revision = revision
        if genesis_hash is not None:
            self.genesis_hash = genesis_hash

    @property
    def version(self):
        """Gets the version of this Version.  # noqa: E501


        :return: The version of this Version.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Version.


        :param version: The version of this Version.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def revision(self):
        """Gets the revision of this Version.  # noqa: E501


        :return: The revision of this Version.  # noqa: E501
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this Version.


        :param revision: The revision of this Version.  # noqa: E501
        :type: str
        """

        self._revision = revision

    @property
    def genesis_hash(self):
        """Gets the genesis_hash of this Version.  # noqa: E501


        :return: The genesis_hash of this Version.  # noqa: E501
        :rtype: str
        """
        return self._genesis_hash

    @genesis_hash.setter
    def genesis_hash(self, genesis_hash):
        """Sets the genesis_hash of this Version.


        :param genesis_hash: The genesis_hash of this Version.  # noqa: E501
        :type: str
        """

        self._genesis_hash = genesis_hash

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
