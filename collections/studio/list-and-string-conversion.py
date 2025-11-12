proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]
connectors = [',', ';', " "]
# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

for string in strings:
    for connector in connectors:
        if connector in string:
            if connector == " ":
                print(f"This {string} is separated by a space.")
            else:
                print(f"This {string} is separated by a '{connector}'.") 

# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.

# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.

# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.

# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.

for string in strings:
    if "," in string:  # b
        items = string.split(",")
        items.reverse()
        new_string = ",".join(items)
        print(new_string)

    elif ";" in string:  # c
        items = string.split(";")
        items.sort()
        new_string = "-".join(items)
        print(new_string)

    else:  # d
        items = string.split()
        items.sort(reverse=True)
        new_string = " ".join(items)
        print(new_string)


for string in strings:
    if ", " in string:  # e
        items = [item.strip() for item in string.split(",")]
        items.sort()  
        new_string = "-".join(items)
        print(new_string)

    elif "," in string:  
        items = string.split(",")
        items.reverse()
        new_string = ",".join(items)
        print(new_string)

    elif ";" in string:  
        items = string.split(";")
        items.sort()
        new_string = "-".join(items)
        print(new_string)

    else:  
        items = string.split()
        items.sort(reverse=True)
        new_string = " ".join(items)
        print(new_string)
