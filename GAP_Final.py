# ------------------------------------------------------
# Final Project for INFO-B 211
# Tawfiq Abulail & Aidan Susnar
# Research Questions:
# 1. Which countries have the highest average AQI?
# 2. Which pollutant (PM2.5, CO, NO2, Ozone) is most correlated with poor air quality?
# 3. (Optional) What are the top 10 most polluted cities worldwide?
# ------------------------------------------------------

# import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr

# load dataset
pollution_data = pd.read_csv('global_air_pollution_data.csv')

# ----------------------------------
# Data Cleaning Section
# ----------------------------------

# rename columns to remove tab character
pollution_data = pollution_data.rename(columns={'co_aqi_value\t': 'co_aqi_value'})

# drop rows with missing country names
pollution_data = pollution_data.dropna(subset=['country_name'])

# make sure numeric columns are integers
pollution_data['aqi_value'] = pollution_data['aqi_value'].astype(int)
pollution_data['co_aqi_value'] = pollution_data['co_aqi_value'].astype(int)
pollution_data['ozone_aqi_value'] = pollution_data['ozone_aqi_value'].astype(int)
pollution_data['no2_aqi_value'] = pollution_data['no2_aqi_value'].astype(int)
pollution_data['pm2.5_aqi_value'] = pollution_data['pm2.5_aqi_value'].astype(int)

# ----------------------------------
# Research Question 1: Country AQI Rankings
# ----------------------------------

# group by country and calculate average AQI
country_avg_aqi = pollution_data.groupby('country_name')['aqi_value'].mean().sort_values(ascending=False)

# visualize top 10 worst countries
plt.figure(figsize=(12,6))
sns.barplot(x=country_avg_aqi.head(10), y=country_avg_aqi.head(10).index)
plt.title('Top 10 Countries with Highest Average AQI')
plt.xlabel('Average AQI')
plt.ylabel('Country')
plt.tight_layout()
plt.show()

# ----------------------------------
# Research Question 2: Pollutant Correlations
# ----------------------------------

# calculate correlation between each pollutant and AQI
pollutants = ['co_aqi_value', 'ozone_aqi_value', 'no2_aqi_value', 'pm2.5_aqi_value']
correlations = {}

for pollutant in pollutants:
    corr, _ = pearsonr(pollution_data[pollutant], pollution_data['aqi_value'])
    correlations[pollutant] = corr

# create a bar plot for pollutant correlations
plt.figure(figsize=(8,5))
sns.barplot(x=list(correlations.values()), y=list(correlations.keys()))
plt.title('Correlation of Pollutants with Overall AQI')
plt.xlabel('Pearson Correlation Coefficient')
plt.ylabel('Pollutant')
plt.tight_layout()
plt.show()

# ----------------------------------
# Research Question 3 (Optional): Top 10 Polluted Cities
# ----------------------------------

# group by city and calculate average AQI
city_avg_aqi = pollution_data.groupby('city_name')['aqi_value'].mean().sort_values(ascending=False)

# visualize top 10 worst cities
plt.figure(figsize=(12,6))
sns.barplot(x=city_avg_aqi.head(10), y=city_avg_aqi.head(10).index)
plt.title('Top 10 Most Polluted Cities (Average AQI)')
plt.xlabel('Average AQI')
plt.ylabel('City')
plt.tight_layout()
plt.show()

# ------------------------------------------------------
# END OF FINAL PROJECT CODE
# Tawfiq Abulail & Aidan Susnar
# ------------------------------------------------------