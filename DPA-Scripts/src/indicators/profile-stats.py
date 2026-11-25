# indicators/profile-stats.py

import pandas as pd

def summarize_population(df, pop_col='total_population'):
    """
    Generate dataset-level population statistics.

    Returns:
        dict
    """

    if df.empty:
        return {
            'record_count': 0,
            'state_fips': [],
            'county_fips': [],
            'total_population': 0,
            'average_population': None,
            'median_population': None,
            'std_population': None,
            'min_population': None,
            'max_population': None
        }

    return {
        'record_count': len(df),

        'state_fips': sorted(
            df['StateFIPS']
            .dropna()
            .unique()
            .tolist()
        ),

        'county_fips': sorted(
            df['CountyFIPS']
            .dropna()
            .unique()
            .tolist()
        ),

        'total_population': int(
            df[pop_col].sum()
        ),

        'average_population': round(
            df[pop_col].mean(),
            2
        ),

        'median_population': round(
            df[pop_col].median(),
            2
        ),

        'std_population': round(
            df[pop_col].std(),
            2
        ),

        'min_population': int(
            df[pop_col].min()
        ),

        'max_population': int(
            df[pop_col].max()
        )
    }

def summarize_minority(df):
    """
    Generate dataset-level population statistics.

    Returns:
        dict
    """
    minority_pop = (
        df['minority_population']
        .sum()
    )

    total_pop = (
        df['total_population']
        .sum()
    )

    return {
        'total_population': total_pop,
        'minority_population': minority_pop,
        'minority_pct': (
            minority_pop / total_pop * 100
            if total_pop > 0 else None
        )
    }

def summarize_minority_by_county(df):
    """
    Generate dataset-level population statistics.

    Returns:
        PD.DataFrame
    """
    county_stats = (
        df
        .groupby('CountyFIPS')
        .agg(
            total_population=(
                'total_population',
                'sum'
            ),
            minority_population=(
                'minority_population',
                'sum'
            )
        )
    )

    county_stats['minority_pct'] = (
        county_stats['minority_population']
        /
        county_stats['total_population']
        * 100
    )

    return county_stats