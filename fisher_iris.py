# Eoin Dowling
# 01 Apr 2019
# This will be my main file for doing calculations for Project 2019 of Programming & Scripting.

# Importing Pandas module to python for calculations and importing of csv file with data.
import pandas as pd

# Reads in the Iris Dataset into python.
# Code adapted from: https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
df = pd.read_csv (r'fisher_iris_dataset.csv')

# Caluclations below adapted from: https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/ 
sl_overall_mean = round(df['sepal_length'].mean(),3)
sw_overall_mean = round(df['sepal_width'].mean(),3)
pl_overall_mean = round(df['petal_length'].mean(),3)
pw_overall_mean = round(df['petal_width'].mean(),3)


# Print Results of Calculations
print ('Overall mean of Sepal Length is around',sl_overall_mean,)
print ('Overall mean of Sepal Width is around',sw_overall_mean,)
print ('Overall mean of Petal Length is around',pl_overall_mean,)
print ('Overall mean of Petal Width is around',pw_overall_mean,)