import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam','Dhanshyam','Aditi','Jagdish','Raj','Simran'],
    "Age": [28,34,22,30,29,40,25,32],
    "Salary": [50000,60000,45000,52000,49000,70000,48000,58000],
    "Performance Score": [85,90,78,92,88,95,80,89]
}

df = pd.DataFrame(data)

print("Employees with salary > 50000")
high_salary = df[df['Salary'] > 50000]
print(high_salary)

# & - and condition
print("Filtering rows salary > 50k & age > 30")
filtered = df[(df['Age']>30) & (df['Salary'] > 50000)]
print(filtered)

# | - or condition
print("Filtering rows age > 35 | performance score > 90")
filtered1 = df[(df['Age']>35) | (df['Performance Score'] > 90)]
print(filtered1)
