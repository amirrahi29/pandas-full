import pandas as pd

df = pd.read_csv("data/demo.csv", encoding="latin1")

print("Displaying the info of data set")
print(df.info())