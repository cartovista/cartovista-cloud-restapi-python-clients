# coding: utf-8

from __future__ import absolute_import

import os
import unittest

from cartovista_cloud_clients.models.create_folder import CreateFolder
from cartovista_cloud_clients.models.create_group_parameter import (
    CreateGroupParameter,
)
from cartovista_cloud_clients.models.get_data_elements_param import (
    GetDataElementsParam,
)
from cartovista_cloud_clients.models.get_folders_parameters import (
    GetFoldersParameters,
)
from cartovista_cloud_clients.models.search_data_elements_parameter import (
    SearchDataElementsParameter,
)
from cartovista_cloud_clients.models.update_folder import UpdateFolder
from cartovista_cloud_clients.models.update_group_parameter import (
    UpdateGroupParameter,
)

from integration.live_assertions import (
    assert_bool_returned,
    assert_list_returned,
    assert_model_returned,
    assert_returned,
    candidate_identifier,
)


class EndpointCase(object):
    def __init__(self, name, api_class, method_name, args_factory,
                 assertion=assert_returned, skip_reason=None):
        self.name = name
        self.api_class = api_class
        self.method_name = method_name
        self.args_factory = args_factory
        self.assertion = assertion
        self.skip_reason = skip_reason

    def invoke(self, context):
        args, kwargs = self.args_factory(context)
        return context.call(
            self.api_class,
            self.method_name,
            *args,
            **kwargs
        )


def no_args(_context):
    return (), {}


def tenant_args(context):
    return (context.tenant,), {}


def login_args(context):
    return (context.login_body(),), {}


def get_data_elements_args(context):
    return (GetDataElementsParam(), context.tenant), {}


def search_data_elements_args(context):
    return (SearchDataElementsParameter(search=""), context.tenant), {}


def get_folders_args(context):
    return (GetFoldersParameters(), context.tenant), {}


def first_map_id(context):
    return context.first_identifier_from(
        "maps",
        lambda: context.call("MapApi", "map_get_maps", context.tenant),
        "map",
    )


def first_layer_id(context):
    return context.first_identifier_from(
        "layers",
        lambda: context.call("LayerApi", "layer_get_layers", context.tenant),
        "layer",
    )


def first_data_table_id(context):
    return context.first_identifier_from(
        "data_tables",
        lambda: context.call(
            "DataTableApi", "data_table_get_data_tables", context.tenant),
        "data table",
    )


def first_grid_layer_id(context):
    return context.first_identifier_from(
        "grid_layers",
        lambda: context.call(
            "GridLayerApi", "grid_layer_get_grid_layers", context.tenant),
        "grid layer",
    )


def first_content_folder_id(context):
    data_elements = context.cached(
        "data_elements_for_folder_parent",
        lambda: context.call(
            "DataApi", "data_get_data_elements",
            GetDataElementsParam(), context.tenant),
    )
    folder_id = getattr(data_elements, "folder_id", None)
    if not folder_id and hasattr(data_elements, "to_dict"):
        folder_id = data_elements.to_dict().get("folder_id")
    if not folder_id:
        raise unittest.SkipTest(
            "No content parent folder id found for folder mutation tests")
    return folder_id


def current_user_identifier(context):
    user = context.cached(
        "current_user",
        lambda: context.call("UserApi", "user_get_current_user",
                             context.tenant),
    )
    identifier = candidate_identifier(user) or getattr(user, "user_name", None)
    if not identifier:
        raise unittest.SkipTest(
            "No current user identifier found for group mutation tests")
    return identifier


def map_id_args(context):
    return (first_map_id(context), context.tenant), {}


def layer_id_args(context):
    return (first_layer_id(context), context.tenant), {}


def data_table_id_args(context):
    return (first_data_table_id(context), context.tenant), {}


def grid_layer_id_args(context):
    return (first_grid_layer_id(context), context.tenant), {}


