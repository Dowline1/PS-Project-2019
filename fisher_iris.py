# Eoin Dowling
# 01 Apr 2019
# This will be my main file for doing calculations for Project 2019 of Programming & Scripting.

# Importing Pandas module to python for calculations and importing of csv file with data.
# Importing numpy and matplotlib for plots and graphs
# Importing seaborn to get all species on one graph for stacking
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sbn

# Reads in the Iris Dataset into python.
# Code adapted from: https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
df = pd.read_csv (r'fisher_iris_dataset.csv')

# Mean by Species code adapted from: https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
mean_by_species = round(df.groupby(['species']).mean(),3)
overall_mean = round(df[['sepal_length','sepal_width','petal_length','petal_width']].mean(),3)

# Using code as above for calculating median
median_by_species = round(df.groupby(['species']).median(),3)
overall_median = round(df[['sepal_length','sepal_width','petal_length','petal_width']].median(),3)

# Save data generated to csv by pandas for mean of species adapted from code in:https://chrisalbon.com/python/data_wrangling/pandas_saving_dataframe_as_csv/
# Initially attempted to import module to convert csv to .md file however could not get to work: csv2md module
# Used following website to convert csv to .md: https://donatstudios.com/CsvToMarkdownTable
mean_by_species.to_csv('mean_by_species.csv')
overall_mean.to_csv('overall_mean.csv')
median_by_species.to_csv('median_by_species.csv')
overall_median.to_csv('overall_median.csv')

# Seaborn graphs adapting code from: http://python-graph-gallery.com/histogram/
sbn.distplot(df.sepal_length, color='blue',label='Sepal Length')
sbn.distplot(df.sepal_width, color='orange',label='Sepal Width')
plt.legend()
plt.savefig('sepal_width_sepal_length_comparison.png')

# Code for graphs adapted from: https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html 
df.hist(bins=10)
plt.savefig('Overall_Histogram.png')
df.hist(column='sepal_length',stacked=True,bins=10,by='species')
plt.savefig('sepal_length_Histogram.png')
df.hist(column='sepal_width',bins=10)
plt.savefig('sepal_width_Histogram.png')
df.hist(column='petal_length',bins=10)
plt.savefig('petal_length_Histogram.png')
df.hist(column='petal_width',bins=10)
plt.savefig('petal_width_Histogram.png')
