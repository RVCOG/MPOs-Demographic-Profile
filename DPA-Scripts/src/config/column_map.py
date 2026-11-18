# --------------------------------------
# Description: This file host list of columns used to process the US Census dataset
#              to use for Title VI products. 
#
# Date: 11-17-2026
# --------------------------------------

# required columns for senior dataset
# table id B01001 
senior_cols: list[str] = [
    'B01001_001E','B01001_002E','B01001_020E', 'B01001_021E',
    'B01001_022E', 'B01001_023E', 'B01001_024E', 'B01001_025E',
    'B01001_026E','B01001_044E','B01001_045E', 'B01001_046E',
    'B01001_047E',	'B01001_048E',	'B01001_049E'

]

# required columns for minority dataset
# table id B03002
minority_cols: list[str] = [
    'B03002_001E', 'B03002_002E', 'B03002_003E', 'B03002_012E'

]

# required columns for poverty dataset
# table id B17010
poverty_cols: list[str] = [
    'B17010_001E', 'B17010_002E', 'B17010_022E'

]

# required columns for LEP dataset
# table id B16004
lep_col: list[str] = [
    'B16004_001E', 'B16004_007E', 'B16004_008E', 'B16004_012E', 
    'B16004_013E',	'B16004_017E', 'B16004_018E', 'B16004_022E', 
    'B16004_023E', 'B16004_029E', 'B16004_030E', 'B16004_034E', 
    'B16004_035E', 'B16004_039E', 'B16004_040E', 'B16004_044E',
    'B16004_045E',	'B16004_051E', 'B16004_052E', 'B16004_056E', 
    'B16004_057E',	'B16004_061E','B16004_062E','B16004_066E',
    'B16004_067E'
]

# required columns for vehicle dataset
# table id B25044
noCar_col: list[str] = [
    'B25044_001E', 'B25044_001M', 'B25044_002E',
    'B25044_002M', 'B25044_009E', 'B25044_009M'
]

# required columns for disability dataset
# table id B22010
disability_col: list[str] = [
    'B22010_001E', 'B22010_001M'
]
