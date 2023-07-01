# python-api-challenge - WeatherPy and VacationPy
This repository contains the code and files for the WeatherPy and VacationPy projects. The WeatherPy project aims to analyze weather data from various cities and visualize the relationship between weather variables and latitude. Additionally, the VacationPy project uses weather data to plan future vacations and create map visualizations.

## WeatherPy

In the WeatherPy project, a Python script was used to visualize the weather of over 500 cities located at varying distances from the equator. 

### Requirement 1: Create plots to showcase the relationship between weather variables and latitude
To fulfill this requirement, the OpenWeatherMap API retrieved weather data for the cities generated in the code. The following scatter plots were created to showcase the relationships between weather variables and latitude:

1. Latitude vs. Temperature
2. Latitude vs. Humidity
3. Latitude vs. Cloudiness
4. Latitude vs. Wind Speed

### Requirement 2: Compute linear regression for each relationship
For this requirement, linear regression analysis was performed for each relationship between weather variables and latitude. The scatter plots are separated into Northern Hemisphere (greater than or equal to 0 degrees latitude) and Southern Hemisphere (less than 0 degrees latitude). The linear regression line, the model's formula, and the r-values are included in the plots.

The scatter plots and linear regression analysis help identify and describe any relationships between weather variables and latitude.

## VacationPy

In the VacationPy project, weather data skills are applied to plan future vacations. Jupyter notebooks, the hvplot Python library, and the Geoapify API were also used.

### Requirement 1: Create a map displaying a point for every city 
For this requirement, a map was created using the hvplot library. The map displays a point for every city in the city_data_df DataFrame. The "size" of the point represents the humidity in each city.

### Requirement 2: Narrow down the DataFrame 
The city_data_df DataFrame was narrowed down to find cities that meet my ideal weather conditions. The output was used to create a new DataFrame.

### Requirement 3: Identify hotels located near each city in the new DataFrame
For each city in hotel_df, the Geoapify API was used to find the first hotel located within 10,000 meters of the city's coordinates.

### Requirement 4: Create another map displaying a point for every city in the new DataFrame
The hotel name and country information were added to the hover message for each city on the map, creating a map visualization with hotel information.


## Additional Resources Used
https://hvplot.holoviz.org<br />
https://holoviz.org<br />
https://stackoverflow.com<br />
https://www.geeksforgeeks.org<br />
Tutor appointment