LIVE_ENDPOINT_CASES = [
    EndpointCase(
        "auth.login",
        "AuthenticationApi",
        "authentication_global_login",
        login_args,
    ),
    EndpointCase(
        "config.get_configuration",
        "ConfigApi",
        "config_get_configuration",
        no_args,
        assert_model_returned,
    ),
    EndpointCase(
        "portal.subscription_and_user",
        "PortalApi",
        "portal_get_subscription_and_user",
        tenant_args,
        assert_model_returned,
    ),
    EndpointCase(
        "organization.get_organization",
        "OrganizationApi",
        "organization_get_organization",
        no_args,
        assert_model_returned,
    ),
    EndpointCase(
        "user.current_user",
        "UserApi",
        "user_get_current_user",
        tenant_args,
        assert_model_returned,
    ),
    EndpointCase(
        "user.get_users",
        "UserApi",
        "user_get_users",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "group.get_groups",
        "GroupApi",
        "group_get_groups",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "folder.get_folders",
        "FolderApi",
        "folder_get_folders",
        get_folders_args,
        assert_list_returned,
    ),
    EndpointCase(
        "folder.get_folders_with_path",
        "FolderApi",
        "folder_get_folders_with_path",
        get_folders_args,
        assert_returned,
    ),
    EndpointCase(
        "data.get_data_elements",
        "DataApi",
        "data_get_data_elements",
        get_data_elements_args,
        assert_returned,
    ),
    EndpointCase(
        "data.search_all_data_elements",
        "DataApi",
        "data_search_all_data_elements",
        search_data_elements_args,
        assert_returned,
    ),
    EndpointCase(
        "data_table.get_data_tables",
        "DataTableApi",
        "data_table_get_data_tables",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "layer.get_layers",
        "LayerApi",
        "layer_get_layers",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "grid_layer.get_grid_layers",
        "GridLayerApi",
        "grid_layer_get_grid_layers",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "map.get_maps",
        "MapApi",
        "map_get_maps",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "map.get_keywords",
        "MapApi",
        "map_get_keywords",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "symbol.get_symbols",
        "SymbolApi",
        "symbol_get_symbols",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "permission.get_security_identities",
        "PermissionApi",
        "permission_get_security_identities",
        tenant_args,
        assert_returned,
    ),
    EndpointCase(
        "subscription.get_content_count",
        "SubscriptionApi",
        "subscription_get_content_count",
        tenant_args,
        assert_model_returned,
    ),
    EndpointCase(
        "subscription.get_plans",
        "SubscriptionApi",
        "subscription_get_plans",
        tenant_args,
        assert_returned,
        "cypresstest returns a server Null not allowed error for plans",
    ),
    EndpointCase(
        "sign_up.get_all_demo_maps",
        "SignUpApi",
        "sign_up_get_all_demo_maps",
        no_args,
        assert_list_returned,
    ),
    EndpointCase(
        "wms.get_wms_layers",
        "WmsApi",
        "wms_get_wms_layers",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "wmts.get_wmts_layers",
        "WmtsApi",
        "wmts_get_wmts_layers",
        tenant_args,
        assert_list_returned,
    ),
    EndpointCase(
        "map.get_map",
        "MapApi",
        "map_get_map",
        map_id_args,
        assert_model_returned,
    ),
    EndpointCase(
        "map.get_layers_by_map",
        "MapApi",
        "map_get_layers_by_map",
        map_id_args,
        assert_list_returned,
    ),
    EndpointCase(
        "map.get_data_tables_by_map",
        "MapApi",
        "map_get_data_tables_by_map",
        map_id_args,
        assert_list_returned,
    ),
    EndpointCase(
        "map.get_grid_layers_by_map",
        "MapApi",
        "map_get_grid_layers_by_map",
        map_id_args,
        assert_list_returned,
    ),
    EndpointCase(
        "layer.get_layer_by_id",
        "LayerApi",
        "layer_get_layer_by_id",
        layer_id_args,
        assert_model_returned,
    ),
    EndpointCase(
        "layer.get_layer_details",
        "LayerApi",
        "layer_get_layer_details",
        layer_id_args,
        assert_model_returned,
    ),
    EndpointCase(
        "data_column.get_layer_data_columns",
        "DataColumnApi",
        "data_column_get_layer_data_columns",
        layer_id_args,
        assert_list_returned,
    ),
    EndpointCase(
        "permission.get_layer_permissions",
        "PermissionApi",
        "permission_get_layer_permissions",
        layer_id_args,
        assert_list_returned,
    ),
    EndpointCase(
        "data_table.get_data_table_by_identifier",
        "DataTableApi",
        "data_table_get_data_table_by_identifier",
        data_table_id_args,
        assert_model_returned,
    ),
    EndpointCase(
        "data_table.get_data_table_details",
        "DataTableApi",
        "data_table_get_data_table_details",
        data_table_id_args,
        assert_model_returned,
    ),
    EndpointCase(
        "grid_layer.get_grid_layer_by_id",
        "GridLayerApi",
        "grid_layer_get_grid_layer_by_id",
        grid_layer_id_args,
        assert_model_returned,
    ),
    EndpointCase(
        "grid_layer.get_grid_layer_details",
        "GridLayerApi",
        "grid_layer_get_grid_layer_details",
        grid_layer_id_args,
        assert_model_returned,
    ),
]


