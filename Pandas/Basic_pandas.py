'''You can also pass in a dictionary to a dataframe where each key is a column name and each value in a list 
is the column value. For instance, take a look at the code below:'''

import pandas as pd

df1 = pd.DataFrame(
    {
    'name': ['Smith', 'Jane', 'Joe'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
}
)


'''Example:

We're going to create a DataFrame consisting of data based on clothing with product-ID its name and color.'''


df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name':['t-shirt','t-shirt','skirt','skirt'],
  'Color': ['blue', 'green', 'red','black']
  
})

print(df1)

print('***************************************************************************')

'''We can also use lists to add data in DataFrame.
You can enter a list of lists, each representing a row of data. To pass a list of column names, use the keyword columns.'''


df2 = pd.DataFrame(
    [ [1, 'Indore', 100], [2, 'Bangalore', 120], [3, 'Hyderabad', 90], [4, 'Mumbai', 115] ],
  columns=['ID', 'Location', 'Number of Employees']
  )

print(df2)


# Loading Data from CSV

df3 = pd.read_csv('loan_data_2015.csv')
print(df3)


print('***************************************************************************')


print("Inspecting a DataFrame")
print('***************************************************************************')

df3.head(10)
df3.info()