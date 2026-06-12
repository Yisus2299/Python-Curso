from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).parent
DEFAULT_CSV_NAMES = [
    'space_missions.csv',
    'space_race_launches.csv',
    'launches.csv',
    'space_data.csv',
]


def find_dataset():
    candidates = [PROJECT_DIR / name for name in DEFAULT_CSV_NAMES if (PROJECT_DIR / name).exists()]
    candidates += sorted(PROJECT_DIR.glob('*.csv'))
    candidates += sorted(PROJECT_DIR.glob('*.xlsx'))
    if not candidates:
        raise FileNotFoundError(
            'No data file found in the project. Place a CSV here or update DATA_PATH.'
        )
    return candidates[0]


def load_space_data(data_path=None):
    path = Path(data_path) if data_path else find_dataset()
    if path.suffix.lower() == '.csv':
        return pd.read_csv(path, low_memory=False)
    if path.suffix.lower() in ['.xls', '.xlsx']:
        return pd.read_excel(path)
    raise ValueError(f'Unsupported file format: {path.suffix}')


def clean_space_data(df):
    df = df.copy()
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    if 'net' in df.columns:
        df['launch_date'] = pd.to_datetime(df['net'], errors='coerce', utc=True)
    elif 'window_start' in df.columns:
        df['launch_date'] = pd.to_datetime(df['window_start'], errors='coerce', utc=True)
    elif 'date' in df.columns:
        df['launch_date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)

    if 'cost' in df.columns:
        df['cost_usd'] = pd.to_numeric(df['cost'], errors='coerce')
    elif 'mission_cost' in df.columns:
        df['cost_usd'] = pd.to_numeric(df['mission_cost'], errors='coerce')

    if 'status' in df.columns:
        df['status_clean'] = df['status'].astype(str).str.lower().str.strip()
    elif 'outcome' in df.columns:
        df['status_clean'] = df['outcome'].astype(str).str.lower().str.strip()
    else:
        df['status_clean'] = pd.NA

    df['success'] = df['status_clean'].astype(str).str.contains('success|ok|complete', na=False)
    df['failure'] = df['status_clean'].astype(str).str.contains('fail|failure|partial', na=False)

    if 'country' not in df.columns and 'launch_service_provider_country' in df.columns:
        df['country'] = df['launch_service_provider_country']
    if 'organization' not in df.columns and 'launch_service_provider_name' in df.columns:
        df['organization'] = df['launch_service_provider_name']

    if 'launch_date' in df.columns:
        df['launch_year'] = df['launch_date'].dt.year
        df['launch_month'] = df['launch_date'].dt.month_name()
        df['launch_month_number'] = df['launch_date'].dt.month
    else:
        df['launch_year'] = pd.NA
        df['launch_month'] = pd.NA
        df['launch_month_number'] = pd.NA

    return df


def main():
    df = load_space_data()
    print('Dataset loaded with', len(df), 'rows and', len(df.columns), 'columns')
    df = clean_space_data(df)
    print('Available columns:', list(df.columns))
    print('Min/Max years:', df['launch_year'].min(), df['launch_year'].max())
    print('Total successes:', int(df['success'].sum() if 'success' in df else 0))


if __name__ == '__main__':
    main()