def create_folder(context):
    name = context.unique_name("folder")
    folder = context.call(
        "FolderApi",
        "folder_create_folder",
        CreateFolder(name=name, parent_id=first_content_folder_id(context)),
        context.tenant,
    )
    folder_id = candidate_identifier(folder)
    if not folder_id:
        raise AssertionError("Created folder response did not include an id")
    context.register_cleanup(
        lambda: context.call(
            "FolderApi",
            "folder_delete_folder",
            folder_id,
            context.tenant,
        )
    )
    return folder, folder_id


def update_folder(context, folder_id):
    updated_name = context.unique_name("folder-updated")
    return context.call(
        "FolderApi",
        "folder_update_folder",
        UpdateFolder(
            name=updated_name,
            parent_id=first_content_folder_id(context),
            hide_from_anonymous=False,
        ),
        folder_id,
        context.tenant,
    )


def create_group(context):
    identifier = "pyapi-{0}-group".format(context.config.run_id[:12]).lower()
    group = context.call(
        "GroupApi",
        "group_create_group",
        CreateGroupParameter(
            identifier=identifier,
            name=identifier,
            description="Created by Python API live tests",
            user_ids=[current_user_identifier(context)],
        ),
        context.tenant,
    )
    group_id = candidate_identifier(group) or identifier
    context.register_cleanup(
        lambda: context.call(
            "GroupApi",
            "group_delete_group",
            group_id,
            context.tenant,
        )
    )
    return group, group_id


def update_group(context, group_id):
    existing_group = context.call(
        "GroupApi",
        "group_get_group",
        group_id,
        context.tenant,
    )
    return context.call(
        "GroupApi",
        "group_update_group",
        UpdateGroupParameter(
            name="pyapi-{0}-updated".format(context.config.run_id[:12]),
            description="Updated by Python API live tests",
            permissions=getattr(existing_group, "permissions", None) or [],
            users=[current_user_identifier(context)],
        ),
        group_id,
        context.tenant,
    )


def create_data_table_from_excel(context, sheet_name=None):
    if not context.config.excel_file:
        raise unittest.SkipTest(
            "No Excel fixture configured for data table import tests")
    if not os.path.exists(context.config.excel_file):
        raise unittest.SkipTest(
            "Excel fixture does not exist: {0}".format(
                context.config.excel_file))

    if sheet_name is None:
        data_table = context.call(
            "DataTableApi",
            "data_table_create_from_excel",
            context.tenant,
            file=context.config.excel_file,
        )
    else:
        data_table = context.call(
            "DataTableApi",
            "data_table_create_from_excel2",
            sheet_name,
            context.tenant,
            file=context.config.excel_file,
        )

    data_table_id = candidate_identifier(data_table)
    if not data_table_id:
        raise AssertionError(
            "Created data table response did not include an identifier")
    context.register_cleanup(
        lambda: context.call(
            "DataTableApi",
            "data_table_delete_data_table",
            data_table_id,
            context.tenant,
        )
    )
    return data_table, data_table_id


def upload_fixture(context):
    if not context.config.upload_file:
        raise unittest.SkipTest(
            "No upload fixture configured for upload endpoint test")
    if not os.path.exists(context.config.upload_file):
        raise unittest.SkipTest(
            "Upload fixture does not exist: {0}".format(
                context.config.upload_file))
    result = context.call(
        "PortalApi",
        "portal_upload",
        context.tenant,
        file=context.config.upload_file,
    )
    if result:
        context.register_cleanup(
            lambda: context.call(
                "PortalApi",
                "portal_cancel_upload",
                result,
                context.tenant,
            )
        )
    return result
