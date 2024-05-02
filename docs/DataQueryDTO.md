# DataQueryDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linking_ids** | **list[str]** |  | [optional] 
**linking_ids_for_stats** | **list[str]** |  | [optional] 
**sort_data_columns** | [**list[DataQueryColumnDTO]**](DataQueryColumnDTO.md) |  | [optional] 
**data_columns** | [**list[DataQueryColumnDTO]**](DataQueryColumnDTO.md) |  | [optional] 
**filter_data_columns** | [**list[DataQueryColumnDTO]**](DataQueryColumnDTO.md) |  | [optional] 
**group_by** | [**DataQueryColumnDTO**](DataQueryColumnDTO.md) |  | [optional] 
**selection_stack_parameters** | **OneOfDataQueryDTOSelectionStackParameters** |  | [optional] 
**spatial_filter** | **OneOfDataQueryDTOSpatialFilter** |  | [optional] 
**time_range** | **OneOfDataQueryDTOTimeRange** |  | [optional] 
**start_index** | **int** |  | [optional] 
**max_count** | **int** |  | [optional] 
**data_sampling_count** | **int** |  | [optional] 
**search_criteria** | **str** |  | [optional] 
**statistics** | **list[str]** |  | [optional] 
**statistics_only** | **bool** |  | [optional] 
**sort_orders** | **list[str]** |  | [optional] 
**exclude_not_available_value** | **bool** |  | [optional] 
**server_cache_enabled** | **bool** |  | [optional] 
**client_stack_trace** | **str** |  | [optional] 
**data_query_filters** | [**list[DataQueryFilterDTOOfDataQueryColumnDTO]**](DataQueryFilterDTOOfDataQueryColumnDTO.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

