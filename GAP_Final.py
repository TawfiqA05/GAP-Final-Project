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
pollution_data = pd.read_csv('/Users/lambirghinibugatti/Downloads/B211/global_air_pollution_data.csv')

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
plt.figure(figsize=(12, 6))
sns.barplot(x=city_avg_aqi.head(10).values, y=city_avg_aqi.head(10).index, palette="Reds_r")
plt.title('Top 10 Most Polluted Cities (Average AQI)')
plt.xlabel('Average AQI')
plt.ylabel('City')
plt.tight_layout() 
plt.show()
# ------------------------------------------------------
# END OF FINAL PROJECT CODE
# Tawfiq Abulail & Aidan Susnar
# ------------------------------------------------------

# Get the number of rows in the dataset
print(f"Number of rows in the dataset: {pollution_data.shape[0]}")




# Get the top 10 worst countries by AQI
top_countries = country_avg_aqi.head(10).index

# Filter data for the top 10 countries
top_countries_data = pollution_data[pollution_data['country_name'].isin(top_countries)]

# Normalize pollutant AQI values and calculate percentage contributions
pollutants = ['co_aqi_value', 'ozone_aqi_value', 'no2_aqi_value', 'pm2.5_aqi_value']
for pollutant in pollutants:
    top_countries_data[f'{pollutant}_contribution'] = (top_countries_data[pollutant] / top_countries_data[pollutants].sum(axis=1)) * 100

# Calculate average contributions for each pollutant by country
avg_contributions = top_countries_data.groupby('country_name')[[f'{p}_contribution' for p in pollutants]].mean()

# Visualize pollutant contributions
avg_contributions.plot(kind='bar', stacked=True, figsize=(12, 6), colormap='viridis')
plt.title('Pollutant Contribution to AQI in Top 10 Worst Countries')
plt.xlabel('Country')
plt.ylabel('Percentage Contribution')
plt.legend(title='Pollutants')
plt.tight_layout()
plt.show()





# Calculate total contributions for each pollutant in the top 10 worst countries
total_contributions = top_countries_data.groupby('country_name')[pollutants].sum()

# Print the total contributions for each pollutant
print("Total Contributions of Each Pollutant to AQI in Top 10 Worst Countries:")
print(total_contributions)

# Visualize total contributions as a bar plot
total_contributions.plot(kind='bar', figsize=(12, 6), colormap='plasma')
plt.title('Total Contributions of Pollutants to AQI in Top 10 Worst Countries')
plt.xlabel('Country')
plt.ylabel('Total AQI Contribution')
plt.legend(title='Pollutants')
plt.tight_layout()
plt.show()

