from typer.testing import CliRunner

from dupe_finder import main

runner = CliRunner()


def test_hello_world() -> None:
    result = runner.invoke(main.app, "World")
    assert result.exit_code == 0
    assert result.output == "Hello World\n"
