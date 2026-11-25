# indicators/minority.py
from indicators.utils import validate_columns, safe_percent

def calculate_minority(df,
                       county_column='CountyFIPS',
                       total_population_column='total_population',
                       white_non_hispanic='white_non_hispanic'):
    """
        Minority Indicator

        Input:
            df
            county_column
            total_population
            white_non_hispanic

        Output:
            minority_population
            minority_county_pct (Calculate County Percentage by block group (row-by-row rate))
            minority_regional_pct (Calculate Regional Percentage by block group (row-by-row rate))
    """
    
    validate_columns(df=df,
                     required_columns= [
                         total_population_column, white_non_hispanic
                         ]
                    )
    
    # minority population
    df['minority_population'] = (
        df[total_population_column] - df[white_non_hispanic]
        )
    # minority percentage
    df['minority_pct'] = safe_percent(
        df['minority_population'], df[total_population_column]
        )
    
    # county population (individually)
    county_population = (
        df.groupby(county_column)
        [total_population_column].transform('sum')
        )
    # regional population 
    regional_population = (
        df[total_population_column].sum()
        )
    
    
    # share of county
    df['minority_county_pct'] = safe_percent(df['minority_population'], county_population)
    # share of region
    df['minority_regional_pct'] = safe_percent(df['minority_population'], regional_population)
    

    return df
