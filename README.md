# Commute-Map

### Records real-time driving time from various starting locations to different destinations (2 main dest). 

### A designated tool to help a household choose the perfect apartment (in terms of daily commute time) from their selections, that record the commute time on road, with consideration of real-time traffic condition during each time period of the day, to their work and school. 

### Utilizing Python and GoogleAPI distance matrix

### Usage
* Modify address.json file: Enter "home" address in the home list, work address in work entry, and school address in school.   
* Scripts can be run manually or a .bat file can be created and run on any interested time of the day (for example, during peak hours and regualr hours). 

### Sample CSV file output with dummy address entries:
|start                                 |dest                        |date      |start_time|travel_time|
|--------------------------------------|----------------------------|----------|----------|-----------|
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/06/2022|08:16     |31 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/06/2022|08:16     |35 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/06/2022|08:16     |27 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/06/2022|08:16     |21 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/06/2022|09:06     |23 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/06/2022|09:06     |24 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/06/2022|09:06     |22 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/06/2022|09:06     |19 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/06/2022|13:40     |24 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/06/2022|13:40     |25 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/06/2022|13:40     |22 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/06/2022|13:40     |19 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/06/2022|18:22     |26 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/06/2022|18:22     |28 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/06/2022|18:22     |26 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/06/2022|18:22     |19 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/06/2022|20:13     |21 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/06/2022|20:13     |22 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/06/2022|20:13     |20 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/06/2022|20:13     |16 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/07/2022|18:51     |23 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/09/2022|09:22     |26 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/09/2022|09:22     |26 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/09/2022|09:22     |24 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/09/2022|09:22     |20 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/09/2022|12:06     |22 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/09/2022|12:06     |22 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/09/2022|12:06     |21 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/09/2022|12:06     |18 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/09/2022|15:17     |25 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/09/2022|15:17     |27 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/09/2022|15:17     |22 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/09/2022|15:17     |20 mins    |
|101 FirstApartment St, City, ST 01234 |1 Work St, City, ST 01234   |05/10/2022|19:42     |20 mins    |
|101 FirstApartment St, City, ST 01234 |1 School Ave, City, ST 01234|05/10/2022|19:42     |20 mins    |
|202 SecondApartment Ln, City, ST 01234|1 Work St, City, ST 01234   |05/10/2022|19:42     |20 mins    |
|202 SecondApartment Ln, City, ST 01234|1 School Ave, City, ST 01234|05/10/2022|19:42     |17 mins    |

### Household individuals can decide which apartment better suits their needs based on the daily commute time to work and school. 