#Many-to-1 data merge
#In a many-to-one (or one-to-many) merge, one of the values will be duplicated and recycled in the output. That is, one of the keys in the merge is not unique.

#Here, the two DataFrames site and visited have been pre-loaded once again. Note that this time, visited has multiple entries for the site column. Confirm this by exploring it in the IPython Shell.

#The .merge() method call is the same as the 1-to-1 merge from the previous exercise, but the data and output will be different.


# Merge the DataFrames: m2o
m2o = pd.merge(left =site ,right =visited , left_on ='name' , right_on ='site' )

# Print m2o
print(m2o)
