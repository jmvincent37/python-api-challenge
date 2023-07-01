#!/usr/bin/env python
# coding: utf-8

# # VacationPy
# ---
# 
# ## Starter Code to Import Libraries and Load the Weather and Coordinates Data

# In[1]:


# Dependencies and Setup
import hvplot.pandas
import pandas as pd
import requests
import matplotlib.pyplot as plt



# Import API key
from api_keys import geoapify_key


# In[2]:


# Load the CSV file created in Part 1 into a Pandas DataFrame
city_data_df = pd.read_csv("output_data/cities.csv")

# Display sample data
city_data_df.head()


# In[3]:


# Check the data types
city_data_df.dtypes


# ---
# 
# ### Step 1: Create a map that displays a point for every city in the `city_data_df` DataFrame. The size of the point should be the humidity in each city.

# In[4]:


get_ipython().run_cell_magic('capture', '--no-display', '\n# Configure the map plot\nmap_plot_humidity = city_data_df.hvplot.points(\n    "Lng",\n    "Lat",\n    geo = True,\n    tiles = "OSM",\n    frame_width = 500,\n    frame_height = 500,\n    size = "Humidity",\n    color = "City"\n)\n\n# Display the map plot\nmap_plot_humidity')


# ### Step 2: Narrow down the `city_data_df` DataFrame to find your ideal weather condition

# In[5]:


# Narrow down cities that fit criteria and drop any results with null values
ideal_df = city_data_df.loc[(city_data_df['Max Temp'] < 80) & (city_data_df['Humidity'] < 50) & (city_data_df['Wind Speed'] < 6),:]
ideal_df


# In[6]:


# Number of rows (cities with ideal conditions) and columns.
ideal_df.shape


# In[7]:


# Drop any rows with null values
ideal_df.dropna()


# In[8]:


# Number of rows (cities with ideal conditions) and columns after dropping any null values.
# There were none.
ideal_df.shape


# ### Step 3: Create a new DataFrame called `hotel_df`.

# In[9]:


# Use the Pandas copy function to create DataFrame called hotel_df to store the city, country, coordinates, and humidity
hotel_df = ideal_df.drop(columns = ["City_ID", "Max Temp", "Cloudiness", "Wind Speed", "Date"])

# Add an empty column, "Hotel Name," to the DataFrame so you can store the hotel found using the Geoapify API
hotel_df["Hotel Name"] = ""

# Display sample data
hotel_df


# ### Step 4: For each city, use the Geoapify API to find the first hotel located within 10,000 metres of your coordinates.

# In[10]:


# Set parameters to search for a hotel
radius = 10000
params = {"categories": "accommodation.hotel",
            "limit": "1",
            "apiKey": geoapify_key
}

# Print a message to follow up the hotel search
print("Starting hotel search")

# Iterate through the hotel_df DataFrame
for index, row in hotel_df.iterrows():
    # get latitude, longitude from the DataFrame
    lat = row["Lat"]
    lng = row["Lng"]

    
    # Add filter and bias parameters with the current city's latitude and longitude to the params dictionary
    params["filter"] = f"circle:{lng},{lat},{radius}"
    params["bias"] = f"proximity:{lng},{lat}"
    
    # Set base URL
    base_url = "https://api.geoapify.com/v2/places"


    # Make and API request using the params dictionaty
    # Convert the API response to JSON format
    name_address = requests.get(base_url, params=params).json()
    
    # Grab the first hotel from the results and store the name in the hotel_df DataFrame
    try:
        hotel_df.loc[index, "Hotel Name"] = name_address["features"][0]["properties"]["name"]
    except (KeyError, IndexError):
        # If no hotel is found, set the hotel name as "No hotel found".
        hotel_df.loc[index, "Hotel Name"] = "No hotel found"
        
    # Log the search results
    print(f"{hotel_df.loc[index, 'City']} - nearest hotel: {hotel_df.loc[index, 'Hotel Name']}")

# Display sample data
hotel_df


# ### Step 5: Add the hotel name and the country as additional information in the hover message for each city in the map.

# In[11]:


get_ipython().run_cell_magic('capture', '--no-display', '\n# Configure the map plot\n\nmap_plot_2 = hotel_df.hvplot.points(\n    "Lng",\n    "Lat",\n    geo = True,\n    tiles = "OSM",\n    frame_width = 700,\n    frame_height = 500,\n    size = "Humidity",\n    scale = 0.65,\n    color = "City",\n    hover_cols = "all"\n)\n\n# Display the map\nmap_plot_2')


# In[ ]:




