#Reshaping your data
#Now that you have all the data combined into a single DataFrame, the next step is to reshape it into a tidy data format.

#Currently, the gapminder DataFrame has a separate column for each year. What you want instead is a single column that contains the year, and a single column that represents the average life expectancy for each year and country. By having year in its own column, you can use it as a predictor variable in a later analysis.

#You can convert the DataFrame into the desired tidy format by melting it.


import pandas as pd

# Melt gapminder: gapminder_melt
gapminder_melt = pd.melt(gapminder,id_vars = 'Life expectancy')

# Rename the columns
gapminder_melt.columns = ['country','year','life_expectancy']

# Print the head of gapminder_melt
print(gapminder_melt.head())

