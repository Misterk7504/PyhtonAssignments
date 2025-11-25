import numpy as np

# 1. Create an array of numbers from 1 to 20 and reshape it into a 4×5 matrix
arr1 = np.arange(1, 21).reshape(4, 5)
print("1. 4x5 matrix (1 to 20):\n", arr1)
# Output:
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# 2. Create an array of 10 zeros and replace the 5th element with 100
arr2 = np.zeros(10)
arr2[4] = 100  # 5th element (0-based index)
print("\n2. Zeros array with 5th element 100:", arr2)
# [  0.   0.   0.   0. 100.   0.   0.   0.   0.   0.]

# 3. Create a NumPy array of even numbers between 2 and 40
even_arr = np.arange(2, 41, 2)
print("\n3. Even numbers 2 to 40:", even_arr)
# [ 2  4  6 ... 36 38 40]

# 4. Generate a 1D array of 15 random integers between 1 and 100 and find min, max, mean, std
np.random.seed(42)  # for reproducibility
rand_arr = np.random.randint(1, 101, size=15)
print("\n4. Random array:", rand_arr)
print("   Min:", rand_arr.min())
print("   Max:", rand_arr.max())
print("   Mean:", rand_arr.mean())
print("   Std Dev:", rand_arr.std())

# 5. Given two arrays of sales and costs, calculate profit and profit percentage
sales = np.array([5000, 7500, 8200, 6000, 9000])
costs = np.array([3000, 4500, 5000, 3800, 5500])

profit = sales - costs
profit_percentage = (profit / costs) * 100

print("\n5. Sales:", sales)
print("   Costs:", costs)
print("   Profit:", profit)
print("   Profit %:", profit_percentage.round(2))

# 6. Create a 6x6 random matrix and compute row sums, column sums, and total sum
np.random.seed(10)
matrix6 = np.random.randint(1, 20, size=(6, 6))
print("\n6. 6x6 Random Matrix:\n", matrix6)

row_sums = matrix6.sum(axis=1)
col_sums = matrix6.sum(axis=0)
total_sum = matrix6.sum()

print("   Row sums:", row_sums)
print("   Column sums:", col_sums)
print("   Total sum:", total_sum)

# 7. Given stock prices, compute daily returns using vectorized operations
prices = np.array([100, 102, 98, 105, 107, 103, 110])
daily_returns = (prices[1:] - prices[:-1]) / prices[:-1]
print("\n7. Stock Prices:", prices)
print("   Daily Returns (%):", (daily_returns * 100).round(2))

# 8. Convert annual interest rates to monthly rates using vectorization
annual_rates = np.array([0.03, 0.05, 0.07, 0.12])  # 3%, 5%, 7%, 12%
monthly_rates = (1 + annual_rates) ** (1/12) - 1
print("\n8. Annual rates:", annual_rates)
print("   Monthly rates:", monthly_rates.round(6))

# 9. Normalize portfolio weights so that they sum to 1
weights = np.array([0.2, 0.3, 0.15, 0.25, 0.1])
normalized_weights = weights / weights.sum()
print("\n9. Original weights:", weights)
print("   Normalized weights (sum=1):", normalized_weights.round(4))
print("   Sum check:", normalized_weights.sum())