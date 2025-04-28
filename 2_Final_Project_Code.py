# Final Project Code
# Team Members: Tawfiq Abulail and Aidan Susnar

# import libraries we learned in class
import pandas as pd  # data handling
import numpy as np  # numerical operations
import matplotlib.pyplot as plt  # plotting basic graphs
import seaborn as sns  # advanced visualization
from scipy import stats  # for statistical operations
from sklearn.preprocessing import StandardScaler  # feature scaling

# load data
data_path = '/mnt/data/global_air_pollution_data.csv'  # path to dataset
air_quality_data = pd.read_csv(data_path)

# display first few rows to make sure it loaded correctly
print(air_quality_data.head())

# clean data
# check for missing values
print(air_quality_data.isnull().sum())

# drop rows with missing values (safe since we have enough data)
air_quality_data = air_quality_data.dropna()

# reset index after dropping rows
air_quality_data = air_quality_data.reset_index(drop=True)

# basic information after cleaning
print(air_quality_data.info())

# Research Question 1: Which countries have the highest average AQI?
# group data by country and calculate mean AQI
country_aqi = air_quality_data.groupby('country')['AQI Value'].mean().sort_values(ascending=False)

# print top 10 countries
print(country_aqi.head(10))

# plot top 10 countries with highest AQI
plt.figure(figsize=(12,6))
sns.barplot(x=country_aqi.head(10).index, y=country_aqi.head(10).values)
plt.title('Top 10 Countries by Average AQI')
plt.xlabel('Country')
plt.ylabel('Average AQI Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Research Question 2: Which pollutant (PM2.5, CO, NO2, Ozone) is most correlated with poor air quality?
# calculate correlation between AQI and main pollutants
pollutants = ['PM2.5', 'CO', 'NO2', 'Ozone']
correlations = {}

for pollutant in pollutants:
    if pollutant in air_quality_data.columns:
        corr, _ = stats.pearsonr(air_quality_data['AQI Value'], air_quality_data[pollutant])
        correlations[pollutant] = corr

# print correlations
print("Correlation of Pollutants with AQI:")
for pollutant, corr_value in correlations.items():
    print(f"{pollutant}: {corr_value:.2f}")

# plot correlation values
plt.figure(figsize=(8,5))
sns.barplot(x=list(correlations.keys()), y=list(correlations.values()))
plt.title('Pollutants Correlation with AQI')
plt.xlabel('Pollutant')
plt.ylabel('Correlation Coefficient')
plt.grid(True)
plt.show()

# Research Question 3 (Optional): What are the top 10 most polluted cities worldwide?
# group by city and calculate mean AQI
city_aqi = air_quality_data.groupby('city')['AQI Value'].mean().sort_values(ascending=False)

# print top 10 cities
print(city_aqi.head(10))

# plot top 10 cities
plt.figure(figsize=(12,6))
sns.barplot(x=city_aqi.head(10).index, y=city_aqi.head(10).values)
plt.title('Top 10 Most Polluted Cities by Average AQI')
plt.xlabel('City')
plt.ylabel('Average AQI Value')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Conclusion (simple print statements)
print("\nConclusion:")
print("1. The countries with the highest average AQI are", country_aqi.index[0:3].tolist())
print("2. The pollutant most correlated with poor air quality is:", max(correlations, key=correlations.get))
print("3. The most polluted city worldwide based on average AQI is:", city_aqi.index[0])