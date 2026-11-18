# Data Standarization Process   
## Standardizing ACS Tables
After downloading the required data, we will need to prepare the table for GIS Software use and for the Demographic Viewer App. Each ACS Table will require it's own uniqe data standarization - from the data to calculate, data to remove, and data to represent in the app. 

The following steps go over the a general process that should be implemented to all tables:

### 1) Preparing Work Environment
- Create new directory for the work.   
- Save a new copy of the table and add **"Data-Profile-Name"** and **"Standarized"** to the end of the name. 
   - For example:   
    ```ACSDT5Y2024.B16004-LEP-Data-Standarized```   
    ```ACSDT5Y2024.B01001-Minority-Data-Standarized```

- **Column Naming convention:** 
  - Column **SHOULD NOT** have white space instead use _ or - as a seperator.
  - New column names can be one of the two formats:
    1) Should be precise descriptive and short.
       1) For example: Senior-Male, MinorityTotal, R_MinorityRate
    2) Should take from the same format as the ACS coded header.
       1) ACS Tables coded headers naming convention usually consist of the table ID + number of the column + estimate or MoE indicator.    
       For example: ```B01001_001E, B16004_010M```
       2) Example of new columns names ```B01001_SeniorRate, B01001_R_SeniorRate```

- **ACS Table Hierarchy:** Make sure to be read, understand and be familar with [ACS Tables Hierarchy](ACS-Table-Hierarchy.md) to prevent calculation and statistical errors.



### 2) Standarizing Table Header

1) Prepare Table Header
   - Rename [Geography, Geographic Area Name] columns to [GEO_ID, NAME]
   - Rename and prep columns to standarize them for **ArcGIS Pro usage**:
     - Make sure to follow column naming convention as listed above.
     - Column name **SHOULD NOT** have any **white space** as a seperator
     - Column name **SHOULD NOT** have **!** character in it.
       - Good column names: ```Total, NAME, MinorityRate```
       - Bad column names: ```Estimate!!Total: , Estimate!!Total:!!5 to 17 years```
   - ~~Delete the coded header and use the descriptive header instead~~


### 3) Adding New Columns

1) Adding New columns:
   
   1) Adding **raw total numbers for categories** column after the ``Estimate!!Total:`` column.
        - this column reflect the total population numbers for each calculated categories i.e. Total Poverty Population, Total Senior Population.
        - 
   
   2) Adding **County** column after the ``GEOID`` column.
       - First name the column ``COUNTY``
       - County column is important for when we need to filter by or calulate by indvidual county instead of both.  
       - This column contain the census code for each county and it is calculated from the GEOID column.
         - Jackson County Code = 029
         - Josephine County Code = 033
       - To calculate county values:
         - Use this Excel Formula: ```LEFT(TEXTAFTER(A2,"US41"),3)```
           - This formula will extract the 3 numbers after "US41" within the GEOID code which is the county code.
  
   3) Adding **County-Rate-Level** calculation.
        - Column naming convention:
          - This should follow the same naming convention listed above.
          - Add the ``ACS Table ID`` before the calculated category.
          - Column name example: ``B01001_SeniorRate``
        - County Rate calculates the percentage of the specific block group against the county block group total.
        - County Rate can represent both the general rate or a specific one customized for each table. For example, you can calculate a general population percentage rate per block group AND a percentage rate for Senior's (65+) per block group.
        - Add a new column after total estimate column
          - name the column "CountyRate"
          - when calculating specific county rate the column name should reflect the specific calculation.
            - For example: (SeniorRate, MinorityRate)
        - To calculate county rate:
          - Use this Excel Formula: ```(B2/SUMIF($A:$A,A2,$B:$B))*100```
          - Where:
              - B2 = represent individual block group value. 
              - A:A = evaluation range (in our case its the entire county code column)
              - A2 = County code per individual block group
              - B:B = sum range (in our case its the entire estimate total)
              - multiple by a 100 to convert to percentages
  
   4) Adding **Regional-Rate-Level** calculation.
      - Column naming convention:
          - This should follow the same naming convention listed above.
          - Add the ``ACS Table ID`` before the calculated category.
          - Add ``_R_`` to indicate regional level calculation.
          - Column name example: ``B01001_R_SeniorRate``
      - This column has the same concept of the County Rate. But instead of calculating the percentage by county we group both counties and canlucate the regional rate.
      - Add a new column after County Rate column
        - name it "RegionalRate"
        - when calculating specific regional rate the column name should reflect the specific calculation.
          - For example: (R_SeniorRate, R_MinorityRate)
          - The "R" indicates a regional calculation column
      - To calculate county rate:
        - Use this Excel Formula: ```(D2/SUM(D2:D216))*100```
        - where:
          - D2 = estimate total of block group
          - D2:D216 = total of all block groups
          - multiple by a 100 to convert to percentages  


### 4) Simplifing Dataset
Every Table will have a different approach to what a simplified dataset looks like. Currently the data simplification going to follow *Title VI needs specifically*. In the future this might be adjusted to a broader scoope. 

--- 

#### ***Sex by Age (B01001)*** 
Table metadata and data simplifing direction: 

|    |Des.|
|:--:|:--:|
|Table use| This table contains population numbers by sex and age. It is used to calculation Senior Population in Title VI Plan |
| Senior Population Defination | Sum of all population of age 65 and over.  |
| Table Header | See [Standarize Header Section](#2-standarizing-table-header) |
| To Keep | • keep raw numbers for blockgroup i.e. (total, total_male, total_female)<br> • |
| To Add | • [Add These new columns](#3-adding-new-columns) <br>• County-Senior-Rate<br> • Regional-Senior-Rate<br> |
| To Delete | • Delete the coded header after standarizing new header<br> • All the Margin of Error columns<br> • All unnecessary data groups [under 5, 5-9, etc..]<br>  | 
|Future use| This table can analyze the age groups by sex at the blockgroup level|


---