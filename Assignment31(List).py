#Write a Python program to get the largest and smallest number from a list without builtin functions.



def get_largest_and_smallest(numbers):
    """
    Function to find the largest and smallest numbers in a list.
    
    Parameters:
    numbers (list): A list of numbers.

    Returns:
    tuple: A tuple containing the smallest and largest numbers.
    """
    if not numbers:
        raise ValueError("The list is empty")

    # Initialize the smallest and largest variables with the first element of the list
    smallest = numbers[0]
    largest = numbers[0]

    # Iterate through the list starting from the second element
    for number in numbers[1:]:
        if number < smallest:
            smallest = number  # Update smallest if the current number is smaller
        if number > largest:
            largest = number  # Update largest if the current number is larger

    return smallest, largest

# Example usage
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
smallest, largest = get_largest_and_smallest(my_list)
print("Smallest number in the list:", smallest)
print("Largest number in the list:", largest)



#Output
#Smallest number in the list: 1
#Largest number in the list: 9

