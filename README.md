# PANDAS
# 🌦️ Pandas Weather Analysis

This project is a hands-on exploration of the **Pandas** library using the `seattle-weather.csv` dataset. It covers essential operations like reading CSVs, indexing, slicing, column access, descriptive statistics, and more — all geared toward building foundational skills in data analysis.

---

## 🧪 What’s Inside

- Read and explore real-world weather data
- Use conditional filtering (e.g., find rainy days)
- Create DataFrames from Python dictionaries
- Explore rows and columns using `head()`, `tail()`, and slicing
- Access and display specific columns using dot and bracket notation
- Descriptive statistics using `.describe()`
- Index manipulation with `.set_index()` and `.reset_index()`

---

## 📁 Files Included

- `pandas_basics.py`: Main script with code demonstrating core Pandas features
- `seattle-weather.csv`: Weather dataset used in the analysis
- `README.md`: You’re reading it!

---

## 🔍 Example Code Snippets

```python
import pandas as pd

# Load dataset
d = pd.read_csv("seattle-weather.csv")

# Print first few rows
print(d.head())

# Filter: Dates when weather was 'rain'
print(d['date'][d['weather'] == 'rain'])

# Set index to 'date' column
d.set_index('date', inplace=True)
print(d.loc['2015-12-31'])
```
📊 Dataset Info
File: seattle-weather.csv

Columns: date, precipitation, temp_max, temp_min, wind, weather

Source: Public Seattle Weather Data

💡 Requirements
Python 3.x

Pandas
```bash
Install dependencies:
pip install pandas
🚀 How to Run
python pandas_basics.py
```
📌 Why This Project?
Understanding real-world datasets with Pandas is a must-have skill for any aspiring data scientist or AI engineer. This project helps build that comfort by applying Pandas features directly to usable weather data.

Screenshots:
![p1](https://github.com/user-attachments/assets/e8ced3e5-1d09-4611-bf99-30595168d144)
![p2](https://github.com/user-attachments/assets/8f832a93-a40d-42ba-a9ab-30fd7ddf2720)
![p3](https://github.com/user-attachments/assets/c98dcaeb-3f25-4e0d-a0a1-18182622f9db)
![p4](https://github.com/user-attachments/assets/5d782ceb-7b49-42ea-8559-5567ee9ce6fe)
![p5](https://github.com/user-attachments/assets/70791e98-0a78-4425-9714-674fbdafd8b5)
![p6](https://github.com/user-attachments/assets/1862304a-e075-4daa-ac2a-769ec902bc42)
![p7](https://github.com/user-attachments/assets/c061a539-c02c-4185-8d83-a39894d50203)
![p8](https://github.com/user-attachments/assets/0a29fd70-9d42-470c-9eb4-b06ea0128019)
![pandas](https://github.com/user-attachments/assets/ff740830-44da-41be-a8df-07e08392f458)






