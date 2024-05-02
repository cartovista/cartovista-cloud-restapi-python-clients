# TerritoryManagerSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_zones** | **int** |  | [optional] 
**area_type** | [**TerritoryAreaByEnum**](TerritoryAreaByEnum.md) |  | [optional] 
**transportation_type** | [**TerritoryTransportTypeEnum**](TerritoryTransportTypeEnum.md) |  | [optional] 
**consider_traffic** | **bool** |  | [optional] 
**selection_color** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**maximum_nearest_for_distance_analysis** | **int** |  | [optional] 
**maximum_distance_meters** | **int** |  | [optional] 
**maximum_time_seconds** | **int** |  | [optional] 
**use_urbanicity** | **bool** |  | [optional] 
**urbanicity_column_id** | **str** |  | [optional] 
**urbanicity_column** | [**UrbanicityDataColumn**](UrbanicityDataColumn.md) |  | [optional] 
**urbanicity_values** | [**list[TerritoryManagerUrbanicity]**](TerritoryManagerUrbanicity.md) |  | [optional] 
**spatial_selection_type** | [**TerritoryScenarioSpatialSelectionTypeEnum**](TerritoryScenarioSpatialSelectionTypeEnum.md) |  | [optional] 
**zones** | [**list[TerritoryManagementZone]**](TerritoryManagementZone.md) |  | [optional] 
**default_pta_zone_id** | **int** |  | [optional] 
**default_exclusivity_zone_id** | **int** |  | [optional] 
**default_establishment_exclusivity** | **bool** |  | [optional] 
**default_free_mode** | **bool** |  | [optional] 
**default_official_pta_zone_id** | **int** |  | [optional] 
**default_official_exclusivity_zone_id** | **int** |  | [optional] 
**default_official_establishment_exclusivity** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

