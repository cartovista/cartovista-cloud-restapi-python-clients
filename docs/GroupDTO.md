# GroupDTO

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_anonymous** | **bool** |  | [optional] 
**display_name** | **str** | Group&#x27;s DisplayName is mapped to the group&#x27;s name | [optional] 
**name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_group** | **bool** |  | [optional] 
**last_modification_time** | **datetime** |  | [optional] 
**creation_time** | **datetime** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**provider** | [**SecurityProvider**](SecurityProvider.md) |  | [optional] 
**provider_name** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**secure_object_permissions** | [**list[PermissionPairDTO]**](PermissionPairDTO.md) | Permissions with a secureObject associated to it | [optional] 
**users** | [**list[UserDTO]**](UserDTO.md) |  | [optional] 
**description** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 
**user_count** | **int** | The userCount will be set when getting a list of groups,  so we don&#x27;t have to also get the list of users of each group.  If the array of users is set, return the number of elements. So setting the userCount when an array exists will do nothing. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

