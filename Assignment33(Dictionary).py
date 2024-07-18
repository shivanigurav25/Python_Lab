#Write a Python program and calculate the mean of the below dictionary.
#test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}



def calculate_mean(dictionary):
    """
    Function to calculate the mean of the values in a dictionary.
    
    Parameters:
    dictionary (dict): A dictionary with values to calculate the mean.

    Returns:
    float: The mean of the values.
    """
    # Initialize the total sum and count of items
    total_sum = 0
    count = 0
    
    # Iterate over the dictionary items
    for key, value in dictionary.items():
        total_sum += value  # Add each value to the total sum
        count += 1          # Increment the count of items
    
    # Calculate the mean
    mean = total_sum / count
    
    return mean

# Example usage
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}
mean_value = calculate_mean(test_dict)
print("Mean of the values:", mean_value)



#Output
#Mean of the values: 6.2







