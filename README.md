# Project Overview
This Python project explores global air pollution data to answer the following research questions:

- Which countries have the highest average Air Quality Index (AQI)?
- Which pollutant (PM2.5, CO, NO2, Ozone) is most correlated with poor air quality?
- (Optional) What are the top 10 most polluted cities worldwide?

We used Python data science tools and included all topics covered in INFO-B 211:

- Pandas for data handling
- NumPy for numeric operations
- SciPy for statistical correlation (Pearson correlation)
- Matplotlib for basic data visualization
- Seaborn for enhanced visualization
- Standard Modules (os, sys if needed)

---

# Files

| File | Description |
|:-----|:------------|
| `final_project_code.py` | Main Python script containing all code |
| `global_air_pollution_data.csv` | Air pollution dataset |
| `README.md` | This file - explains the project and code |

---

# How to Run

1. Install the required libraries:
```bash
pip install pandas numpy matplotlib seaborn scipy
```
2. Download the dataset `global_air_pollution_data.csv`.
3. Run the `final_project_code.py` script.

The script will output:
- Bar charts for AQI by country and city
- Correlation plot between pollutants and AQI
- Pollutant contribution breakdown for top 10 worst countries

---

# Project Workflow

## 1. Data Import and Cleaning
- Loaded the CSV file using `pandas.read_csv()`.
- Renamed the mislabeled column (`co_aqi_value\t` to `co_aqi_value`).
- Dropped rows with missing `country_name`.
- Made sure all AQI-related columns are integers.

## 2. Research Question 1 - Country AQI Rankings
- Grouped data by `country_name` and calculated the average AQI.
- Sorted and displayed the Top 10 countries with highest average AQI.
- Used Seaborn barplots for visualization.

## 3. Research Question 2 - Pollutant Correlations
- Calculated Pearson correlation coefficients between:
  - CO AQI, Ozone AQI, NO2 AQI, PM2.5 AQI against Overall AQI.
- Used SciPy's `pearsonr()` function.
- Visualized pollutant correlations using a Seaborn barplot.

## 4. Research Question 3 (Optional) - Top 10 Polluted Cities
- Grouped data by `city_name` to find average AQI.
- Displayed the Top 10 most polluted cities using a Seaborn barplot.

## 5. Deeper Pollutant Analysis
- Focused on the Top 10 countries with the worst AQI.
- Normalized pollutant contributions by row.
- Created stacked bar plots showing pollutant contribution percentages.
- Summed and visualized total pollutant contributions per country.

---

# Libraries Used

| Library | Purpose |
|:--------|:--------|
| pandas | Load, clean, manipulate tabular data |
| numpy | Support numeric calculations |
| scipy.stats | Calculate Pearson correlations |
| matplotlib | Create basic custom plots |
| seaborn | Create advanced statistical graphs |
| sys/os (optional) | Manage file paths and file handling |

---

# Visualizations Produced

- Bar Chart: Top 10 Countries by Average AQI
- Bar Chart: Pollutant-AQI Correlations
- Bar Chart: Top 10 Polluted Cities
- Stacked Bar Chart: Pollutant Contribution in Top 10 Countries
- Grouped Bar Chart: Total Pollutant Contributions

---

# Project Reflection

- Code is fully organized, commented, and easy to follow.
- All variable names are written using snake_case.
- Each major section of the project follows clear and logical steps: import, clean, analyze, visualize.
- All data visualizations support answering the analytical questions.

---

# Project Limitations

During the attempt to visualize the top 10 most polluted cities, it was discovered that all of the top cities had the maximum AQI value of 500. As a result, the bar chart for cities did not show meaningful variation or clear ranking; it appeared fully colored without distinction. Even when expanding the analysis to the top 50 cities, many still displayed the maximum AQI of 500. Despite different attempts to refine the data, the overwhelming number of cities hitting the maximum AQI limit caused challenges in accurately determining the top
