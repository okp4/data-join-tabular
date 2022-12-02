import os
import pandas as pd


def check(result_path: str, ref_path: str):
    assert os.path.isdir(ref_path), " referenced direcorty do not exists"
    path: str = os.path.join(result_path, os.listdir(result_path)[0])
    csv_outs: str = os.path.join(path, os.listdir(path)[0])
    name = os.path.basename(csv_outs)
    csv_ref = os.path.join(ref_path, name)
    assert os.path.isfile(
        csv_ref
    ), f"referenced csv file with name {name} do not exists"
    df_ref: pd.DataFrame = pd.read_csv(csv_ref, low_memory=False)
    df_ref = df_ref.sort_values(by=[df_ref.columns[0]])
    df_out: pd.DataFrame = pd.read_csv(csv_outs, low_memory=False)
    df_out = df_out.sort_values(by=[df_ref.columns[0]])
    assert df_ref.equals(
        df_out
    ), f"csv {name} should be the same than the reference csv"
