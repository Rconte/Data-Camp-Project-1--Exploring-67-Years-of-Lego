#The Rebrickable database includes data on every LEGO set that ever been sold; 
#the names of the sets, what bricks they contain, what color the bricks are, etc.
#It might be small bricks, but this is big data! In this project, you will get to explore the Rebrickable database. 
#To do this you need to know your way around pandas dataframes and it's recommended that you take a look at the courses pandas Foundations
#and Manipulating DataFrames with pandas.


#1. Introduction
 
#Everyone loves Lego (unless you ever stepped on one). 
#Did you know by the way that "Lego" was derived from the Danish phrase leg godt, which means "play well"? 
#Unless you speak Danish, probably not.
#In this project, we will analyze a fascinating dataset on every single lego block that has ever been built!

#2. Reading Data
#A comprehensive database of lego blocks is provided by Rebrickable.
# Import Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Read colors data

colors = pd.read_csv('datasets/colors.csv')

# Print the first few rows

colors.head()

#3. Exploring Colors
#Now that we have read the colors data, we can start exploring it! Let us start by understanding the number of colors available.

num_colors = colors.rgb.count() 

# How many distinct colors are available?
#I was trying another way to find distinct number of colors thinking 
#there might be doubles or triples in the list, but a print(colors.count()) 
#works just fine since the DataFrame contains distinct colors (135)

print('PRINT CHECK: There are' ,num_colors, 'Distinct colors') 

#4. Transparent Colors in Lego Sets
#The colors data has a column named is_trans that indicates whether a color is transparent or not. 
#It would be interesting to explore the distribution of transparent vs. non-transparent colors.
# colors_summary: Distribution of colors based on transparency

colors_summary = colors.groupby('is_trans').count()
print(colors_summary)

#5. Explore Lego Sets
#Another interesting dataset available in this database is the sets data. 
#It contains a comprehensive list of sets over the years and the number of parts that each of these sets contained.

%matplotlib inline
# Read sets data as `sets`
sets = pd.read_csv('datasets/sets.csv')
sets = pd.DataFrame(sets)
sets.head() # prints first few lines, just to check if everything is alright
# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year = sets[['year', 'num_parts']].groupby('year').mean()
parts_by_year.head()
# Plot trends in average number of parts by year


parts_by_year.plot()
plt.clf()
plt.show()

#6. Lego Themes Over Years
#Lego blocks ship under multiple themes. 
#Let us try to get a sense of how the number of themes shipped has varied over the years.
# themes_by_year: Number of themes shipped by year

themes_by_year = sets[['year', 'theme_id']].groupby('year',as_index = False).agg({'theme_id':pd.Series.nunique})
themes_by_year.head()
