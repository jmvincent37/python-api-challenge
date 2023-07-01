#!/usr/bin/env python
# coding: utf-8

# # WeatherPy
# 
# ---
# 
# ## Starter Code to Generate Random Geographic Coordinates and a List of Cities

# In[1]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt
import numpy as np
import requests
import time
from scipy.stats import linregress

# Import the OpenWeatherMap API key
from api_keys import weather_api_key

# Import citipy to determine the cities based on latitude and longitude
from citipy import citipy


# ### Generate the Cities List by Using the `citipy` Library

# In[2]:


# Empty list for holding the latitude and longitude combinations
lat_lngs = []

# Empty list for holding the cities names
cities = []

# Range of latitudes and longitudes
lat_range = (-90, 90)
lng_range = (-180, 180)

# Create a set of random lat and lng combinations
lats = np.random.uniform(lat_range[0], lat_range[1], size=1500)
lngs = np.random.uniform(lng_range[0], lng_range[1], size=1500)
lat_lngs = zip(lats, lngs)

# Identify nearest city for each lat, lng combination
for lat_lng in lat_lngs:
    city = citipy.nearest_city(lat_lng[0], lat_lng[1]).city_name
    
    # If the city is unique, then add it to a our cities list
    if city not in cities:
        cities.append(city)

# Print the city count to confirm sufficient count
print(f"Number of cities in the list: {len(cities)}")


# ---

# ## Requirement 1: Create Plots to Showcase the Relationship Between Weather Variables and Latitude
# 
# ### Use the OpenWeatherMap API to retrieve weather data from the cities list generated in the started code

# In[3]:


# Set the API base URL
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key

# Define an empty list to fetch the weather data for each city
city_data = []

# Print to logger
print("Beginning Data Retrieval     ")
print("-----------------------------")

# Create counters
record_count = 1
set_count = 1

# Loop through all the cities in our list to fetch weather data
for i, city in enumerate(cities):
        
    # Group cities in sets of 50 for logging purposes
    if (i % 50 == 0 and i >= 50):
        set_count += 1
        record_count = 0

    # Create endpoint URL with each city
    city_url = url + "&q=" + city.replace(" ","+")
    
    # Log the url, record, and set numbers
    print("Processing Record %s of Set %s | %s" % (record_count, set_count, city))

    # Add 1 to the record count
    record_count += 1

    # Run an API request for each of the cities
    try:
        # Parse the JSON and retrieve data
        city_weather = requests.get(city_url).json()

        # Parse out latitude, longitude, max temp, humidity, cloudiness, wind speed, country, and date
        city_lat = city_weather["coord"]["lat"]
        city_lng = city_weather["coord"]["lon"]
        city_max_temp = city_weather["main"]["temp_max"]
        city_humidity = city_weather["main"]["humidity"]
        city_clouds = city_weather["clouds"]["all"]
        city_wind = city_weather["wind"]["speed"]
        city_country = city_weather["sys"]["country"]
        city_date = city_weather["dt"]

        # Append the City information into city_data list
        city_data.append({"City": city, 
                          "Lat": city_lat, 
                          "Lng": city_lng, 
                          "Max Temp": city_max_temp,
                          "Humidity": city_humidity,
                          "Cloudiness": city_clouds,
                          "Wind Speed": city_wind,
                          "Country": city_country,
                          "Date": dt.datetime.strftime(dt.datetime.utcfromtimestamp(city_date), '%m/%d/%y')})

    # If an error is experienced, skip the city
    except:
        print("City not found. Skipping...")
        pass
              
# Indicate that Data Loading is complete 
print("-----------------------------")
print("Data Retrieval Complete      ")
print("-----------------------------")


# In[4]:


# Convert the cities weather data into a Pandas DataFrame
city_data_df = pd.DataFrame(city_data)


# Show Record Count
city_data_df.count()


# In[5]:


# Display sample data
city_data_df.head()


# In[6]:


# Export the City_Data into a csv
city_data_df.to_csv("output_data/cities.csv", index_label="City_ID")


# In[7]:


# Read saved data
city_data_df = pd.read_csv("output_data/cities.csv", index_col="City_ID")

# Display sample data
city_data_df.head()


# ### Create the Scatter Plots Requested
# 
# #### Latitude Vs. Temperature

# In[28]:


# Build scatter plot for latitude vs. temperature
lat = city_data_df["Lat"]
temp = city_data_df["Max Temp"]


plt.scatter(lat,  
            temp,  
            edgecolor="black", linewidths=1, marker="o",  
            alpha=0.8, label="Cities")

