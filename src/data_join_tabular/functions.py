import geopandas as gpd
import pandas as pd
import os
import logging

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s ",
    level=logging.INFO,
)


def read_file(filepath: str, sep=";"):
    """Documentation:
    inputs:
            filepath: DataFrame to save
            sep : the field separator value
    this function reads files in geojson, shp,xlsx,xsl,Xslx,csv format
    """
    print(filepath, sep)
    fileformat = filepath.split(".")[-1]
    if fileformat in ("geojson", "shp"):
        return gpd.read_file(filepath)
    if fileformat in ("xlsx", "xls", "Xlsx"):
        return pd.read_excel(filepath, sep=sep)
    if fileformat in ("csv"):
        return pd.read_csv(filepath, sep=sep)
    else:
        logging.error("this file cannot be processed....")


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
    on_right: str,
    on_left: str,
    on: str,
    how: str,
    sort: bool,
    validate: str,
    out_dir: str,
    overwrite: bool,
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
            dry_run: ,
    this function saves the Dataframe in the directory
    """
    logging.info("start reading files ...")
    df1 = read_file(file_path1, sep_file1)
    df2 = read_file(file_path2, sep_file2)
    if on is None:
        df1[on_left] = df1[on_left].astype(
            df2[on_right].dtype
        )  # they have to be of the same type
    else:
        df1[on] = df1[on].astype(df2[on].dtype)  # they have to be of the same type
    logging.info("start merging ...")
    df_out = pd.merge(
        df1,
        df2,
        how=how,
        on=on,
        left_on=on_left,
        right_on=on_right,
        sort=sort,
        suffixes=(suffix_left, suffix_right),
        validate=validate,
    )
    if output_file_name is None:
        output_file_name = os.path.basename(file_path1).split(".")[:-1][0].lower()
    output_path = os.path.join(out_dir, output_file_name + ".csv")
    if not dry_run:
        to_csv(df_out, output_path, overwrite)
