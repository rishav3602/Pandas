import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(data)
print(data.dtypes)  #will throw data types of the columns
print(data.info())  #will throw all the info about the given data set.
print(data.describe()) #this will give count mean,25,50,75,max, min,etc info
print(data["Age"].describe()) #describe this particular column
print(data[["Sex","Ticket","Fare"]].describe()) #describe these columns
print(type(data))  #data type is data frame
print(type(data.dtypes))  #data type is data series
print(data.dtypes == "object") #will throw true if the data type of the column is object
print(data.dtypes == "int64") #will throw true if the data type of the column is int
print(data.dtypes[data.dtypes == "object"]) #will throw the columns name where data type is object
print(data.dtypes[data.dtypes == "object"].index) #this is used to return the name of the column in list form
print(data[data.dtypes[data.dtypes == "object"].index]) #will throw all the data belonging to object data type column
print(data[data.dtypes[data.dtypes == "object"].index].describe()) #will give a description of the above code
print(data)
print(data["Survived"])
print(data["Survived"] == 0)
print(data[data["Survived"] == 0])
print(data[data["Survived"] == 0].describe())
print(data[data["Survived"]==0].count()) #will show the count of the records in the particular column
print(len(data[data["Survived"]==0]))   #will show the count of the records in the particular column.




