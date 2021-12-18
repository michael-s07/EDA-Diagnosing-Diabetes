#import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data =pd.read_csv('diabetes.csv')
print(diabetes_data.head())
#Number of columns in the dataframe
print(len(diabetes_data.columns))
#Number of rows in the diabetes data
print(len(diabetes_data))

#mising data in the data frame
print(diabetes_data.isnull().sum())

#Summary Statistics 
print(diabetes_data.describe())

#Working on the Missing values 
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)
print(diabetes_data.isnull().sum())

print(diabetes_data[diabetes_data.isnull().any(axis=1)])

#datatypes of each column
print(diabetes_data.dtypes)

#Convecting the datatypes on Outcome to int
print(diabetes_data.Outcome.unique())
diabetes_data.Outcome = diabetes_data.Outcome.replace('\D+', '0', regex= True)
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype('int64')
print(diabetes_data.dtypes)

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] =diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(np.nan,np.mean)
print(diabetes_data[diabetes_data.isnull().any(axis=1)])
