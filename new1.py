import pandas as pd
data = pd.read_csv('dataf.csv.csv')
f =  data[data['Wind Speed_km/h']==4]   # find the details according to our need 

fi = data[data['Rel Hum_%']==67] # same as above accordingly our need

firs = data.groupby('Weather').get_group('Fog') # find the details accordingly group

first =data['Weather'].value_counts() # find the value of each coulumn counts  data by column name

fifth = data.rename(columns={'Weather':'Weather condition'}) # change the column name in the data 

sixth = data.Visibility_km.mean() # find the mean of visibility 

seventh =  data.Press_kPa.std() # find the mean of standard deviation

ninth = data[data.Weather_condition.str.contains('Snow')] # find the data in weather condition which contains snow related (full or partial match   )

tenth =  data[(data['Wind Speed_km/h']>24) & (data['Visibility_km']==25)] # find the data where wind speed is >24 and visibility is == 25 . two condittion at the same time
eleventh = data[(data['Press_kPa']>101) & (data['Weather_condition']=='Mostly Cloudy') & (data['Dew Point Temp_C']> -15)] # same as above
sixteen = data[(data['Weather_condition']=='Clear') & (data['Rel Hum_%']>50) | (data['Visibility_km']>40)] # and or used

twelve = data.groupby('Weather_condition').mean() # mean value against weather condition for each column(avg of every column)
thirteen = data.groupby('Weather_condition').max() # find the max againt weathercondition

tenth = data[data['County'].isin(['Bibb','Baldwin'])] # .isin function is use to find the example-cities in a district

eleventh = data[~(data['TotalPop'] >20000)] #delete the population which is greater than 20000 . we use ~ sign

twelve = data['Employed'].fillna(data['Employed'].mean()) # will use to fill na column with the help of mean

thirtheen  = data['FamilyWork'] = data['FamilyWork'].apply(lambda x:x+3) # will increase x values by 3 

