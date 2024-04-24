import matplotlib.pyplot as plt
import numpy as np



def bubble_sort(arr, ax):
    n = len(arr)
    pic_count = 0
    for i in range(n - 1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                pic_count = pic_count + 1 
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
                # Updates the plot every iteration
                ax.clear()
                
                # Colors the 2 comparing indexs yellow and the rest green 
                colors = ['green'] * len(arr)
                yellow_i = [j,j+1]
                for i in yellow_i:
                    colors[i] = 'yellow'
                
                # Plots
                ax.bar(range(len(arr)), arr, color=colors, edgecolor = 'black')
                plt.xlabel('Index')
                plt.ylabel('Value')
                plt.pause(0.001)  # lower the pause = faster animation 
                plt.savefig(f'IMAGES/{pic_count}.png')  # Save as PNG
                
 
# Generate random data for sorting
data = np.random.randint(1, 10, size = 25)

fig, ax = plt.subplots()
bubble_sort(data, ax)
plt.show()
