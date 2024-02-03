# FitnessMembershipSatisfactionAnalysis


This project analyzes the effectiveness of two Fitness membership packages, Standard and Premium, on members' satisfaction and attendance frequency using a dataset in Excel format.

## Steps in Analysis

### STEP 1: Load Data
The dataset is loaded into a Python environment using pandas. Ensure the file path matches your dataset location.

```python
import pandas as pd
df = pd.read_excel('Data/spor_salonu_uyelik_veriseti.xlsx')
```

### STEP 2: Examine Averages
Calculate and examine the averages for Satisfaction Score and Attendance Frequency for both membership types.

```python
satisfaction_avg = df.groupby('Uyelik_Paketi')['Memnuniyet_Puani'].mean()
attendance_avg = df.groupby('Uyelik_Paketi')['Katilim_Sikligi'].mean()
```

### STEP 3: Assumption Checking
Determine if the data meets the assumptions for parametric testing.

#### STEP 3.1: Normality Assumption
Use the Shapiro-Wilk test to check for normal distribution of Satisfaction Scores for each package.

```python
from scipy.stats import shapiro
stat, p = shapiro(df[df['Uyelik_Paketi'] == 'Standart']['Memnuniyet_Puani'])
```

### STEP 4: Final Test
If assumptions are not met, use the Mann-Whitney U Test, a non-parametric test, to compare the satisfaction scores between the two packages.

```python
from scipy.stats import mannwhitneyu
u_stat, p_value = mannwhitneyu(df[df['Uyelik_Paketi'] == 'Standart']['Memnuniyet_Puani'],
                               df[df['Uyelik_Paketi'] == 'Premium']['Memnuniyet_Puani'])
```

## Interpretation
- If p < 0.05, H0 is rejected, indicating a statistically significant difference.
- If p > 0.05, H0 cannot be rejected, indicating no statistically significant difference.

## Requirements
- Python 3.11
- Pandas
- SciPy

## Dataset
The dataset should contain the following columns: `Uyelik_Paketi`, `Memnuniyet_Puani`, and `Katilim_Sikligi`.

## Usage
1. Ensure the dataset file is in the specified path.
2. Run the Python script to perform the analysis.
