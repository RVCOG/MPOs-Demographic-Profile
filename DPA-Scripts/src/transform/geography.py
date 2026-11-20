# transform/geography.py
class GeographyProcessor:
    
    def create_geoid(self, df, source_column="geo_id"):
        series = df[source_column].astype(str)
        lengths = series.str.len()

        if lengths.isin([20, 21]).all():
            df["geoid"] = series.str.split("US").str[-1]
        else:
            raise ValueError(
                f"Unexpected GEOID length found in '{source_column}': {lengths.unique().tolist()}"
            )

        return df


    def create_county_geoid(self, df, source_column="geoid"):
        df["CountyFIPS"] = df[source_column].str[2:5]
        return df


    def create_state_fips(self, df, source_column="geoid"):
        df["StateFIPS"] = df[source_column].str[:2]
        return df    


    def process(self, df):
        df = self.create_geoid(df)
        df = self.create_county_geoid(df)
        df = self.create_state_fips(df)
        return df
        
