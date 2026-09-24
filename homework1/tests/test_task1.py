import runpy


def test_hello_world(capsys):
    runpy.run_path("homework1/src/task1.py")
    output = capsys.readouterr().out
    assert output == "Hello, World!\n"