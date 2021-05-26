import pandas
import joblib
dataset = pandas.read_csv('Salary_Data.csv')
# dataset.columns
y = dataset['Salary']
x = dataset['YearsExperience']
x = x.values
x = x.reshape(-1,1)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x,y)
joblib.dump(model, 'Salary.pk1')