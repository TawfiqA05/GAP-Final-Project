# Project Overview
This Python project analyzes global air pollution data to answer the following research questions:

- Which countries have the highest average Air Quality Index (AQI)?
- Which pollutant (PM2.5, CO, NO2, Ozone) is most correlated with poor air quality?
- (Optional) What are the top 10 most polluted cities worldwide?

We used Python data science tools and included all topics covered in INFO-B 211:

- Pandas for data handling
- NumPy for numeric operations
- SciPy for Pearson correlation analysis
- Matplotlib for basic plotting
- Seaborn for enhanced visualization
- Scikit-learn for machine learning (Decision Tree Regressor)
- Standard modules (os, sys if needed)

---

# Files

| File | Description |
|:-----|:------------|
| `GAP_Final.py` | Main Python script containing all analysis and visualizations |
| `global_air_pollution_data.csv` | Air pollution dataset |
| `README.md` | This file explaining the project |

---

# How to Run

1. Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scipy scikit-learn
```
2. Make sure the dataset `global_air_pollution_data.csv` is in the correct path.
3. Run the `GAP_Final.py` script.

The script will output:
- Bar charts for AQI rankings by country
- Correlation analysis between pollutants and AQI
- Pollutant contribution breakdown for top 10 worst countries
- Machine learning feature importance results from a Decision Tree Regressor

---

# Project Workflow

## 1. Data Import and Cleaning
- Imported the dataset using `pandas.read_csv()`.
- Renamed the `co_aqi_value\t` column to `co_aqi_value` to fix formatting.
- Dropped rows missing a `country_name`.
- Converted all pollutant AQI columns and `aqi_value` to integers for consistency.

## 2. Research Question 1 - Country AQI Rankings
- Grouped the data by `country_name`.
- Calculated the mean AQI per country.
- Visualized the Top 10 countries with the highest average AQI using a bar chart (Seaborn).

## 3. Research Question 2 - Pollutant Correlations
- Calculated Pearson correlation coefficients between each pollutant (PM2.5, CO, NO2, Ozone) and the overall AQI.
- Displayed correlation strengths using a horizontal bar chart (Seaborn).

## 4. Research Question 3 (Optional) - Top 10 Polluted Cities
- Grouped the data by `city_name` and calculated the mean AQI.
- Visualized the Top 10 cities with the highest AQI using a Seaborn barplot.

## 5. Deeper Pollutant Contribution Analysis
- Focused on the Top 10 worst countries by AQI.
- Normalized pollutant values to determine percentage contributions to AQI per country.
- Visualized stacked bar plots showing pollutant percentage breakdowns.

## 6. Machine Learning Model
- Built a `DecisionTreeRegressor` model using scikit-learn.
- Used `pm2.5_aqi_value`, `co_aqi_value`, `no2_aqi_value`, and `ozone_aqi_value` as features to predict `aqi_value`.
- Split the data into training and testing sets.
- Fitted the model and extracted feature importances.
- Displayed pollutant importance in a ranked DataFrame.

---

# Libraries Used

| Library | Purpose |
|:--------|:--------|
| pandas | Load and clean tabular data |
| numpy | Support numeric calculations |
| scipy.stats | Perform Pearson correlation analysis |
| matplotlib | Create standard plots |
| seaborn | Create advanced statistical visualizations |
| scikit-learn | Machine learning analysis (Decision Tree Regressor) |
| sys/os (optional) | Standard module utilities |

---

# Visualizations Produced

- Bar Chart: Top 10 Countries by Average AQI
- Bar Chart: Correlation of Pollutants with Overall AQI
- Bar Chart: Top 10 Polluted Cities (Average AQI)
- Stacked Bar Chart: Pollutant Contribution Breakdown for Top 10 Countries
- Table: Feature Importance from Decision Tree Regressor

---

# Project Reflection

- Code is cleanly structured, commented, and easy to read.
- Variable names consistently use snake_case.
- Each section of the project builds logically: import, clean, analyze, visualize, model.
- Data science concepts were correctly applied to answer research questions.
- Machine learning modeling extended the analysis for deeper insights.

---

# Project Limitations

When trying to visualize the Top 10 most polluted cities, it was found that many cities had the maximum AQI value of 500. As a result, the bar chart did not show meaningful variations between cities; the bars were fully colored and indistinguishable. Expanding the analysis to the Top 50 cities showed the same issue. This heavy concentration at maximum AQI values limited the ability to accurately rank or differentiate cities based on air quality, affecting the usefulness of the city-based visualizations.
