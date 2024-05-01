import matplotlib.pyplot as plt
import numpy as np


def reverse(arr, ax):
    high = len(arr) - 1
    low = 0
    pic_count = 0 
    while (low < high):
        # Colors the 2 comparing indexs yellow and the rest green 
        colors = ['green'] * len(arr)
        yellow_i = [low, high]
        for i in yellow_i:
            colors[i] = 'yellow'
        # plot
        ax.bar(range(len(arr)), arr, color=colors, edgecolor = 'black')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.pause(0.001)  # lower the pause = faster animation 
        plt.savefig(f'reverse_frams/{pic_count}.png')  # Save as PNG
        
        # Actual Reversing
        temp = arr[low]
        arr[low] = arr[high]
        arr[high] = temp
        
        pic_count = pic_count + 1
        low = low + 1
        high = high - 1
        # Updates the plot every iteration
        ax.clear()
        
 
        
    ax.bar(range(len(arr)), arr, color=colors, edgecolor = 'black')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.pause(0.001)  
    plt.savefig(f'reverse_frams/{pic_count}.png') 
    
 

data = []
for i in range(1,25):
    data.append(i)

print(data)
fig, ax = plt.subplots()
reverse(data, ax)
plt.show()
