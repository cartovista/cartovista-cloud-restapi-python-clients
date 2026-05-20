# coding: utf-8

from __future__ import absolute_import

import inspect
import re
import unittest

import cartovista_cloud_clients.models as models


def _model_classes():
    classes = []
    for name, cls in vars(models).items():
        if (inspect.isclass(cls) and
                getattr(cls, "__module__", "").startswith(
                    "cartovista_cloud_clients.models.")):
            classes.append((name, cls))
    return sorted(classes)


def _sample_value(type_name):
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
        return [_sample_value(list_match.group(1))]

    dict_match = re.match(r"dict\([^,]+, (.*)\)$", type_name)
    if dict_match:
        return {"sample": _sample_value(dict_match.group(1))}

    model_cls = getattr(models, type_name, None)
    if inspect.isclass(model_cls):
        return model_cls()

    return "sample"


class TestGeneratedModelContracts(unittest.TestCase):
    def test_all_models_construct_and_serialize_declared_attributes(self):
        for name, cls in _model_classes():
            with self.subTest(model=name):
                kwargs = {
                    attr: _sample_value(type_name)
                    for attr, type_name in cls.swagger_types.items()
                }

                model = cls(**kwargs)

                self.assertIsNone(model.discriminator)
                for attr, value in kwargs.items():
                    self.assertEqual(value, getattr(model, attr))
                self.assertEqual(set(cls.swagger_types), set(model.to_dict()))
                self.assertEqual(model.to_str(), repr(model))

    def test_all_models_compare_by_model_state(self):
        for name, cls in _model_classes():
            with self.subTest(model=name):
                kwargs = {
                    attr: _sample_value(type_name)
                    for attr, type_name in cls.swagger_types.items()
                }

                self.assertEqual(cls(**kwargs), cls(**kwargs))
                self.assertNotEqual(cls(**kwargs), object())

                if kwargs:
                    changed_kwargs = dict(kwargs)
                    first_attr = next(iter(changed_kwargs))
                    changed_kwargs[first_attr] = object()
                    self.assertNotEqual(cls(**kwargs), cls(**changed_kwargs))


if __name__ == "__main__":
    unittest.main()
