#Write a function in Python to count and display the total number of words in a text file “ABC.txt”



#Open file
file = open("anudip.txt")
#Read data
data = file.read()
string = data
#apply split()
word = string.split()
#Count the word
word_count=len(word)
#Print the result
print("Total number of word =", word_count)
#Close file
file.close()



#Output
Total number of word = 5

