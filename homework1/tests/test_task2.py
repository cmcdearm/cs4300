import runpy

import pytest


@pytest.mark.parametrize(
    "name, expected_value, expected_type",
    [
        ("count", 12, int),
        ("pi", 3.14, float),
        ("greeting", "Hello, World!", str),
        ("is_valid", True, bool),
    ],
)
def test_variable(name, expected_value, expected_type):
    variables = runpy.run_path("homework1/src/task2.py")
    actual = variables[name]
    assert actual == expected_value
    assert type(actual) is expected_type