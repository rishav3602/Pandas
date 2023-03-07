import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(data)

#iloc - it require by default numbered index system indexes
#loc - it require named indexes

data.drop(0) ##will drop the row temporarily
data = data.drop(0) ##will drop the row permanently
print(data.iloc(0)) ##will throw the row at index 0
print(data.loc[2:5])  ##will fetch the record from 2 to 5 rows
print(data.loc[101:105,['Survived','Pclass']])  ##will fetch survived and pclass row 101-105. 
print(data.loc[3:4,['Fare','Cabin','Embarked']])  
print(data.iloc[[3,4,5],[9,10,11]])
print(data.iloc[0:,[0,2]]) 
print(data.loc[0:,['Pclass','PassengerId']]) 
print(data.loc[[3,5],['PassengerId','Survived','Pclass']])
print(data.iloc[[3,5],[0,1,2]])
print(data[data['Age'] > 35])
print(data[(data['Age'] > 35) & (data['Pclass']==1)])
print(
    
)
