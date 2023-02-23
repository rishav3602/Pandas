import pandas as pd
import openpyxl
data = pd.read_csv("addresses.csv")  #will read the csv file
# print(data)  #will throw entire file in output
# print(type(data))   #type is data frame
# print(data.head())   #will give first five data of the file
# print(data.head(8))   #will give first 8 records of the file
# print(data.tail())   #will throw last five records
# print(data.tail(10))   #will throw last 10 records
# print(data.columns)    #will show all the columns available in the data set
# print(list(data.columns))  #will throw the columns in a list formats
# print(data["state_province"]) #will show all the records available in this column
# print(type(data["state_province"])) #single column data type will be series.
# print(type(data[["state_province"]])) #single column put in a list form will throw dataframe type
# print(data[["city","location_id"]]) #will throw data in both the column
#for getting the records of multiple column put need to pass them in the form of a list.

data1 = pd.read_excel("airline.xls")   #will read the excel file
data2 = pd.read_excel("airline.xls" , sheet_name="Sheet2")  #will read only sheet2 of the excel file 
#sheet_name= parameter is set to read the particular sheet
# print(data1)
data1.to_csv('test1.csv' , index = False) #will convert records into csv file
data3 = pd.read_csv("test1.csv")  
# print(data3)
data3.to_excel("test2.xlsx") #will convert the records to xl file
print(data1.columns)


