from data_join_tabular.functions import tabular_join
import data_join_tabular.__init__ as init
import logging
import click

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s ",
    level=logging.INFO,
)


def check_join_column(cols_left, cols_right):
    if type(cols_left) == list:
        assert len(cols_left) == len(
            cols_right
        ), "cols_left and cols_right must have the same length"


@click.group
def cli():
    """Represents the root cli function"""
    pass


@cli.command
def version():
    """Represents cli 'version' command"""
    click.echo(init.__version__)


@cli.command
@click.option(
    "-i1",
    "--input1",
    "input_file1",
    type=click.Path(dir_okay=False, file_okay=True, exists=True, readable=True),
    required=True,
    help="path to first file to join",
)
@click.option(
    "-i2",
    "--input2",
    "input_file2",
    type=click.Path(dir_okay=False, file_okay=True, exists=True, readable=True),
    required=True,
    help="path to second file to join",
)
@click.option(
    "-s1",
    "--sep1",
    "separator1",
    type=str,
    required=False,
    default=None,
    help="separtor for reading the first file",
)
@click.option(
    "-s2",
    "--sep2",
    "separator2",
    type=str,
    required=False,
    default=None,
    help="separtor for reading the second file",
)
@click.option(
    "-sr",
    "--sufrigh",
    "suffix_right",
    type=str,
    required=False,
    default="_right",
    help="the suffix to add to overlapping column names in right",
)
@click.option(
    "-sl",
    "--sufleft",
    "suffix_left",
    type=str,
    required=False,
    default="_left",
    help="the suffix to add to overlapping column names in left",
)
@click.option(
    "-onm",
    "--outname",
    "output_file_name",
    type=str,
    required=False,
    help="output file name, if not provioded, output name will be the same as file1",
)
@click.option(
    "-o",
    "--on",
    "on",
    multiple=True,
    required=False,
    help="Column or index level names to join on. These must be found in both DataFrames.\
        If on is None and not merging on indexes then this defaults to the intersection of the columns in both DataFrames",
)
@click.option(
    "-v",
    "--validate",
    "validate",
    type=click.Choice(["one_to_one", "one_to_many", "many_to_one", "many_to_many"]),
    required=False,
    default=None,
    help="If specified, checks if merge is of specified type.\
        “one_to_one” or “1:1”: check if merge keys are unique in both left and right datasets.\
        “one_to_many” or “1:m”: check if merge keys are unique in left dataset.\
        “many_to_one” or “m:1”: check if merge keys are unique in right dataset.\
        “many_to_many” or “m:m”: allowed, but does not result in checks.",
)
@click.option(
    "-how",
    "--how",
    "how",
    type=click.Choice(["left", "right", "outer", "inner", "cross"]),
    required=False,
    default="inner",
    help="Type of merge to be performed.\
    left: use only keys from left frame, similar to a SQL left outer join; preserve key order.\
    right: use only keys from right frame, similar to a SQL right outer join; preserve key order.\
    outer: use union of keys from both frames, similar to a SQL full outer join; sort keys lexicographically.\
    inner: use intersection of keys from both frames, similar to a SQL inner join; preserve the order of the left keys.\
    cross: creates the cartesian product from both frames, preserves the order of the left keys.",
)
@click.option(
    "-so",
    "--sort",
    "sort",
    type=str,
    required=False,
    default=None,
    help="Sort the join keys lexicographically in the result DataFrame. If False,\
        the order of the join keys depends on the join type (how keyword).",
)
@click.option(
    "-or",
    "--onrigh",
    "on_right",
    multiple=True,
    required=False,
    help="Column name to join in the right DataFrame.",
)
@click.option(
    "-ol",
    "--onleft",
    "on_left",
    multiple=True,
    required=False,
    help="Column name to join in the left DataFrame",
)
@click.option(
    "-out",
    "--output",
    "out_dir",
    type=click.Path(dir_okay=True, file_okay=False, exists=True, readable=True),
    default=".",
    show_default=True,
    help="output directory where output file will be written",
)
@click.option(
    "-f",
    "--force",
    "overwrite",
    type=bool,
    is_flag=True,
    default=False,
    help="overwrite existing file",
)
@click.option(
    "-ft",
    "--fix-types",
    "fix_types",
    type=bool,
    is_flag=True,
    default=False,
    help="fix types issues",
)
@click.option(
    "--dry-run",
    "dry_run",
    type=bool,
    is_flag=True,
    default=False,
    help="passthrough, will not write anything",
)
def join(
    input_file1: str,
    input_file2: str,
    separator1: str,
    separator2: str,
    suffix_right: str,
    suffix_left: str,
    output_file_name: str,
    on: str,
    on_right: str,
    on_left: str,
    how: str,
    sort: bool,
    validate: str,
    out_dir: str,
    overwrite: bool,
    fix_types: bool,
    dry_run: bool,
):
    """Represents cli 'join' command"""
    check_join_column(on_left, on_right)
    return tabular_join(
        input_file1,
        input_file2,
        separator1,
        separator2,
        suffix_right,
        suffix_left,
        output_file_name,
        on,
        on_right,
        on_left,
        how,
        sort,
        validate,
        out_dir,
        overwrite,
        fix_types,
        dry_run,
    )


if __name__ == "__main__":
    cli()
