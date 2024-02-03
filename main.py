import pandas as pd
from scipy.stats import shapiro, mannwhitneyu

# STEP 1: Load the data into Python environment
df = pd.read_excel('Data/spor_salonu_uyelik_veriseti.xlsx')  # Ensure the file name matches your dataset

# STEP 2: Examine the averages for the target groups (Standard Membership & Premium Membership)
# Satisfaction Score Averages
satisfaction_avg = df.groupby('Uyelik_Paketi')['Memnuniyet_Puani'].mean()
print("Satisfaction Score Averages:\n", satisfaction_avg)

# Attendance Frequency Averages
attendance_avg = df.groupby('Uyelik_Paketi')['Katilim_Sikligi'].mean()
print("Attendance Frequency Averages:\n", attendance_avg)

# STEP 3: Parametric or Non-Parametric (Assumption Checking)

# STEP 3.1: Normality Assumption (Shapiro-Wilk Test)
# For Standard Package - Satisfaction Score
stat, p = shapiro(df[df['Uyelik_Paketi'] == 'Standart']['Memnuniyet_Puani'])
print("Standard Package - Satisfaction Score - Shapiro Test: Statistic = {:.4f}, p = {:.4f}".format(stat, p))

# For Premium Package - Satisfaction Score
stat, p = shapiro(df[df['Uyelik_Paketi'] == 'Premium']['Memnuniyet_Puani'])
print("Premium Package - Satisfaction Score - Shapiro Test: Statistic = {:.4f}, p = {:.4f}".format(stat, p))

# STEP 4: Final Test (If assumptions are not met, use Mann-Whitney U Test - Non-parametric Test)
# Mann-Whitney U Test for Satisfaction Scores
u_stat, p_value = mannwhitneyu(df[df['Uyelik_Paketi'] == 'Standart']['Memnuniyet_Puani'],
                               df[df['Uyelik_Paketi'] == 'Premium']['Memnuniyet_Puani'])

print("Mann-Whitney U Test - Satisfaction Scores: U Statistic = {:.4f}, p = {:.4f}".format(u_stat, p_value))

# Interpretation based on p-value
# If p < 0.05, H0 is rejected, indicating a statistically significant difference between the groups.
# If p > 0.05, H0 cannot be rejected, indicating no statistically significant difference between the groups.