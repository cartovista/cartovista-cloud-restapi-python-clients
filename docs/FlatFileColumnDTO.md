# FlatFileColumnDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id that CVWP_DataColumn will be assign. | [optional] 
**ogr_field_type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_empty** | **bool** |  | [optional] 
**metadata** | **str** |  | [optional] 
**units** | **str** |  | [optional] 
**unit_placement** | [**UnitPlacement**](UnitPlacement.md) |  | [optional] 
**values** | **list[object]** |  | [optional] 
**column_number** | **int** | Represents the index of the column in the file. | [optional] 
**data_type** | [**CartoVistaPortalDataType**](CartoVistaPortalDataType.md) |  | [optional] 
**unremovable** | **bool** | If true, the user won&#x27;t be able to remove this column when uploading the file. It is normally false except when updating a DataTable or layer. Columns that already exists can&#x27;t be unchecked. | [optional] 
**precision** | **int** |  | [optional] 
**round_to_precision** | **bool** |  | [optional] 
**mappable** | **bool** |  | [optional] 
**not_availablevalues** | **bool** |  | [optional] 
**value_to_convert** | **float** |  | [optional] 
**aggregation_type** | [**AggregationType**](AggregationType.md) |  | [optional] 
**format_data_type** | **OneOfFlatFileColumnDTOFormatDataType** | The datatype defined by the user in the file.  If it has a value, the user has defined one.  Currently only excel files can have a Format set by the user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

