#Write a Python script to concatenate the following dictionaries to create a new one.



# Define the dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Create a new dictionary by concatenating the existing dictionaries
new_dic ={}
new_dic.update(dic1)
new_dic.update(dic2)
new_dic.update(dic3)

# Print the new concatenated dictionary
print("New_Dictionary = ", new_dic)



#Output
#New_Dictionary =  {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

