# Display Character
# Created by Samuel Marriott on 15/03/2026

'''1. Asks the user to input a string.
2. Asks the user to input an integer (index)
3. Displays the character at that index in the string. (input_string[index]).'''

while True:
    try:
        input_string = input("Say something: ")
        index = int(input("Enter a number: "))
        #print(input_string, index)
        if index < len(input_string):
            char_at_index = (input_string[index])
            if char_at_index == " ":
                print("The character is an empty space.")
            print("The character at index", index, "is", char_at_index) # Displays character at index
            break # Inputs are valid: end while loop
        else:
            print("Please try again.")
    except ValueError:
        print("Please try again.") # Loop will continue until inputs are valid