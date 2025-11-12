my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.
my_stringend = my_string[:3]
print(my_string[3:] + my_stringend)


# Use a template literal to print the original and modified string in a descriptive phrase.
print(f"Pig latin for {my_string} is {my_string[3:] + my_stringend}")


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
user = input("Please enter number 0 - 10: ")
user = int(user)
print(my_string[user:] + my_stringend)

# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
if user > len(my_string):
    print(f"Number too high. Defaulting to {my_string[3:] + my_stringend}")