# FlatFileSheetSpatialMetaDataDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**spatial_metadata_id** | **str** | Used when importing already existing data from another db.  Should be left blank when importing from the UI. (auto generated) | [optional] 
**geometry_type** | [**GeometryTypeEnum**](GeometryTypeEnum.md) |  | [optional] 
**target_proj4** | **str** |  | [optional] 
**target_srid** | **int** |  | [optional] 
**proj4** | **str** |  | [optional] 
**user_friendly_proj** | **str** |  | [optional] 
**reprojection_requested** | **bool** |  | [optional] 
**is_spherical_mercator** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

