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
df = pd.read_csv (r'files/fisher_iris_dataset.csv')

# Filtering so that species can be placed on same histogram for species comparison code adapted from: https://pythonspot.com/pandas-filter/
df_setosa = df[df.species == 'setosa']
df_versicolor = df[df.species == 'versicolor']
df_virginica = df[df.species == 'virginica']

# Mean by Species code adapted from: https://datatofish.com/use-pandas-to-calculate-stats-from-an-imported-csv-file/
mean_by_species = round(df.groupby(['species']).mean(),3)
overall_mean = round(df[['sepal_length','sepal_width','petal_length','petal_width']].mean(),3)

# Using code as above for calculating median
median_by_species = round(df.groupby(['species']).median(),3)
overall_median = round(df[['sepal_length','sepal_width','petal_length','petal_width']].median(),3)

# Save data generated to csv by pandas for mean of species adapted from code in:https://chrisalbon.com/python/data_wrangling/pandas_saving_dataframe_as_csv/
# Initially attempted to import module to convert csv to .md file however could not get to work: csv2md module
# Used following website to convert csv to .md: https://donatstudios.com/CsvToMarkdownTable
mean_by_species.to_csv('files/mean_by_species.csv')
overall_mean.to_csv('files/overall_mean.csv')
median_by_species.to_csv('files/median_by_species.csv')
overall_median.to_csv('files/overall_median.csv')

# Colors SL=Blue, SW=Orange, PL=Cyan, PW=Crimson
# Color codes taken from: https://matplotlib.org/examples/color/named_colors.html
# Seaborn graphs adapting code from: http://python-graph-gallery.com/histogram/
sbn.distplot(df.sepal_length, color='blue',label='Sepal Length')
sbn.distplot(df.sepal_width, color='orange',label='Sepal Width')
plt.legend()
plt.savefig('images/histogram_sepal_width_sepal_length_comparison.png')

# Needed to clear plot for next plot
plt.cla()

sbn.distplot(df.petal_length, color='cyan',label='Petal Length')
sbn.distplot(df.petal_width, color='crimson',label='Petal Width')
plt.legend()
plt.savefig('images/histogram_petal_width_petal_length_comparison.png')

# Plotting Histogram by species
plt.cla()

# Sepal length comparison
sbn.distplot(df_setosa.sepal_length, color='magenta',label='Setosa')
sbn.distplot(df_versicolor.sepal_length, color='g',label='Versicolor')
sbn.distplot(df_virginica.sepal_length, color='aqua',label='Virginica')
plt.legend()
plt.savefig('images/histogram_sepal_length_species_comparison')

plt.cla()

# Sepal width comparison
sbn.distplot(df_setosa.sepal_width, color='magenta',label='Setosa')
sbn.distplot(df_versicolor.sepal_width, color='g',label='Versicolor')
sbn.distplot(df_virginica.sepal_width, color='aqua',label='Virginica')
plt.legend()
plt.savefig('images/histogram_sepal_width_species_comparison')

plt.cla()

# Petal length comparison
sbn.distplot(df_setosa.petal_length, color='magenta',label='Setosa')
sbn.distplot(df_versicolor.petal_length, color='g',label='Versicolor')
sbn.distplot(df_virginica.petal_length, color='aqua',label='Virginica')
plt.legend()
plt.savefig('images/histogram_petal_length_species_comparison')

plt.cla()

# Petal width comparison
sbn.distplot(df_setosa.petal_width, color='magenta',label='Setosa')
sbn.distplot(df_versicolor.petal_width, color='g',label='Versicolor')
sbn.distplot(df_virginica.petal_width, color='aqua',label='Virginica')
plt.legend()
plt.savefig('images/histogram_petal_width_species_comparison')


# Code to create scatterplot adapted from: http://python-graph-gallery.com/scatter-plot/
sbn.lmplot( x='sepal_length', y='sepal_width', data=df, fit_reg=False, hue='species', legend=False)
plt.legend(loc='upper right')
plt.savefig('images/sepal_length_sepal_width_scatter.png')

sbn.lmplot( x='petal_length', y='petal_width', data=df, fit_reg=False, hue='species', legend=False)
plt.legend(loc='lower right')
plt.savefig('images/petal_length_petal_width_scatter.png')

plt.cla()

# Pallete for box plots
my_pal = {"versicolor": "g", "setosa": "magenta", "virginica":"aqua"}

# Code to creat Box Plot Graphs adapted from: https://python-graph-gallery.com/33-control-colors-of-boxplot-seaborn/
# Sepal Length
sbn.boxplot( x=df["species"], y=df["sepal_length"], palette=my_pal)
plt.legend()
plt.savefig('images/boxplot_sepal_length_species_comparison')

plt.cla()

# Sepal Width
sbn.boxplot( x=df["species"], y=df["sepal_width"], palette=my_pal)
plt.legend()
plt.savefig('images/boxplot_sepal_width_species_comparison')

plt.cla()

# Petal Length
sbn.boxplot( x=df["species"], y=df["petal_length"], palette=my_pal)
plt.legend()
plt.savefig('images/boxplot_petal_length_species_comparison')

plt.cla()

# Petal Width
sbn.boxplot( x=df["species"], y=df["petal_width"], palette=my_pal)
plt.legend()
plt.savefig('images/boxplot_petal_width_species_comparison')

plt.cla()

# Code to create violin plot graphs adapted from: https://python-graph-gallery.com/53-control-color-of-seaborn-violinplot/
# Sepal Length
sbn.violinplot( x=df["species"], y=df["sepal_length"], palette=my_pal)
plt.legend()
plt.savefig('images/violinplot_sepal_length_species_comparison')

plt.cla()

# Sepal Width
sbn.violinplot( x=df["species"], y=df["sepal_width"], palette=my_pal)
plt.legend()
plt.savefig('images/violinplot_sepal_width_species_comparison')

plt.cla()

# Petal Length
sbn.violinplot( x=df["species"], y=df["petal_length"], palette=my_pal)
plt.legend()
plt.savefig('images/violinplot_petal_length_species_comparison')

plt.cla()

# Petal Width
sbn.violinplot( x=df["species"], y=df["petal_width"], palette=my_pal)
plt.legend()
plt.savefig('images/violinplot_petal_width_species_comparison')

plt.cla()

# Code for graphs adapted from: https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html 
df.hist(bins=10)
plt.savefig('images/overall_histogram_trellis.png')

df.hist(column='sepal_length',stacked=True,bins=10,by='species')
plt.savefig('images/species_histogram_sepal_length_trellis.png')

df.hist(column='sepal_width',stacked=True,bins=10,by='species')
plt.savefig('images/species_histogram_sepal_width_trellis.png')

df.hist(column='petal_length',stacked=True, bins=10,by='species' )
plt.savefig('images/species_histogram_petal_length_trellis.png')

df.hist(column='petal_width',stacked=True,bins=10,by='species')
plt.savefig('images/species_histogram_petal_width_trellis.png')
