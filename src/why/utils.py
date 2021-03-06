from pathlib import Path
from .explainer import Explainer


def get_root_dir():
    src_paths = [p for p in Path(__file__).parents if str(p.resolve()).endswith("src")]
    assert len(src_paths) == 1, "There must be only src directory in the directory tree"
    return src_paths[0].parent


def get_data_summary(exp: Explainer) -> str:
    n_rows = exp.train.shape[0] + exp.test.shape[0]
    n_cols = exp.train.shape[1]
    return f"There are **{n_rows}** observations and **{n_cols - 1}** features in this dataset. The target variable is **{exp.target}.**"
