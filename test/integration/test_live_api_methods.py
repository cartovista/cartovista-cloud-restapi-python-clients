# coding: utf-8

from __future__ import absolute_import

import unittest

from cartovista_cloud_clients.rest import ApiException

from integration.endpoint_metadata import (
    LIVE_ENDPOINT_CASES,
    create_data_table_from_excel,
    create_folder,
    create_group,
    update_folder,
    update_group,
    upload_fixture,
)
from integration.live_assertions import (
    assert_model_returned,
    assert_returned,
    candidate_identifier,
)
from integration.live_config import LiveConfig, require_live_config
from integration.live_context import LiveApiContext


class TestLiveApiMethods(unittest.TestCase):
    """Live integration tests for generated API methods.

    These tests are skipped unless CARTOVISTA_HOST, CARTOVISTA_TENANT,
    CARTOVISTA_API_ADMIN_EMAIL, and CARTOVISTA_API_TEST_PASSWORD are set.
    """

    @classmethod
    def setUpClass(cls):
        config, skip_reason = LiveConfig.from_environment()
        if skip_reason:
            if require_live_config():
                raise AssertionError(skip_reason)
            raise unittest.SkipTest(skip_reason)
        cls.context = LiveApiContext(config)
        cls.context.authenticate()

    @classmethod
    def tearDownClass(cls):
        context = getattr(cls, "context", None)
        if context is not None:
            context.cleanup_all()

    def test_generated_api_methods_return_expected_responses(self):
        for endpoint in LIVE_ENDPOINT_CASES:
            with self.subTest(endpoint=endpoint.name):
                if endpoint.skip_reason:
                    self.skipTest(endpoint.skip_reason)
                result = endpoint.invoke(self.context)
                endpoint.assertion(self, result)

    def test_folder_create_read_update_delete_roundtrip(self):
        if not self.context.config.allow_mutation:
            self.skipTest("Live API mutation tests are disabled")

        folder, folder_id = create_folder(self.context)
        assert_model_returned(self, folder)

        fetched = self.context.call(
            "FolderApi",
            "folder_get_folder",
            folder_id,
            self.context.tenant,
        )
        assert_model_returned(self, fetched)

        updated = update_folder(self.context, folder_id)
        assert_model_returned(self, updated)

        self.context.call(
            "FolderApi",
            "folder_delete_folder",
            folder_id,
            self.context.tenant,
        )
        self.context._cleanups.pop()

        with self.assertRaises(ApiException):
            self.context.call(
                "FolderApi",
                "folder_get_folder",
                folder_id,
                self.context.tenant,
            )

    def test_group_create_read_update_delete_roundtrip(self):
        if not self.context.config.allow_mutation:
            self.skipTest("Live API mutation tests are disabled")

        group, group_id = create_group(self.context)
        assert_model_returned(self, group)

        fetched = self.context.call(
            "GroupApi",
            "group_get_group",
            group_id,
            self.context.tenant,
        )
        assert_model_returned(self, fetched)

        updated = update_group(self.context, group_id)
        assert_model_returned(self, updated)

        self.context.call(
            "GroupApi",
            "group_delete_group",
            group_id,
            self.context.tenant,
        )
        self.context._cleanups.pop()

        with self.assertRaises(ApiException):
            self.context.call(
                "GroupApi",
                "group_get_group",
                group_id,
                self.context.tenant,
            )

    def test_data_table_create_from_excel_roundtrip(self):
        if not self.context.config.allow_mutation:
            self.skipTest("Live API mutation tests are disabled")

        table, table_id = create_data_table_from_excel(self.context)
        assert_model_returned(self, table)

        fetched = self.context.call(
            "DataTableApi",
            "data_table_get_data_table_by_identifier",
            table_id,
            self.context.tenant,
        )
        assert_model_returned(self, fetched)

        self.context.call(
            "DataTableApi",
            "data_table_delete_data_table",
            table_id,
            self.context.tenant,
        )
        self.context._cleanups.pop()

        with self.assertRaises(ApiException):
            self.context.call(
                "DataTableApi",
                "data_table_get_data_table_by_identifier",
                table_id,
                self.context.tenant,
            )

    def test_data_table_create_from_excel_sheet_roundtrip(self):
        if not self.context.config.allow_mutation:
            self.skipTest("Live API mutation tests are disabled")

        table, table_id = create_data_table_from_excel(
            self.context,
            self.context.config.excel_sheet_name,
        )
        assert_model_returned(self, table)

        fetched = self.context.call(
            "DataTableApi",
            "data_table_get_data_table_by_identifier",
            table_id,
            self.context.tenant,
        )
        assert_model_returned(self, fetched)

        self.context.call(
            "DataTableApi",
            "data_table_delete_data_table",
            table_id,
            self.context.tenant,
        )
        self.context._cleanups.pop()

        with self.assertRaises(ApiException):
            self.context.call(
                "DataTableApi",
                "data_table_get_data_table_by_identifier",
                table_id,
                self.context.tenant,
            )

    def test_upload_endpoint_with_fixture(self):
        if not self.context.config.allow_mutation:
            self.skipTest("Live API mutation tests are disabled")

        result = upload_fixture(self.context)
        assert_returned(self, result)
        self.assertTrue(candidate_identifier({"id": result}) or result)


if __name__ == "__main__":
    unittest.main()
