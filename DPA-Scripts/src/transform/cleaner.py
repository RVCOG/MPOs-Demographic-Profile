#transform/cleaner.py
import yaml 
import pandas as pd 



class CensusCleaner:
    def __init__(
            self,
            column_map_file=r"src\config\columns_map"
            ) -> None:
        with open(column_map_file) as f:
            self.column_map = yaml.safe_load(f)

    def rename_columns(self, df):
        df = df.drop(0)
        return df.rename(columns=self.column_map)
    
    def convert_to_numeric(self, df):
        txt_cols = ['geo_id', 'geography_name']
        num_cols = [col for col in df.columns if col not in txt_cols]
        df[num_cols] = df[num_cols].apply(pd.to_numeric, errors='coerce').astype('float64')
        return df
    
    def remove_duplicates(self, df):
        return df.drope_duplicates()

    def clean(self, df):
        df = self.rename_columns(df)
        df = self.convert_to_numeric(df)
        df = self.remove_duplicates(df)
        return df



# testing class
cleaner = CensusCleaner(column_map_file=r"C:\GitHub-Repo-Workspace\MPOs-Demographic-Profile\DPA-Scripts\src\config\columns_map.yaml")
print(cleaner.column_map)