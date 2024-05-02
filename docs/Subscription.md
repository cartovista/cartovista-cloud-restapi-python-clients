# Subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | [optional] 
**is_managed** | **bool** |  | [optional] 
**is_license** | **bool** |  | [optional] 
**package** | [**SubscriptionPackage**](SubscriptionPackage.md) |  | [optional] 
**billing_cycle_end** | **datetime** |  | [optional] 
**max_users** | **int** |  | [optional] 
**geocoding_remaining** | **int** |  | [optional] 
**industry** | **OneOfSubscriptionIndustry** |  | [optional] 
**has_expired** | **bool** |  | [optional] 
**grace_period_end** | **datetime** |  | [optional] 
**is_monthly** | **bool** |  | [optional] 
**max_geocoding_transaction** | **int** |  | [optional] 
**current_geocoding_transaction** | **int** |  | [optional] 
**active_users** | **int** |  | [optional] 
**data_usage_gb** | **float** |  | [optional] 
**data_usage_limit_gb** | **float** |  | [optional] 
**max_maps** | **int** |  | [optional] 
**layers_per_map** | **int** |  | [optional] 
**features_per_layer** | **int** |  | [optional] 
**has_invoices** | **bool** |  | [optional] 
**scheduled_changes** | [**ScheduledSubscriptionChanges**](ScheduledSubscriptionChanges.md) |  | [optional] 
**payment_failed** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

