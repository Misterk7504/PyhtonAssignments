import numpy as np
import pandas as pd

print("=== NUMPY PROBLEMS ===\n")

# 1. Array 1 to 20 → 4x5 matrix
arr1 = np.arange(1, 21).reshape(4, 5)
print("1. 4×5 matrix:\n", arr1)

# 2. 10 zeros, replace 5th element with 100
arr2 = np.zeros(10)
arr2[4] = 100
print("\n2. Zeros array (5th element = 100):", arr2)

# 3. Even numbers from 2 to 40
even_nums = np.arange(2, 41, 2)
print("\n3. Even numbers 2 to 40:", even_nums)

# 4. 15 random integers (1-100) → min, max, mean, std
np.random.seed(42)  # for reproducible results
rand_arr = np.random.randint(1, 101, 15)
print("\n4. Random array:", rand_arr)
print(f"   Min: {rand_arr.min()}, Max: {rand_arr.max()}, Mean: {rand_arr.mean():.2f}, Std: {rand_arr.std():.2f}")

# 5. Profit and profit percentage
sales = np.array([5000, 7500, 8200, 6000, 9000])
costs = np.array([3000, 4500, 5000, 3800, 5500])
profit = sales - costs
profit_pct = (profit / costs) * 100
print("\n5. Profit:", profit)
print("   Profit %:", profit_pct.round(2))

# 6. 6x6 random matrix → row/col/total sums
matrix6 = np.random.randint(1, 50, size=(6,6))
print("\n6. 6×6 Matrix:\n", matrix6)
print("   Row sums:", matrix6.sum(axis=1))
print("   Col sums:", matrix6.sum(axis=0))
print("   Total sum:", matrix6.sum())

# 7. Daily returns from stock prices
prices = np.array([100, 105, 103, 108, 112, 107, 115])
returns = (prices[1:] - prices[:-1]) / prices[:-1] * 100
print("\n7. Daily Returns (%):", returns.round(2))

# 8. Annual → Monthly interest rates
annual_rates = np.array([0.04, 0.06, 0.08, 0.12])
monthly_rates = (1 + annual_rates)**(1/12) - 1
print("\n8. Monthly rates:", monthly_rates.round(5))

# 9. Normalize portfolio weights
weights = np.array([0.4, 0.3, 0.2, 0.25, 0.15])
normalized = weights / weights.sum()
print("\n9. Normalized weights:", normalized.round(4))
print("   Sum →", normalized.sum())

print("\n=== PANDAS PROBLEMS ===\n")

# 10. Pandas Series
data = [1200, 1500, 1800, 2000, 2200]
s = pd.Series(data, index=['A', 'B', 'C', 'D', 'E'])
print("10. Series:\n", s)
print(f"    Mean: {s.mean()}")
print(f"    Max: {s.max()}")
print(f"    Index of max: {s.idxmax()}")

# 11. DataFrame with student marks
df_students = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
    'Math': [85, 92, 78, 96, 88],
    'Science': [90, 87, 85, 91, 93],
    'English': [88, 84, 89, 95, 90]
})

print("\n11. Full DataFrame:\n", df_students)
print("\n    Math column:\n", df_students['Math'])
print("\n    First 2 rows:\n", df_students.head(2))
print("    Shape:", df_students.shape)

# 12. Filtering on Account Balance
df = pd.DataFrame({
    "Account": [101, 102, 103, 104],
    "Balance": [5000, 15000, 7000, 12000]
})

print("\n12. Original DataFrame:\n", df)
print("\n    Balance > 8000:\n", df[df['Balance'] > 8000])
print("\n    Balance between 6000 and 13000:\n", df[df['Balance'].between(6000, 13000)])
