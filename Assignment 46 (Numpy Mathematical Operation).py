#Calculate the total revenue generated by two product categories in a store 
#Input: 
#category1_revenue = np.array([500, 600, 700, 550])
#category2_revenue = np.array([450, 700, 800, 600])



import numpy as np

# Revenue data for each category
category1_revenue = np.array([500, 600, 700, 550])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate the total revenue
total_revenue = category1_revenue + category2_revenue

# Print the total revenue
print("Total Revenue:", total_revenue)


#Output
#Total Revenue: [ 950 1300 1500 1150]
