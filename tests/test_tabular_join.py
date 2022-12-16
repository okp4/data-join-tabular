from data_join_tabular import __version__
from data_join_tabular import main
import glob
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
    input_files1 = sorted(glob.glob(os.path.join(test_path1, "*")))
    input_files2 = sorted(glob.glob(os.path.join(test_path2, "*.csv")))
    return [
        [
            "-i1",
            os.path.abspath(input_files1[0]),
            "-i2",
            os.path.abspath(input_files2[0]),
            "-o",
            "categorie",
            "-o",
            "statut",
            "-o",
            "effectif",
            "-o",
            "genre",
            "-s1",
            ";",
            "-s2",
            ";",
            "-out",
            ".",
            "-f",
        ],
        [
            "-i1",
            os.path.abspath(input_files1[1]),
            "-i2",
            os.path.abspath(os.path.join(test_path2, "Départements/DEPARTEMENT.shp")),
            "-ol",
            "code",
            "-or",
            "INSEE_REG",
            "-out",
            ".",
            "-f",
        ],
    ]


@pytest.mark.parametrize(
    "arguments",
    get_arguments(
        "./tests/data/inputs1",
        "./tests/data/inputs2",
    ),
)
def test_join_tabular(tmpdir_factory, arguments):

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
