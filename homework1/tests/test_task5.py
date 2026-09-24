import runpy


def test_first_three_books(capsys):
    data = runpy.run_path("homework1/src/task5.py")
    printed = capsys.readouterr().out.strip()

    assert len(data["books"]) >= 4
    assert printed == str(data["books"][:3])


def test_student_ids():
    data = runpy.run_path("homework1/src/task5.py")
    students = data["students"]

    assert students["Alice"] == 1054
    assert students["Bob"] == 1432
    assert students["Charlie"] == 1573
    assert students["Dillweed"] == 1774