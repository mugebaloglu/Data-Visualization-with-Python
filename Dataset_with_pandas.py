import numpy as np  
import pandas as pd 

df_can = pd.read_excel(
    'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Canada.xlsx',
    sheet_name='Canada by Citizenship',
    skiprows=range(20),
    skipfooter=2)

print('Data read into a pandas dataframe!')
print(df_can.head())

#This method can be used to get a short summary of the dataframe.
df_can.info(verbose=False)


df_can.columns
df_can.index
print(type(df_can.columns))
print(type(df_can.index))

#To get the index and columns as lists, we can use the tolist() method.

df_can.columns.tolist()
df_can.index.tolist()
print(type(df_can.columns.tolist()))
print(type(df_can.index.tolist()))

df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)


df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
df_can.columns
print(df_can.head(2))


df_can[['Country', 1980, 1981, 1982, 1983, 1984, 1985]]

df_can.set_index('Country', inplace=True)
print(df_can.head(3))
df_can.index.name = None

#Example: Let's view the number of immigrants from Japan for the following scenarios: 1. The full row data (all columns) 2. For year 2013 3. For years 1980 to 1985.

# 1. the full row data (all columns)
df_can.loc['Japan']
#or
df_can[df_can.index == 'Japan']

# 2. for year 2013
df_can.loc['Japan', 2013]

# 3. for years 1980 to 1985
df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1984]]



