import pandas as pd

# Load the dataset
data_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
df = pd.read_csv(data_url)

# Display the first few rows of the dataset
print(df.head())

# Basic analysis
print(f"Shape of the dataset: {df.shape}")
print(f"Column names: {df.columns}")

# Data preprocessing
df['date'] = pd.to_datetime(df['date'])  # Convert date to datetime format

# Total cases and deaths
total_cases = df['total_cases'].max()
total_deaths = df['total_deaths'].max()
print(f"Total cases: {total_cases}")
print(f"Total deaths: {total_deaths}")

# Analysis by location
location = 'United States'  # Replace with the location you want to analyze
location_data = df[df['location'] == location]
print(f"Data for {location}:\n{location_data.head()}")

# Plotting
import matplotlib.pyplot as plt

location_data.plot(x='date', y='total_cases', kind='line', title=f'Total COVID-19 cases in {location}')
plt.show()
