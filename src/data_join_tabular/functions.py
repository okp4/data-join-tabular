import geopandas as gpd
import pandas as pd
import os
from typing import Optional
import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s ",
    level=logging.INFO,
)


def read_file(filepath: str, sep: str):
    """Documentation:
    inputs:
            filepath: DataFrame to save
            sep : the field separator value
    this function reads files in geojson, shp,xlsx,xsl,Xslx,csv format
    """
    sep = "," if sep is None else sep
    fileformat = filepath.split(".")[-1]
    if fileformat in ("geojson", "shp"):
        return gpd.read_file(filepath)
    if fileformat in ("csv"):
        return pd.read_csv(filepath, sep=sep)
    else:
        logging.error("this file cannot be processed....")

def check_types(on, on_left, on_right, df_right, df_left):
    """Documentation:
    inputs:
            on: Names of columns or indexes to join (common to both dataframes)
            on_left: Names of columns or indexes to join in the first dataframe
            on_right: Names of columns or indexes to join in the second dataframe
            df_right: First dataframe to be merged
            df_left: Second dataframe to be merged
    this function checks the column types to be merged are the same.
    """
    if on != ():
        for col in on:
            assert "the columns to be merged must have the same type", (
                df_right[col].dtype == df_left[col].dtype
            )
    else:
        for (col_right, col_left) in zip(on_right, on_left):
            assert "the columns to be merged must have the same type", (
                df_right[col_right].dtype == df_left[col_left].dtype
            )


def fix_type(on, on_left, on_right, df_right, df_left):
    """Documentation:
    inputs:
            on: Names of columns or indexes to join (common to both dataframes)
            on_left: Names of columns or indexes to join in the first dataframe
            on_right: Names of columns or indexes to join in the second dataframe
            df_right: First dataframe to be merged
            df_left: Second dataframe to be merged
    This function converts the column types to ensure that the column types to be merged are the same.
    """
    if on != ():
        for col in on:
            df_right[col] = df_right[col].astype(
                df_left[col].dtype
            )  # they have to be of the same type
    else:
        for (col_right, col_left) in zip(on_right, on_left):
            df_right[col_right] = df_right[col_right].astype(df_left[col_left].dtype)
    return df_left, df_right

def columns_to_be_merged(on, on_left, on_right):
    on = None if on == () else on
    on_left = None if on_left == () else on_left
    on_right = None if on_right == () else on_right
    return on, on_left, on_right




def to_csv(df: pd.DataFrame, output_path: str, overwrite: bool):
    """Documentation:
    inputs:
            df: DataFrame to save
            output_path : path of the directory where the dataframe will be saved
            overwrite : 'true' to overwrite the existing csv files
    this function saves the Dataframe in the directory
    """
    file_name: str = os.path.basename(output_path)
    if overwrite or not os.path.exists(output_path):
        logging.info(f"the csv with name {file_name} was saved succefully")
        df.to_csv(output_path, index=False)
    else:
        logging.error(f"the csv with name {file_name} is duplicated")
        raise ValueError(f"{file_name} already exists")


def tabular_join(
    file_path1: str,
    file_path2: str,
    sep_file1: str,
    sep_file2: str,
    suffix_right: str,
    suffix_left: str,
    output_file_name: str,
    on: Optional[str],
    on_right: Optional[str],
    on_left: Optional[str],
    how: str,
    sort: bool,
    validate: str,
    out_dir: str,
    overwrite: bool,
    fix_types: bool,
    dry_run: bool,
):
    """Documentation:
    inputs:
            file_path1: first file path,
            file_path2: second file path,
            sep_file1: the field separator value for first file,
            sep_file2: the field separator value for second file,
            suffix_right: suffix  for second file,
            suffix_left: suffix to first file ,
            output_file_name: the name of the output file ,
            on_right: str,
            on_left: str,
            on : str,
            how:str,
            sort:bool,
            validate:str,
            out_dir: output directory,
            overwrite : 'true' to overwrite the existing csv files,
            fix_types: fix types issues
            dry_run: ,
    this function saves the Dataframe in the directory
    """
    logging.info("start reading files ...")
    df1 = read_file(file_path1, sep_file1)
    df2 = read_file(file_path2, sep_file2)
    check_types(on, on_left, on_right, df2, df1)
    if fix_types:
        df1, df2 = fix_type(on, on_left, on_right, df1, df2)
    logging.info("start joining ...")
    on, on_left, on_right = columns_to_be_merged(on, on_left, on_right)
    df_out = pd.merge(
        df1,
        df2,
        how=how,
        on=on,
        left_on=on_left,
        right_on=on_right,
        suffixes=(suffix_left, suffix_right),
        sort=sort,
        validate=validate,
    )
    if output_file_name is None:
        output_file_name = os.path.basename(file_path1).split(".")[:-1][0].lower()
    output_path = os.path.join(out_dir, output_file_name + ".csv")
    logging.info("process files")
    if not dry_run:
        to_csv(df_out, output_path, overwrite)
