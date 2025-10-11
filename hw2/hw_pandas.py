import numpy as np
import pandas as pd

# Q1
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
every_20th = df.loc[::20, ['Manufacturer', 'Model', 'Type']]
print(every_20th.head(10))

# Q2
for col in ['Min.Price', 'Max.Price']:
    df[col] = df[col].fillna(df[col].mean())

print(df[['Min.Price', 'Max.Price']].isna().sum().to_string())

# Q3
np.random.seed(0)
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_gt_100 = df[df.sum(axis=1) > 100]
print("Original shape:", df.shape, "-> Filtered shape:", rows_gt_100.shape)
print(rows_gt_100.to_string(index=False))
