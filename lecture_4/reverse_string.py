input_string = "Python"

# Method 1, using loop
reversed_string = ""
index = len(input_string) # index point to last character + 1
while index>0:
    index = index -1
    reversed_string = reversed_string + input_string[index]

print(reversed_string)

# Method 2, using slicing
reversed_string = input_string[::-1]
print(reversed_string)