# FlatFileSheetDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id that CVWP_DataTable will be assign. If we are updating a DataTable or SpatialMetadata that already exists, this will be assigned to it. For GridLayers, this is the GridLayerId | [optional] 
**table_ref** | **str** |  | [optional] 
**sheet_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**columns** | [**list[FlatFileColumnDTO]**](FlatFileColumnDTO.md) |  | [optional] 
**record_count** | **int** |  | [optional] 
**lat_column_number** | **int** |  | [optional] 
**long_column_number** | **int** |  | [optional] 
**address_column_numbers** | **list[int]** |  | [optional] 
**can_geocode_by_lat_long** | **bool** |  | [optional] 
**spatial_meta_data** | **OneOfFlatFileSheetDTOSpatialMetaData** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

