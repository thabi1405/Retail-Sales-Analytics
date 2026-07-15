import pandas as pd

def load_and_clean_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Convert dates
    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    # Create new columns
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["Month Name"] = df["Order Date"].dt.month_name()
    df["Shipping Days"] = (
        df["Ship Date"] - df["Order Date"]
    ).dt.days

    return df