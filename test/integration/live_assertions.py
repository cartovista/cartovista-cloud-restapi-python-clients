# coding: utf-8

from __future__ import absolute_import


def assert_returned(testcase, result):
    testcase.assertIsNotNone(result)
    if isinstance(result, str):
        testcase.assertTrue(result.strip())


def assert_list_returned(testcase, result):
    testcase.assertIsInstance(result, list)


def assert_bool_returned(testcase, result):
    testcase.assertIsInstance(result, bool)


def assert_model_returned(testcase, result):
    testcase.assertIsNotNone(result)
    testcase.assertTrue(
        hasattr(result, "to_dict"),
        "Expected a generated model response, got {0}".format(type(result)))
    testcase.assertIsInstance(result.to_dict(), dict)


def candidate_identifier(value):
    if value is None:
        return None

    for attr in (
            "id",
            "identifier",
            "system_identifier",
            "unique_identifier",
            "friendly_identifier",
            "map_id",
            "layer_id",
            "security_identifier",
            "security_provider_identity",
            "data_table_identifier",
            "data_column_identifier"):
        attr_value = getattr(value, attr, None)
        if attr_value:
            return attr_value

    if isinstance(value, dict):
        for key in (
                "id",
                "identifier",
                "systemIdentifier",
                "uniqueIdentifier",
                "friendlyIdentifier",
                "securityIdentifier",
                "securityProviderIdentity"):
            if value.get(key):
                return value[key]

    return None


def first_item(value):
    if value is None:
        return None
    if isinstance(value, list):
        return value[0] if value else None
    if isinstance(value, dict):
        for key in ("items", "data", "results", "value", "values"):
            item = first_item(value.get(key))
            if item is not None:
                return item
    for attr in ("items", "data", "results", "value", "values"):
        item = first_item(getattr(value, attr, None))
        if item is not None:
            return item
    return None
