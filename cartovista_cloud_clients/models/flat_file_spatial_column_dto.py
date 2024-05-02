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

class FlatFileSpatialColumnDTO(object):
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
        'id': 'str',
        'name': 'str',
        'original_name': 'str',
        'description': 'str',
        'is_empty': 'bool',
        'metadata': 'str',
        'units': 'str',
        'unit_placement': 'UnitPlacement',
        'values': 'list[object]',
        'column_number': 'int',
        'data_type': 'CartoVistaPortalDataType',
        'unremovable': 'bool',
        'precision': 'int',
        'round_to_precision': 'bool',
        'mappable': 'bool',
        'not_availablevalues': 'bool',
        'value_to_convert': 'float',
        'aggregation_type': 'AggregationType',
        'format_data_type': 'OneOfFlatFileSpatialColumnDTOFormatDataType',
        'ogr_field_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'original_name': 'originalName',
        'description': 'description',
        'is_empty': 'isEmpty',
        'metadata': 'metadata',
        'units': 'units',
        'unit_placement': 'unitPlacement',
        'values': 'values',
        'column_number': 'columnNumber',
        'data_type': 'dataType',
        'unremovable': 'unremovable',
        'precision': 'precision',
        'round_to_precision': 'roundToPrecision',
        'mappable': 'mappable',
        'not_availablevalues': 'notAvailablevalues',
        'value_to_convert': 'valueToConvert',
        'aggregation_type': 'aggregationType',
        'format_data_type': 'formatDataType',
        'ogr_field_type': 'ogrFieldType'
    }

    def __init__(self, id=None, name=None, original_name=None, description=None, is_empty=None, metadata=None, units=None, unit_placement=None, values=None, column_number=None, data_type=None, unremovable=None, precision=None, round_to_precision=None, mappable=None, not_availablevalues=None, value_to_convert=None, aggregation_type=None, format_data_type=None, ogr_field_type=None):  # noqa: E501
        """FlatFileSpatialColumnDTO - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._original_name = None
        self._description = None
        self._is_empty = None
        self._metadata = None
        self._units = None
        self._unit_placement = None
        self._values = None
        self._column_number = None
        self._data_type = None
        self._unremovable = None
        self._precision = None
        self._round_to_precision = None
        self._mappable = None
        self._not_availablevalues = None
        self._value_to_convert = None
        self._aggregation_type = None
        self._format_data_type = None
        self._ogr_field_type = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if original_name is not None:
            self.original_name = original_name
        if description is not None:
            self.description = description
        if is_empty is not None:
            self.is_empty = is_empty
        if metadata is not None:
            self.metadata = metadata
        if units is not None:
            self.units = units
        if unit_placement is not None:
            self.unit_placement = unit_placement
        if values is not None:
            self.values = values
        if column_number is not None:
            self.column_number = column_number
        if data_type is not None:
            self.data_type = data_type
        if unremovable is not None:
            self.unremovable = unremovable
        if precision is not None:
            self.precision = precision
        if round_to_precision is not None:
            self.round_to_precision = round_to_precision
        if mappable is not None:
            self.mappable = mappable
        if not_availablevalues is not None:
            self.not_availablevalues = not_availablevalues
        if value_to_convert is not None:
            self.value_to_convert = value_to_convert
        if aggregation_type is not None:
            self.aggregation_type = aggregation_type
        if format_data_type is not None:
            self.format_data_type = format_data_type
        if ogr_field_type is not None:
            self.ogr_field_type = ogr_field_type

    @property
    def id(self):
        """Gets the id of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The id of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlatFileSpatialColumnDTO.


        :param id: The id of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The name of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlatFileSpatialColumnDTO.


        :param name: The name of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def original_name(self):
        """Gets the original_name of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The original_name of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._original_name

    @original_name.setter
    def original_name(self, original_name):
        """Sets the original_name of this FlatFileSpatialColumnDTO.


        :param original_name: The original_name of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: str
        """

        self._original_name = original_name

    @property
    def description(self):
        """Gets the description of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The description of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FlatFileSpatialColumnDTO.


        :param description: The description of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_empty(self):
        """Gets the is_empty of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The is_empty of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._is_empty

    @is_empty.setter
    def is_empty(self, is_empty):
        """Sets the is_empty of this FlatFileSpatialColumnDTO.


        :param is_empty: The is_empty of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: bool
        """

        self._is_empty = is_empty

    @property
    def metadata(self):
        """Gets the metadata of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The metadata of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this FlatFileSpatialColumnDTO.


        :param metadata: The metadata of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: str
        """

        self._metadata = metadata

    @property
    def units(self):
        """Gets the units of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The units of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this FlatFileSpatialColumnDTO.


        :param units: The units of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: str
        """

        self._units = units

    @property
    def unit_placement(self):
        """Gets the unit_placement of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The unit_placement of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: UnitPlacement
        """
        return self._unit_placement

    @unit_placement.setter
    def unit_placement(self, unit_placement):
        """Sets the unit_placement of this FlatFileSpatialColumnDTO.


        :param unit_placement: The unit_placement of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: UnitPlacement
        """

        self._unit_placement = unit_placement

    @property
    def values(self):
        """Gets the values of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The values of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: list[object]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this FlatFileSpatialColumnDTO.


        :param values: The values of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: list[object]
        """

        self._values = values

    @property
    def column_number(self):
        """Gets the column_number of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The column_number of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: int
        """
        return self._column_number

    @column_number.setter
    def column_number(self, column_number):
        """Sets the column_number of this FlatFileSpatialColumnDTO.


        :param column_number: The column_number of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: int
        """

        self._column_number = column_number

    @property
    def data_type(self):
        """Gets the data_type of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The data_type of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: CartoVistaPortalDataType
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this FlatFileSpatialColumnDTO.


        :param data_type: The data_type of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: CartoVistaPortalDataType
        """

        self._data_type = data_type

    @property
    def unremovable(self):
        """Gets the unremovable of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The unremovable of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._unremovable

    @unremovable.setter
    def unremovable(self, unremovable):
        """Sets the unremovable of this FlatFileSpatialColumnDTO.


        :param unremovable: The unremovable of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: bool
        """

        self._unremovable = unremovable

    @property
    def precision(self):
        """Gets the precision of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The precision of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this FlatFileSpatialColumnDTO.


        :param precision: The precision of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: int
        """

        self._precision = precision

    @property
    def round_to_precision(self):
        """Gets the round_to_precision of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The round_to_precision of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._round_to_precision

    @round_to_precision.setter
    def round_to_precision(self, round_to_precision):
        """Sets the round_to_precision of this FlatFileSpatialColumnDTO.


        :param round_to_precision: The round_to_precision of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: bool
        """

        self._round_to_precision = round_to_precision

    @property
    def mappable(self):
        """Gets the mappable of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The mappable of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._mappable

    @mappable.setter
    def mappable(self, mappable):
        """Sets the mappable of this FlatFileSpatialColumnDTO.


        :param mappable: The mappable of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: bool
        """

        self._mappable = mappable

    @property
    def not_availablevalues(self):
        """Gets the not_availablevalues of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The not_availablevalues of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: bool
        """
        return self._not_availablevalues

    @not_availablevalues.setter
    def not_availablevalues(self, not_availablevalues):
        """Sets the not_availablevalues of this FlatFileSpatialColumnDTO.


        :param not_availablevalues: The not_availablevalues of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: bool
        """

        self._not_availablevalues = not_availablevalues

    @property
    def value_to_convert(self):
        """Gets the value_to_convert of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The value_to_convert of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: float
        """
        return self._value_to_convert

    @value_to_convert.setter
    def value_to_convert(self, value_to_convert):
        """Sets the value_to_convert of this FlatFileSpatialColumnDTO.


        :param value_to_convert: The value_to_convert of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: float
        """

        self._value_to_convert = value_to_convert

    @property
    def aggregation_type(self):
        """Gets the aggregation_type of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The aggregation_type of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: AggregationType
        """
        return self._aggregation_type

    @aggregation_type.setter
    def aggregation_type(self, aggregation_type):
        """Sets the aggregation_type of this FlatFileSpatialColumnDTO.


        :param aggregation_type: The aggregation_type of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: AggregationType
        """

        self._aggregation_type = aggregation_type

    @property
    def format_data_type(self):
        """Gets the format_data_type of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The format_data_type of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: OneOfFlatFileSpatialColumnDTOFormatDataType
        """
        return self._format_data_type

    @format_data_type.setter
    def format_data_type(self, format_data_type):
        """Sets the format_data_type of this FlatFileSpatialColumnDTO.


        :param format_data_type: The format_data_type of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: OneOfFlatFileSpatialColumnDTOFormatDataType
        """

        self._format_data_type = format_data_type

    @property
    def ogr_field_type(self):
        """Gets the ogr_field_type of this FlatFileSpatialColumnDTO.  # noqa: E501


        :return: The ogr_field_type of this FlatFileSpatialColumnDTO.  # noqa: E501
        :rtype: str
        """
        return self._ogr_field_type

    @ogr_field_type.setter
    def ogr_field_type(self, ogr_field_type):
        """Sets the ogr_field_type of this FlatFileSpatialColumnDTO.


        :param ogr_field_type: The ogr_field_type of this FlatFileSpatialColumnDTO.  # noqa: E501
        :type: str
        """

        self._ogr_field_type = ogr_field_type

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
        if issubclass(FlatFileSpatialColumnDTO, dict):
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
        if not isinstance(other, FlatFileSpatialColumnDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other