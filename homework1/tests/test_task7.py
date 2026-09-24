import runpy

import pytest


@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([10, 20, 30], 20),
        ([2, 4], 3),
        ([1, 2, 3, 4], 2.5),
    ],
)
def test_average(numbers, expected):
    average = runpy.run_path("homework1/src/task7.py")["average"]
    assert average(numbers) == pytest.approx(expected)