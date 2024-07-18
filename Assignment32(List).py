#Write a Python program to sum all the items in a list.



def sum_of_list(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
print("Sum of the list:", sum_of_list(my_list))



#Output
#Sum of the list: 15
