#Compute the median of the flattened NumPy array 
#Input: x_odd = np.array([1, 2, 3, 4, 5, 6, 7])


# importing numpy as library 
import numpy as np

# printing original array
x_odd = np.array([1, 2, 3, 4, 5, 6, 7]) 
print("Printing the Original array:") 
print(x_odd) 
  
# calculating median 
median = np.median(x_odd) 
print("Median of the array is:") 
print(median)



#Output
#Printing the Original array:
#[1 2 3 4 5 6 7]
#Median of the array is:
#4.0
