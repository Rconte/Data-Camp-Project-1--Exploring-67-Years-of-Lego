#Thinking about the question at hand
#Since you are given life expectancy level data by country and year, you could ask questions about how much the average life expectancy changes over each year.

#Before continuing, however, it's important to make sure that the following assumptions about the data are true:

#'Life expectancy' is the first column (index 0) of the DataFrame.
#The other columns contain either null or numeric values.
#The numeric values are all greater than or equal to 0.
#There is only one instance of each country.
#You can write a function that you can apply over the entire DataFrame to verify some of these assumptions. Note that spending the time to write such a script will help you when working with other datasets as well.

def check_null_or_valid(row_data):
    """Function that takes a row of data,
    drops all missing values,
    and checks if all remaining values are greater than or equal to 0
    """
    no_na = row_data.dropna()
    numeric = pd.to_numeric(no_na)
    ge0 = numeric >= 0
    return ge0

# Check whether the first column is 'Life expectancy'
assert g1800s.columns[0] == 'Life expectancy'

# Check whether the values in the row are valid
assert g1800s.iloc[:, 1:].apply(check_null_or_valid, axis=1).all().all()

# Check that there is only one instance of each country
assert g1800s['Life expectancy'].value_counts()[0] == 1
