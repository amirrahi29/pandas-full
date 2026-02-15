#head() tail()
#head() 5
#tail(n) 5

import pandas as pd

df = pd.read_csv("data/demo.csv", encoding="latin1")

print("Display 10 rows of first")
print(df.head(10))

print("Display 10 rows of last")
print(df.tail(10))

