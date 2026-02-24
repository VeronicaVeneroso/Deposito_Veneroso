import numpy as np

arr = np.linspace(0,1,5)
print(arr)

# Matrice 3x3 con valori casuali uniformi tra 0 e 1
random_arr = np.random.rand(3,3)
print(random_arr)

arr2 = np.array([1,2,3,4,5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print("Sum: ", sum_value)
print("Mean: ", mean_value)
print("Standard Deviation: ", std_value)