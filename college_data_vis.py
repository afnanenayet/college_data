# college_data_vis.py   Afnan Enayet
# 2017
# A Python script that utilizes the gleam library (which utilizes other
# libraries such as Flask and ggplot to help easily create pages that
# allow easy data visualization

# TODO:
#  - load data from csv into pandas dataframe
#  - visualize it

DATA_FP = "./data/college_data.csv"

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# constants
DATA_FP = "./data/college_data.csv"
x_col = "ADM_RATE_ALL"
y_col = "SAT_AVG_ALL"
fields = [x_col, y_col]

sns.set_context("poster")
sns.set_style('ticks')

# setup
# load data into pandas dataframe
df = pd.read_csv(DATA_FP, usecols=fields, dtype=
                 {
                     "ADM_RATE_ALL": "f", 
                     "SAT_AVG_ALL": "f"
                 }
)

# Create scatterplot of dataframe
fig = sns.lmplot(x_col, # Horizontal axis
                 y_col, # Vertical axis
                 data=df, # Data source
                 fit_reg=False, # fix a regression line
                 scatter_kws={"marker": "D", # Set marker style
                              "s": 10}) # S marker size

# Set title
plt.title('Admittance rate versus SAT scores')

# Set x-axis label
plt.xlabel('Admittance rate')

# Set y-axis label
plt.ylabel('Average SAT score')

plt.savefig("sat_vs_admit.svg", format="svg")
plt.show()

