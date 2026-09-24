import runpy

import pytest


@pytest.mark.parametrize(
    "price, discount, expected",
    [
        (100, 20, 80),
        (19.99, 10, 17.991),
        (50, 0, 50),
        (50, 100, 0),
    ],
)
def test_calculate_discount(price, discount, expected):
    calculate_discount = runpy.run_path("homework1/src/task4.py")["calculate_discount"]
    assert calculate_discount(price, discount) == pytest.approx(expected)

@pytest.mark.parametrize(
    "price, discount",
    [
        (-1, 20),
        (50, -1),
        (50, 101),
    ],
)
def test_rejects_invalid_values(price, discount):
    calculate_discount = runpy.run_path("homework1/src/task4.py")["calculate_discount"]

    with pytest.raises(ValueError):
        calculate_discount(price, discount)