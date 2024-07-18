#Write a Python script to concatenate the following dictionaries to create a new one. 
#Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60}



def concatenate_dictionaries(*dicts):
    """
    Function to concatenate multiple dictionaries into a new one.
    
    Parameters:
    *dicts: Variable length dictionary list to be concatenated.

    Returns:
    dict: A new dictionary containing all key-value pairs from the input dictionaries.
    """
    concatenated_dict = {}  # Initialize an empty dictionary to store the result
    
    # Iterate over each dictionary passed as an argument
    for dictionary in dicts:
        concatenated_dict.update(dictionary)  # Add each key-value pair to the result dictionary
    
    return concatenated_dict

# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Concatenate dictionaries
new_dict = concatenate_dictionaries(dic1, dic2, dic3)

# Print the resulting dictionary
print("Concatenated Dictionary:", new_dict)


#Output
#Concatenated Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


