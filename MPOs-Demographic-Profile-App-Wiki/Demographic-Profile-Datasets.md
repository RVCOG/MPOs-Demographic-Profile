# ACS Data
The American Community Survey (ACS)[^1] is the premier source of detailed information about the nation's people and housing. As an ongoing survey conducted by the U.S. Census Bureau since 2005, the ACS collects detailed social, economic, housing, and demographic information from a sample of households across the 50 states, the District of Columbia, and Puerto Rico.


American Community Survey (ACS) are used as a primary data source for the Demographic Profile App. The App will use the 5-year estimates for a better data accuracy. 


# ACS Data Tables
Currently there are approximatly 5 different ACS data tables that are used to generate the required Title VI analysis. To build on those dataset for a comprehensive demographic viewer app, addtional tables are proposed to be added - please note this is a **Minimum Viable Product (MVP)** more dataset and application might be added in future as demaned by uses increase.   

The datasets are group into two categories: 
1) Population Profile
2) Housing Profile

Below are the proposed tables to be used:

<table>
  <tr>
    <th>Category</th>
    <th>Table Name</th>
    <th>Table ID</th>
  </tr>
  <tr>
    <td rowspan="6">Population Profile</td>
    <td>Population by Age</td>
    <td>B01001</td>
  </tr>
  <tr>
    <td>Population by Race</td>
    <td>B02001</td>
  </tr>
  <tr>
    <td>Minority Population</td>
    <td>B03002</td>
  </tr>
  <tr>
    <td>Senior Population</td>
    <td>B01001</td>
  </tr>
  <tr>
    <td>Persons with Disabilities</td>
    <td>B22010</td>
  </tr>
  <tr>
    <td>Persons Who Speak English Less Than Well</td>
    <td>B16004</td>
  </tr>
  <tr>
    <td rowspan="2">Housing Profile</td>
    <td>Household Poverty</td>
    <td>C17002, S17010</td>
  </tr>
  <tr>
    <td>Households with No Vehicles</td>
    <td>B25044</td>
  </tr>
</table>








---
[^1]:https://www.test.census.gov/programs-surveys/acs/about/information-guide.html