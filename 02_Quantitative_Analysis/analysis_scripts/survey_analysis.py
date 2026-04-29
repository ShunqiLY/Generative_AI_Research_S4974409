"""
Survey Analysis Script
Study: Using Generative AI Tools - Boon or Bane
"""

import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = "../survey_data/survey_data_raw.csv"

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def summarise_likert(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    return df[columns].describe()

def plot_frequency_distribution(df: pd.DataFrame, column: str, title: str) -> None:
    counts = df[column].value_counts()
    counts.plot(kind="bar", title=title)
    plt.tight_layout()
    plt.savefig(f"../reports/{column}_distribution.png")
    plt.close()

if __name__ == "__main__":
    df = load_data(DATA_PATH)
    likert_cols = ["q5_productivity", "q6_ethics", "q7_trust", "q8_integrity"]
    print(summarise_likert(df, likert_cols))
    plot_frequency_distribution(df, "genai_frequency", "GenAI Usage Frequency")
