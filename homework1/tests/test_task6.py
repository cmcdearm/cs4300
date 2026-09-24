import pytest
import runpy
from pathlib import Path


def test_assignment_file_word_count():
    count_words = runpy.run_path("homework1/src/task6.py")["count_words"]
    file_path = Path("homework1/task6_read_me.txt")

    assert count_words(file_path) == 104


@pytest.mark.parametrize(
    "contents, expected",
    [
        ("", 0),
        ("one two three", 3),
        ("Hello, world!\nNext line.", 4),
        ("word , another .", 2),
    ],
)
def test_word_count_samples(tmp_path, contents, expected):
    sample_file = tmp_path / "sample.txt"
    sample_file.write_text(contents, encoding="utf-8")

    count_words = runpy.run_path("homework1/src/task6.py")["count_words"]
    assert count_words(sample_file) == expected