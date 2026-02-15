import pandas as pd

#read data from csv file into a data frame
df = pd.read_csv("data/demo.csv", encoding="latin1")

print(df)