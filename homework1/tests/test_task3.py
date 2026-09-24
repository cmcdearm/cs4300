import runpy

import pytest


@pytest.mark.parametrize(
    "number, expected",
    [
        (-5, "negative"),
        (0, "zero"),
        (7, "positive"),
    ],
)
def test_classify_number(number, expected):
    classify_number = runpy.run_path("homework1/src/task3.py")["classify_number"]
    assert classify_number(number) == expected


def test_first_ten_primes(capsys):
    print_primes = runpy.run_path("homework1/src/task3.py")["print_first_ten_primes"]
    print_primes()

    printed_lines = capsys.readouterr().out.splitlines()
    numbers = [int(line) for line in printed_lines]

    assert numbers == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_sum_one_to_hundred():
    sum_numbers = runpy.run_path("homework1/src/task3.py")["sum_one_to_hundred"]
    assert sum_numbers() == 5050


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, False),
        (1, False),
        (2, True),
        (9, False),
        (29, True),
    ],
)
def test_is_prime(number, expected):
    is_prime = runpy.run_path("homework1/src/task3.py")["is_prime"]
    assert is_prime(number) is expected