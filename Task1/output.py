import joblib
name = input('Enter your name : ')
num = float(input('Enter year of experience : '))
model = joblib.load('marks.pk1')
print()
print('Name               : ' ,name)
print('Year_of_Experience : ', exp)
output = model.predict([[exp]])
print('Salary             : ',output)