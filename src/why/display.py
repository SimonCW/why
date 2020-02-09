import re
from typing import Tuple

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_predictions(y_pred: np.ndarray, p_min: float, p_max: float) -> Tuple:
    """Plot model predictions as a histogram and highlight predictions in a selected range
    
    Args:
        y_pred (np.ndarray): Array of predictions
        p_min (float): Lower boundary of predictions to highlight
        p_max (float): Upper boundary of predictions to highlight
    
    Returns:
        Tuple: Matplotlib figure and axes
    """
    fig, ax = plt.subplots()
    ax.hist(y_pred, bins=100, color="grey")
    for i, r in enumerate(ax.patches):
        if p_min <= r.get_x() <= p_max:
            ax.patches[i].set_color("#90ee90")
    ax.set_title("Model Prediction")
    ax.set_xlabel("Predicted probability of class 1")
    ax.set_ylabel("Number of predictions")
    plt.tight_layout()
    return fig, ax


def color_by_sign(val):
    sign = re.search("(\( ([\+\-])\d\.)", val).group(2)
    color = "#ee9090" if sign == "-" else "#90ee90"
    return f"border-left: 8px solid {color}"


def format_local_explanations(feat_values: pd.DataFrame) -> pd.DataFrame.style:
    cm = sns.light_palette("#90ee90", as_cmap=True)
    return feat_values.style.applymap(
        color_by_sign, subset=list(set(feat_values.columns) - set(["Prediction"]))
    ).background_gradient(
        cmap=cm, axis="index", subset=["Prediction"]
    )  # TODO: This should be red for small p1s
