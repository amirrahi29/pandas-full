import pandas as pd

data = {
    "Name": ['Ram','Shyam','Ghanshyam',None,'Aditi','Jagdish','Raj','Simran'],
    "Age": [28,34,22,30,29,40,25,32],
    "Salary": [50000,None,45000,52000,49000,70000,48000,58000],
    "Performance Score": [85,90,78,92,88,None,80,89]
}

df = pd.DataFrame(data)

print(df)

print(df.isnull())
print(df.isnull().sum())