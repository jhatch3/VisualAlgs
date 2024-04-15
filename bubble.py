import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

def bubble_sort(arr, ax):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                # Updates the plot every iteration
                ax.clear()
                ax.bar(range(len(arr)), arr, color='black')
                plt.pause(0.0001)  
                
# Generate random data for sorting
data = np.random.randint(1, 10, size = 25)

fig, ax = plt.subplots()
bubble_sort(data, ax)
plt.show()
