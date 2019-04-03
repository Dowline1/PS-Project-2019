# Eoin Dowling
# 01 Apr 2019
# This will be my main file for doing calculations for Project 2019 of Programming & Scripting.

# Importing Pandas module to python for calculations and importing of csv file with data.
import pandas as pd
import pytablereader as ptr 
import pytablewriter as ptw
import csvtomd 

# Reads in the Iris Dataset into python.
# Code adapted from: https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
df = pd.read_csv (r'fisher_iris_dataset.csv')

# Caluclations below adapted from: https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/ 
# Overall Mean
sl_overall_mean = round(df['sepal_length'].mean(),3)
sw_overall_mean = round(df['sepal_width'].mean(),3)
pl_overall_mean = round(df['petal_length'].mean(),3)
pw_overall_mean = round(df['petal_width'].mean(),3)

# Mean by Species
mean_by_species = df.groupby(['species']).mean()

# Overall Median
sl_overall_median = round(df['sepal_length'].median(),3)
sw_overall_median = round(df['sepal_width'].median(),3)
pl_overall_median = round(df['petal_length'].median(),3)
pw_overall_median = round(df['petal_width'].median(),3)

# Print Results of Calculations
print ('Overall mean of Sepal Length is around',sl_overall_mean,)
print ('Overall mean of Sepal Width is around',sw_overall_mean,)
print ('Overall mean of Petal Length is around',pl_overall_mean,)
print ('Overall mean of Petal Width is around',pw_overall_mean,)

print ('Overall median of Sepal Length is around',sl_overall_median,)
print ('Overall median of Sepal Width is around',sw_overall_median,)
print ('Overall median of Petal Length is around',pl_overall_median,)
print ('Overall median of Petal Width is around',pw_overall_median,)

# Save data fram generate by panas for mean of species adapted from code in:https://chrisalbon.com/python/data_wrangling/pandas_saving_dataframe_as_csv/
mean_by_species.to_csv('mean_by_species.csv')
csvtomd mean_by_species.csv