# Incorporate the other graph properties
plt.title(f"Latitude vs. Max Temperature "+ time.strftime("%x"))
plt.ylabel("Max Temperature (C)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("output_data/Fig1.png")

# Show plot
plt.show()


# #### Latitude Vs. Humidity

# In[27]:


# Build the scatter plots for latitude vs. humidity
lat = city_data_df["Lat"]
humidity = city_data_df["Humidity"]


plt.scatter(lat,  
            temp,  
            edgecolor="black", linewidths=1, marker="o",  
            alpha=0.8, label="Cities")

# Incorporate the other graph properties
plt.title(f"City Latitude vs. Humidity "+ time.strftime("%x"))
plt.ylabel("Humidity (%)")
plt.xlabel("Latitude")
plt.grid(True)


# Save the figure
plt.savefig("output_data/Fig2.png")

# Show plot
plt.show()


# #### Latitude Vs. Cloudiness

# In[26]:


# Build the scatter plots for latitude vs. cloudiness
lat = city_data_df["Lat"]
cloudiness = city_data_df["Cloudiness"]


plt.scatter(lat,  
            temp,  
            edgecolor="black", linewidths=1, marker="o",  
            alpha=0.8, label="Cities")

# Incorporate the other graph properties
plt.title(f"City Latitude vs. Cloudiness "+ time.strftime("%x"))
plt.ylabel("Cloudiness (%)")
plt.xlabel("Latitude")
plt.grid(True)


# Save the figure
plt.savefig("output_data/Fig3.png")

# Show plot
plt.show()


# #### Latitude vs. Wind Speed Plot

# In[11]:


# Build the scatter plots for latitude vs. wind speed
lat = city_data_df["Lat"]
wind_speed = city_data_df["Wind Speed"]


plt.scatter(lat,  
            temp,  
            edgecolor="black", linewidths=1, marker="o",  
            alpha=0.8, label="Cities")

# Incorporate the other graph properties
plt.title(f"City Latitude vs. Windspeed "+ time.strftime("%x"))
plt.ylabel("Wind Speed(m/s)")
plt.xlabel("Latitude")
plt.grid(True)

# Save the figure
plt.savefig("output_data/Fig4.png")

# Show plot
plt.show()


# ---
# 
# ## Requirement 2: Compute Linear Regression for Each Relationship
# 

# In[12]:


#Define x_values and y_values
x_values = city_data_df.Lat
y_values = city_data_df['Max Temp']


# In[31]:


# Define a function to create Linear Regression plots
def Plot(x_values,y_values,title):

    plt.scatter(x_values,  
                y_values,  
                edgecolor="black", linewidths=1, marker="o",  
                alpha=0.8, label="Cities")

    plt.title(f"Latitude vs. {title} {time.strftime('%x')}")
    plt.ylabel(f"{title}")
    plt.xlabel("Latitude")
    plt.grid(True)
    
    (slope, intercept, rvalue, pvalue, std_err) = linregress(x_values, y_values)
    regress_values = x_values * slope + intercept
    plt.plot(x_values,regress_values,"r-")
    
              
    #plt.show()


#def plot_linear_regression(x_values, y_values, title, y_label, text_coordinates):
(slope, intercept, rvalue, pvalue, std_err) = linregress(x_values, y_values)
    


# In[32]:


# Calculate the regression line values.
regress_values = x_values * slope + intercept
print(regress_values)  


# In[33]:


# Create the line equation string.
line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
print(line_eq)


# In[34]:


# Create a DataFrame with the Northern Hemisphere data (Latitude >= 0)
northern_hemi_df = city_data_df.loc[(city_data_df["Lat"] >= 0)]
# Display sample data

northern_hemi_df.head()


# In[35]:


# Create a DataFrame with the Southern Hemisphere data (Latitude < 0)
southern_hemi_df = city_data_df.loc[(city_data_df["Lat"] < 0)]

# Display sample data
southern_hemi_df.head()


# ###  Temperature vs. Latitude Linear Regression Plot

# In[36]:


# Linear regression on Northern Hemisphere
plt.annotate(f"y={slope:.2f}x + {intercept:.2f}",(20,40), color='red')
Plot(northern_hemi_df.Lat,northern_hemi_df['Max Temp'], "Max Temp")

# Calculate and print the r value
r_value = x_values.corr(northern_hemi_df['Max Temp'])
print(r_value)

# Save the figure
plt.savefig("output_data/Fig5.png")

# Show plot
plt.show()


# In[37]:


# Linear regression on Southern Hemisphere
plt.annotate(f"y={slope:.2f}x + {intercept:.2f}",(-50,80), color='red')
Plot(southern_hemi_df.Lat,southern_hemi_df['Max Temp'], "Max Temp")

# Calculate and print the r value
r_value = x_values.corr(southern_hemi_df['Max Temp'])
print(r_value)

# Save the figure
plt.savefig("output_data/Fig6.png")

# Show plot
plt.show()


# **Discussion about the linear relationship:
# 
# **Northern Hemisphere
# 
# Analysis shows that as latitude increases, temperature decreases moderatley.
# With the r-value being -0.70, this suggests may be a negative correlation between northern hemisphere latitudes and temperatures.
# 
# **Southern Hemisphere
# 
# Analysis shows that as latitude decreases, temperature increases signficantly.
# With the r-value being 0.82, this indicates a strong positive correlation between southern hemisphere latitudes and temperatures.
# 
# 
# Overall, cities closer to the equator experience higher temperatures. The correlation between latitudes and temperatures is more signficant for southern hemispheres.

# ### Humidity vs. Latitude Linear Regression Plot

# In[38]:


# Linear regression on Northern Hemisphere
plt.annotate(f"y={slope:.2f}x + {intercept:.2f}",(60,20), color='red')
Plot(northern_hemi_df.Lat,northern_hemi_df["Humidity"], "Humidity")

# Calculate and print the r value
r_value = x_values.corr(northern_hemi_df["Humidity"])
print(r_value)

# Save the figure
plt.savefig("output_data/Fig7.png")

# Show plot
plt.show()


# In[39]:


# Linear regression on Southern Hemisphere
plt.annotate(f"y={slope:.2f}x + {intercept:.2f}",(-50,20), color='red')
Plot(southern_hemi_df.Lat,southern_hemi_df["Humidity"], "Humidity")

# Calculate and print the r value
r_value = x_values.corr(southern_hemi_df["Humidity"])
print(r_value)

# Save the figure
plt.savefig("output_data/Fig8.png")

# Show plot
plt.show()


# **Discussion about the linear relationship:
# 
# For both northern and southern hemisphere cities there is no statistical correlation between latitude and humidity levels.

# ### Cloudiness vs. Latitude Linear Regression Plot

# In[40]:


# Northern Hemisphere
plt.annotate(f"y={slope:.2f}x + {intercept:.2f}",(-3,-3), color='red')
Plot(northern_hemi_df.Lat,northern_hemi_df["Cloudiness"], "Cloudiness")

# Calculate and print the r value
r_value = x_values.corr(northern_hemi_df["Cloudiness"])
print(r_value)

# Save the figure
plt.savefig("output_data/Fig9.png")

# Show plot
plt.show()


# In[41]:


# Southern Hemisphere
plt.annotate(f"y={slope:.2f}x + {intercept:.2f}",(-55,10), color='red')
Plot(southern_hemi_df.Lat,southern_hemi_df["Cloudiness"], "Cloudiness")

# Calculate and print the r value
r_value = x_values.corr(southern_hemi_df["Cloudiness"])
print(r_value)

# Save the figure
plt.savefig("output_data/Fig10.png")

# Show plot
plt.show()


# **Discussion about the linear relationship:** 
# 
# For both northern and southern hemisphere cities there is no statistical correlation between latitude and cloudiness.

# ### Wind Speed vs. Latitude Linear Regression Plot

# In[42]:


# Northern Hemisphere
plt.annotate(f"y={slope:.2f}x + {intercept:.2f}",(45,26), color='red')
Plot(northern_hemi_df.Lat,northern_hemi_df["Wind Speed"], "Wind Speed")

# Calculate and print the r value
r_value = x_values.corr(northern_hemi_df["Wind Speed"])
print(r_value)

# Save the figure
plt.savefig("output_data/Fig11.png")

# Show plot
plt.show()


# In[43]:


# Southern Hemisphere
plt.annotate(f"y={slope:.2f}x + {intercept:.2f}",(-45,22), color='red')
Plot(southern_hemi_df.Lat,southern_hemi_df["Wind Speed"], "Wind Speed")

# Calculate and print the r value
r_value = x_values.corr(southern_hemi_df["Wind Speed"])
print(r_value)

# Save the figure
plt.savefig("output_data/Fig12.png")

# Show plot
plt.show()


# **Discussion about the linear relationship:** 
# 
# For both northern and southern hemisphere cities there is no statistical correlation between latitude and wind speeds.

# In[ ]:





# In[ ]:




