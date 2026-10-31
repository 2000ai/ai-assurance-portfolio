# W9 Day2: DataFrame 基础练习
import pandas as pd

DATA_PATH = "week09/data/sales.csv"

# 读取 CSV
df = pd.read_csv(DATA_PATH)
print("=== 数据读取成功 ===")

# 1. shape
print("\n=== 1. shape（行数, 列数）===")
print(df.shape)
print(f"行数：{df.shape[0]}，列数：{df.shape[1]}")

# 2. columns
print("\n=== 2. columns（列名）===")
print(list(df.columns))

# 3. dtypes
print("\n=== 3. dtypes（每列类型）===")
print(df.dtypes)

# 4. head
print("\n=== 4. head（前 5 行）===")
print(df.head())

# 5. tail
print("\n=== 5. tail（后 5 行）===")
print(df.tail())

# 6. info
print("\n=== 6. info ===")
df.info()

# 7. describe
print("\n=== 7. describe（数值列统计）===")
print(df.describe())

# 8. isna
print("\n=== 8. isna（缺失值统计）===")
print(df.isna().sum())
print(f"总缺失值：{df.isna().sum().sum()}")

# 9. duplicated
print("\n=== 9. duplicated（重复行）===")
dup_count = df.duplicated().sum()
print(f"重复行数：{dup_count}")