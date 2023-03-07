import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
# print(data)

#1Filter the number of data where no one survive and sex is male
print(data['Survived']==0)
print(data[data['Survived']==0])
print(data[(data['Survived']==0) & (data['Sex']== 'male')])
print(data[(data['Survived']==0) & (data['Sex']== 'male')].count())
print(len(data[(data['Survived']==0) & (data['Sex']== 'male')]))

##2Filter the number of female who have died
print(len(data[(data['Survived']==0) & (data['Sex']== 'female')]))

##3filter out the number of male and female
print(len(data[data['Sex']== 'female']))
print(len(data[data['Sex']== 'male']))
print(data['Sex'].value_counts())

##3Filter the number of male and females survived
print(len(data[(data['Survived']==1) & (data['Sex']== 'male')]))
print(len(data[(data['Survived']==1) & (data['Sex']== 'female')]))

##4Filter the name of the person who have paid the highest fare
print(data['Fare'])
print(data['Fare'].describe())
print(data['Fare']== 512.329200)
print(data[data['Fare']== 512.329200])
print(data[data['Fare']== 512.329200]['Name'])
print(data[data['Fare']== 512.329200][['Name']])

##5People paying the highest fare survive or died
print(len(data[data['Fare']== 512.329200]))
print(len(data[(data['Fare']== 512.329200)& data['Survived']==1]))

#6 Filter those people who have recived cabin 
print(data['Cabin'].isnull()==False)
print(data[data['Cabin'].isnull()==False])
print(len(data[data['Cabin'].isnull()==False]))