import argparse
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="muted")

DATASET_CANDIDATES = [
    "fatal-police-shootings-data.csv",
    "police_killings.csv",
    "police-shootings.csv",
    "police_shootings.csv",
    "shootings.csv"
]
CENSUS_CANDIDATES = [
    "us_census_data.csv",
    "census_by_state.csv",
    "state_census.csv",
    "census.csv",
    "usa_census.csv"
]


def find_dataset_file(folder: Path, names):
    for name in names:
        candidate = folder / name
        if candidate.exists():
            return candidate
    return None


def parse_percentage(value):
    if pd.isna(value):
        return np.nan
    text = str(value).strip()
    text = text.replace("%", "").replace(",", "")
    try:
        return float(text)
    except ValueError:
        return np.nan


def parse_currency(value):
    if pd.isna(value):
        return np.nan
    text = str(value).strip().replace("$", "").replace(",", "")
    try:
        return float(text)
    except ValueError:
        return np.nan


def load_police_shootings(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]

    rename_map = {
        "State": "state",
        "state": "state",
        "race": "race",
        "Race": "race",
        "date": "date",
        "Date": "date",
        "caused_by_officer": "caused_by_officer",
        "name": "name",
        "manner_of_death": "manner_of_death",
        "armed": "armed",
        "age": "age",
        "gender": "gender",
        "city": "city",
        "county_name": "county",
        "latitude": "latitude",
        "longitude": "longitude",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    if "state" not in df.columns and "State" in df.columns:
        df["state"] = df["State"]

    if "race" in df.columns:
        df["race"] = df["race"].fillna("Unknown").astype(str).str.upper()
    else:
        df["race"] = "UNKNOWN"

    if "age" in df.columns:
        df["age"] = pd.to_numeric(df["age"], errors="coerce")

    df["state"] = df["state"].astype(str).str.upper().str.strip()
    return df


def load_census(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]

    rename_map = {
        "State": "state",
        "state": "state",
        "State Name": "state",
        "State_Name": "state",
        "poverty_rate": "poverty_rate",
        "poverty": "poverty_rate",
        "Poverty Rate": "poverty_rate",
        "high_school_grad_rate": "high_school_grad_rate",
        "high_school_grad": "high_school_grad_rate",
        "high_school_graduation_rate": "high_school_grad_rate",
        "HS Grad Rate": "high_school_grad_rate",
        "median_household_income": "median_household_income",
        "median_income": "median_household_income",
        "Median Income": "median_household_income",
        "population": "population",
        "Population": "population",
        "white_pct": "white_pct",
        "black_pct": "black_pct",
        "hispanic_pct": "hispanic_pct",
        "asian_pct": "asian_pct",
        "percent_white": "white_pct",
        "percent_black": "black_pct",
        "percent_hispanic": "hispanic_pct",
        "percent_asian": "asian_pct",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    if "state" in df.columns:
        df["state"] = df["state"].astype(str).str.upper().str.strip()

    for col in ["poverty_rate", "high_school_grad_rate"]:
        if col in df.columns:
            df[col] = df[col].apply(parse_percentage)

    if "median_household_income" in df.columns:
        df["median_household_income"] = df["median_household_income"].apply(parse_currency)

    for col in ["white_pct", "black_pct", "hispanic_pct", "asian_pct"]:
        if col in df.columns:
            df[col] = df[col].apply(parse_percentage)

    if "population" in df.columns:
        df["population"] = pd.to_numeric(df["population"].astype(str).str.replace(",", ""), errors="coerce")

    return df


def state_summary(shootings: pd.DataFrame) -> pd.DataFrame:
    state_counts = shootings.groupby("state").size().reset_index(name="deaths")
    return state_counts.sort_values("deaths", ascending=False)


def merge_datasets(shootings: pd.DataFrame, census: pd.DataFrame) -> pd.DataFrame:
    state_counts = state_summary(shootings)
    merged = state_counts.merge(census, on="state", how="left")

    if "population" in merged.columns and not merged["population"].isna().all():
        merged["deaths_per_100k"] = merged["deaths"] / merged["population"] * 100000
    else:
        merged["deaths_per_100k"] = np.nan

    return merged


def print_top_states(merged: pd.DataFrame, n: int = 10) -> None:
        print("\nTop states by number of deaths involving police:")
        print(merged[["state", "deaths", "deaths_per_100k", "poverty_rate", "high_school_grad_rate", "median_household_income"]]
            .sort_values(["deaths", "deaths_per_100k"], ascending=[False, False])
            .head(n)
            .to_string(index=False))


def correlation_report(merged: pd.DataFrame) -> None:
    indicators = [
        col for col in ["poverty_rate", "high_school_grad_rate", "median_household_income", "deaths_per_100k"]
        if col in merged.columns
    ]
    subset = merged[indicators].dropna()
    if subset.empty:
        print("\nNot enough data to compute correlations.")
        return
    print("\nCorrelation between socioeconomic indicators and police-involved deaths:")
    corr = subset.corr(method="pearson")
    print(corr.to_string())

    for x in ["poverty_rate", "high_school_grad_rate", "median_household_income"]:
        if x in subset.columns and "deaths_per_100k" in subset.columns:
            coef = subset[x].corr(subset["deaths_per_100k"])
            print(f"  - deaths_per_100k vs {x}: {coef:.3f}")


def analyze_race(shootings: pd.DataFrame, census: pd.DataFrame) -> None:
    if "race" not in shootings.columns:
        print("\nNo 'race' column in police shootings data.")
        return

    race_counts = shootings["race"].value_counts(dropna=False).rename_axis("race").reset_index(name="deaths")
    race_counts["share_of_deaths"] = race_counts["deaths"] / race_counts["deaths"].sum() * 100

    print("\nRacial distribution of police-involved deaths:")
    print(race_counts.to_string(index=False))

    if {"white_pct", "black_pct", "hispanic_pct", "asian_pct"}.issubset(set(census.columns)):
        race_shares = {
            "WHITE": census["white_pct"].mean(),
            "BLACK": census["black_pct"].mean(),
            "HISPANIC": census["hispanic_pct"].mean(),
            "ASIAN": census["asian_pct"].mean(),
        }
        print("\nApproximate population share comparison (national average):")
        for race_key, pop_share in race_shares.items():
            death_share = race_counts.loc[race_counts["race"] == race_key, "share_of_deaths"]
            if not death_share.empty:
                print(f"  - {race_key}: death share = {death_share.iloc[0]:.1f}%, population share ≈ {pop_share:.1f}%")


def plot_indicator_vs_deaths(merged: pd.DataFrame, x: str, label: str, output_path: Path) -> None:
    if x not in merged.columns or "deaths_per_100k" not in merged.columns:
        return

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=merged, x=x, y="deaths_per_100k")
    sns.regplot(data=merged, x=x, y="deaths_per_100k", scatter=False, color="red")
    plt.title(f"Police-involved deaths per 100k vs {label}")
    plt.xlabel(label)
    plt.ylabel("Deaths per 100k")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"Plot saved to: {output_path}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze police-involved deaths in the U.S. together with state-level census indicators."
    )
    parser.add_argument(
        "--shootings",
        type=Path,
        default=None,
        help="Path to the police shootings CSV file.",
    )
    parser.add_argument(
        "--census",
        type=Path,
        default=None,
        help="Path to the state-level census CSV file.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("analysis_output"),
        help="Directory where plots will be saved.",
    )
    args = parser.parse_args()

    folder = Path(__file__).resolve().parent
    shootings_path = args.shootings or find_dataset_file(folder, DATASET_CANDIDATES)
    census_path = args.census or find_dataset_file(folder, CENSUS_CANDIDATES)

    if shootings_path is None:
        print("No police shootings dataset found. Look for one of these names:")
        for candidate in DATASET_CANDIDATES:
            print(f"  - {candidate}")
        return

    if census_path is None:
        print("No census data file found. Look for one of these names:")
        for candidate in CENSUS_CANDIDATES:
            print(f"  - {candidate}")
        return

    print(f"Loading police shootings data from: {shootings_path}")
    print(f"Loading census data from: {census_path}")

    shootings = load_police_shootings(shootings_path)
    census = load_census(census_path)

    merged = merge_datasets(shootings, census)
    print_top_states(merged, n=15)
    correlation_report(merged)
    analyze_race(shootings, census)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    plot_indicator_vs_deaths(merged, "poverty_rate", "Poverty rate", args.output_dir / "deaths_vs_poverty.png")
    plot_indicator_vs_deaths(merged, "high_school_grad_rate", "High school graduation rate", args.output_dir / "deaths_vs_high_school_grad.png")
    plot_indicator_vs_deaths(merged, "median_household_income", "Median household income", args.output_dir / "deaths_vs_income.png")

    print("\nAnalysis complete. Check console output and generated plots.")


if __name__ == "__main__":
    main()
