# transform/validator.py
class DatasetValidator:

    def __init__(self):
        #self.dataset = dataset
        self.required_columns = [
            "geoid", "geography_name", 
            "CountyFIPS", "StateFIPS",
            "total_population"
        ]

    def validate_record_availability(self, df):
        # Implement validation logic here
        if not df:
            raise ValueError("Dataset is empty or None")
        # Additional validation checks can be added here
        return True

    def validate_columns(self, df):
        missing = [
            col for col in self.required_columns if col not in df.columns 
        ]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
        return print("All required columns exists.")


    def validate_dtype(self, df):
        txt_cols = ['geo_id', 'geography_name', "CountyFIPS", "StateFIPS"]
        non_float = df.select_dtypes(exclude=["float"]).columns

        leftover = [
            col for col in non_float if col not in txt_cols 
        ]

        if leftover:
            raise ValueError(f"Unexpected column dtype. Check columns: {leftover}")
        

    def validate_duplicates(self, df):
        duplicates = (
            df["geoid"].duplicated().sum()
        )
        if duplicates > 0:
            raise ValueError (f"{duplicates} duplicate GEOIDd found")
        return print("No GEOIDs duplicates found.")


    def validate_population(self, df):
        bad_records = (df["total_population"] < 0).sum()

        if bad_records > 0:
            raise ValueError(
                "Negative population values found."
            )

    def validate(self, df):
        self.validate_columns(df)
        self.validate_dtype(df)
        self.validate_duplicates(df)
        self.validate_population(df)





# testing class
# df = pd.DataFrame(
#     {
#         "geoid": ["123456", "12345", "123456"],
#         "geography_name": ["block10", "block10", "block10"],
#         "CountyFIPS": ["029", "029", "029"],
#         "StateFIPS": ["41", "41", "41"],
#         "total_population":[1000.00, 50, 300], 
#         "percentage": [90.00, 14, 5.01]
#     }
# )

# validator = DatasetValidator()

