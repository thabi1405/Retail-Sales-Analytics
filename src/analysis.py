import pandas as pd


def category_analysis(df):
    """
    Returns sales and profit by category.
    """

    category_summary = (
        df.groupby("Category")[["Sales", "Profit"]]
        .sum()
        .sort_values(by="Profit", ascending=False)
    )

    return category_summary