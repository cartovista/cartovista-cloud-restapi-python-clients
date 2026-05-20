# coding: utf-8

from __future__ import absolute_import

import inspect
import re

import cartovista_cloud_clients.models as models


def sample_value(type_name, seen=None):
    seen = seen or set()
    if type_name == "str":
        return "sample"
    if type_name in ("int", "long"):
        return 123
    if type_name == "float":
        return 12.5
    if type_name == "bool":
        return True
    if type_name == "object":
        return {"key": "value"}
    if type_name == "date":
        return "2026-05-15"
    if type_name == "datetime":
        return "2026-05-15T10:30:00Z"

    list_match = re.match(r"list\[(.*)\]$", type_name)
    if list_match:
        return [sample_value(list_match.group(1), seen)]

    dict_match = re.match(r"dict\([^,]+, (.*)\)$", type_name)
    if dict_match:
        return {"sample": sample_value(dict_match.group(1), seen)}

    model_class = getattr(models, type_name, None)
    if inspect.isclass(model_class):
        if model_class in seen:
            return None
        return build_model_instance(model_class, seen)

    return "sample"


def build_model_instance(model_class, seen=None):
    seen = set(seen or set())
    seen.add(model_class)
    kwargs = {
        attr: sample_value(type_name, seen)
        for attr, type_name in model_class.swagger_types.items()
    }
    return model_class(**kwargs)
