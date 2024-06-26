# coding: utf-8

"""
    CartoVista REST API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class DataColumnCreateParameter(object):
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
        'identifier': 'str',
        'carto_vista_data_type': 'CartoVistaPortalDataType',
        'name': 'str',
        'description': 'str',
        'metadata': 'str',
        'units': 'str',
        'unit_placement': 'OneOfDataColumnCreateParameterUnitPlacement',
        'aggregation_type': 'OneOfDataColumnCreateParameterAggregationType',
        'mappable': 'bool',
        'precision': 'int',
        'round_to_precision': 'bool',
        'time_stamp': 'object',
        'time_stamp_accuracy': 'object',
        'not_available_values': 'bool',
        'value_to_convert': 'float',
        'system_identifier': 'str'
    }

    attribute_map = {
        'identifier': 'identifier',
        'carto_vista_data_type': 'cartoVistaDataType',
        'name': 'name',
        'description': 'description',
        'metadata': 'metadata',
        'units': 'units',
        'unit_placement': 'unitPlacement',
        'aggregation_type': 'aggregationType',
        'mappable': 'mappable',
        'precision': 'precision',
        'round_to_precision': 'roundToPrecision',
        'time_stamp': 'timeStamp',
        'time_stamp_accuracy': 'timeStampAccuracy',
        'not_available_values': 'notAvailableValues',
        'value_to_convert': 'valueToConvert',
        'system_identifier': 'systemIdentifier'
    }

    def __init__(self, identifier=None, carto_vista_data_type=None, name=None, description=None, metadata=None, units=None, unit_placement=None, aggregation_type=None, mappable=None, precision=None, round_to_precision=None, time_stamp=None, time_stamp_accuracy=None, not_available_values=None, value_to_convert=None, system_identifier=None):  # noqa: E501
        """DataColumnCreateParameter - a model defined in Swagger"""  # noqa: E501
        self._identifier = None
        self._carto_vista_data_type = None
        self._name = None
        self._description = None
        self._metadata = None
        self._units = None
        self._unit_placement = None
        self._aggregation_type = None
        self._mappable = None
        self._precision = None
        self._round_to_precision = None
        self._time_stamp = None
        self._time_stamp_accuracy = None
        self._not_available_values = None
        self._value_to_convert = None
        self._system_identifier = None
        self.discriminator = None
        if identifier is not None:
            self.identifier = identifier
        if carto_vista_data_type is not None:
            self.carto_vista_data_type = carto_vista_data_type
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if metadata is not None:
            self.metadata = metadata
        if units is not None:
            self.units = units
        if unit_placement is not None:
            self.unit_placement = unit_placement
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type
        if mappable is not None:
            self.mappable = mappable
        if precision is not None:
            self.precision = precision
        if round_to_precision is not None:
            self.round_to_precision = round_to_precision
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if time_stamp_accuracy is not None:
            self.time_stamp_accuracy = time_stamp_accuracy
        if not_available_values is not None:
            self.not_available_values = not_available_values
        if value_to_convert is not None:
            self.value_to_convert = value_to_convert
        if system_identifier is not None:
            self.system_identifier = system_identifier

    @property
    def identifier(self):
        """Gets the identifier of this DataColumnCreateParameter.  # noqa: E501


        :return: The identifier of this DataColumnCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this DataColumnCreateParameter.


        :param identifier: The identifier of this DataColumnCreateParameter.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def carto_vista_data_type(self):
        """Gets the carto_vista_data_type of this DataColumnCreateParameter.  # noqa: E501


        :return: The carto_vista_data_type of this DataColumnCreateParameter.  # noqa: E501
        :rtype: CartoVistaPortalDataType
        """
        return self._carto_vista_data_type

    @carto_vista_data_type.setter
    def carto_vista_data_type(self, carto_vista_data_type):
        """Sets the carto_vista_data_type of this DataColumnCreateParameter.


        :param carto_vista_data_type: The carto_vista_data_type of this DataColumnCreateParameter.  # noqa: E501
        :type: CartoVistaPortalDataType
        """

        self._carto_vista_data_type = carto_vista_data_type

    @property
    def name(self):
        """Gets the name of this DataColumnCreateParameter.  # noqa: E501


        :return: The name of this DataColumnCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DataColumnCreateParameter.


        :param name: The name of this DataColumnCreateParameter.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this DataColumnCreateParameter.  # noqa: E501


        :return: The description of this DataColumnCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DataColumnCreateParameter.


        :param description: The description of this DataColumnCreateParameter.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def metadata(self):
        """Gets the metadata of this DataColumnCreateParameter.  # noqa: E501


        :return: The metadata of this DataColumnCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DataColumnCreateParameter.


        :param metadata: The metadata of this DataColumnCreateParameter.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def units(self):
        """Gets the units of this DataColumnCreateParameter.  # noqa: E501


        :return: The units of this DataColumnCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this DataColumnCreateParameter.


        :param units: The units of this DataColumnCreateParameter.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def unit_placement(self):
        """Gets the unit_placement of this DataColumnCreateParameter.  # noqa: E501


        :return: The unit_placement of this DataColumnCreateParameter.  # noqa: E501
        :rtype: OneOfDataColumnCreateParameterUnitPlacement
        """
        return self._unit_placement

    @unit_placement.setter
    def unit_placement(self, unit_placement):
        """Sets the unit_placement of this DataColumnCreateParameter.


        :param unit_placement: The unit_placement of this DataColumnCreateParameter.  # noqa: E501
        :type: OneOfDataColumnCreateParameterUnitPlacement
        """

        self._unit_placement = unit_placement

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this DataColumnCreateParameter.  # noqa: E501


        :return: The aggregation_type of this DataColumnCreateParameter.  # noqa: E501
        :rtype: OneOfDataColumnCreateParameterAggregationType
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this DataColumnCreateParameter.


        :param aggregation_type: The aggregation_type of this DataColumnCreateParameter.  # noqa: E501
        :type: OneOfDataColumnCreateParameterAggregationType
        """

        self._aggregation_type = aggregation_type

    @property
    def mappable(self):
        """Gets the mappable of this DataColumnCreateParameter.  # noqa: E501


        :return: The mappable of this DataColumnCreateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._mappable

    @mappable.setter
    def mappable(self, mappable):
        """Sets the mappable of this DataColumnCreateParameter.


        :param mappable: The mappable of this DataColumnCreateParameter.  # noqa: E501
        :type: bool
        """

        self._mappable = mappable

    @property
    def precision(self):
        """Gets the precision of this DataColumnCreateParameter.  # noqa: E501


        :return: The precision of this DataColumnCreateParameter.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this DataColumnCreateParameter.


        :param precision: The precision of this DataColumnCreateParameter.  # noqa: E501
        :type: int
        """

        self._precision = precision

    @property
    def round_to_precision(self):
        """Gets the round_to_precision of this DataColumnCreateParameter.  # noqa: E501


        :return: The round_to_precision of this DataColumnCreateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._round_to_precision

    @round_to_precision.setter
    def round_to_precision(self, round_to_precision):
        """Sets the round_to_precision of this DataColumnCreateParameter.


        :param round_to_precision: The round_to_precision of this DataColumnCreateParameter.  # noqa: E501
        :type: bool
        """

        self._round_to_precision = round_to_precision

    @property
    def time_stamp(self):
        """Gets the time_stamp of this DataColumnCreateParameter.  # noqa: E501


        :return: The time_stamp of this DataColumnCreateParameter.  # noqa: E501
        :rtype: object
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        """Sets the time_stamp of this DataColumnCreateParameter.


        :param time_stamp: The time_stamp of this DataColumnCreateParameter.  # noqa: E501
        :type: object
        """

        self._time_stamp = time_stamp

    @property
    def time_stamp_accuracy(self):
        """Gets the time_stamp_accuracy of this DataColumnCreateParameter.  # noqa: E501


        :return: The time_stamp_accuracy of this DataColumnCreateParameter.  # noqa: E501
        :rtype: object
        """
        return self._time_stamp_accuracy

    @time_stamp_accuracy.setter
    def time_stamp_accuracy(self, time_stamp_accuracy):
        """Sets the time_stamp_accuracy of this DataColumnCreateParameter.


        :param time_stamp_accuracy: The time_stamp_accuracy of this DataColumnCreateParameter.  # noqa: E501
        :type: object
        """

        self._time_stamp_accuracy = time_stamp_accuracy

    @property
    def not_available_values(self):
        """Gets the not_available_values of this DataColumnCreateParameter.  # noqa: E501


        :return: The not_available_values of this DataColumnCreateParameter.  # noqa: E501
        :rtype: bool
        """
        return self._not_available_values

    @not_available_values.setter
    def not_available_values(self, not_available_values):
        """Sets the not_available_values of this DataColumnCreateParameter.


        :param not_available_values: The not_available_values of this DataColumnCreateParameter.  # noqa: E501
        :type: bool
        """

        self._not_available_values = not_available_values

    @property
    def value_to_convert(self):
        """Gets the value_to_convert of this DataColumnCreateParameter.  # noqa: E501


        :return: The value_to_convert of this DataColumnCreateParameter.  # noqa: E501
        :rtype: float
        """
        return self._value_to_convert

    @value_to_convert.setter
    def value_to_convert(self, value_to_convert):
        """Sets the value_to_convert of this DataColumnCreateParameter.


        :param value_to_convert: The value_to_convert of this DataColumnCreateParameter.  # noqa: E501
        :type: float
        """

        self._value_to_convert = value_to_convert

    @property
    def system_identifier(self):
        """Gets the system_identifier of this DataColumnCreateParameter.  # noqa: E501


        :return: The system_identifier of this DataColumnCreateParameter.  # noqa: E501
        :rtype: str
        """
        return self._system_identifier

    @system_identifier.setter
    def system_identifier(self, system_identifier):
        """Sets the system_identifier of this DataColumnCreateParameter.


        :param system_identifier: The system_identifier of this DataColumnCreateParameter.  # noqa: E501
        :type: str
        """

        self._system_identifier = system_identifier

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
        if issubclass(DataColumnCreateParameter, dict):
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
        if not isinstance(other, DataColumnCreateParameter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
