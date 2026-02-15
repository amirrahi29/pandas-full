import pandas as pd

#customer data frame
df_customer = pd.DataFrame({
    'CustomerID': [1,2,3],
    'Name': ['Remesh','Suresh','Kalpesh']
})

#order dataframe
df_orders = pd.DataFrame({
    'CustomerID': [1,2,4],
    'OrderAmount': [250,450,350]
})

#merge
#inner join
df_inner_merged = pd.merge(df_customer,df_orders, on='CustomerID', how="inner")
#outer join
df_outer_merged = pd.merge(df_customer,df_orders, on='CustomerID', how="outer")
#left join
df_left_merged = pd.merge(df_customer,df_orders, on='CustomerID', how="left")
#right join
df_right_merged = pd.merge(df_customer,df_orders, on='CustomerID', how="right")

print("Inner Join")
print(df_inner_merged)

print("Outer Join")
print(df_outer_merged)

print("Left Join")
print(df_left_merged)

print("Right Join")
print(df_right_merged)