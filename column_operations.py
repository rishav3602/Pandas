import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
print(data)


data['new_col'] = "Rishav"  ##will create a new column
data['new_name'] = data['Name']  #will duplicate copy of Name column
data['age_Pclass'] = data['Age'] + data['Pclass']
data.drop('new_col',axis=1) ##will drop this column temprorily
data.drop('new_col',axis=1,inplace=True) ##will drop this column premanentily




