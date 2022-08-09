from src.data_join_tabular import __version__
from src.data_join_tabular import main
import glob
import os.path
import os
import pytest
from click.testing import Result, CliRunner
from tests.utils import check


def test_version_displays_library_version():
    # arrange
    runner: CliRunner = CliRunner()

    # act
    result: Result = runner.invoke(main.cli, ["version"])

    # assert
    assert (
        __version__ == result.output.strip()
    ), "Version number should match library version."


def get_arguments(test_path1: str, test_path2: str) -> list[list[str]]:
    input_files1 = sorted(glob.glob(os.path.join(test_path1, "*.csv")))
    input_files2 = [glob.glob(os.path.join(test_path2, "*"))[0] for _ in input_files1]
    return [
        [
            "-i1",
            os.path.abspath(file1),
            "-i2",
            os.path.abspath(file2),
            "-or",
            "INSEE_REG",
            "-ol",
            "INSEE_REG",
            "-s1",
            ",",
            "-s2",
            ",",
            "-sl",
            "_left",
            "-sr",
            "_right",
            "-out",
            ".",
            "-f",
        ]
        for (file1, file2) in zip(input_files1, input_files2)
    ]


@pytest.mark.parametrize(
    "arguments",
    get_arguments(
        "./tests/data/inputs1",
        "./tests/data/inputs2",
    ),
)
def test_join_spatial(tmpdir_factory, arguments):

    # arrange
    runner: CliRunner = CliRunner()
    ref_folder = os.path.abspath("./tests/data/ref_outputs")
    out_folder = str(tmpdir_factory.mktemp("data"))

    # act
    with runner.isolated_filesystem(temp_dir=out_folder):
        result: Result = runner.invoke(
            cli=main.cli,
            args=["join"] + arguments,
            catch_exceptions=False,
        )
        if result.exit_code != 0:
            print(result.output)

        # assert
        assert result.exit_code == 0, "Exit code should return 0"
        check(out_folder, ref_folder)
