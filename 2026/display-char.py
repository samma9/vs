# Display Character
# Created by Samuel Marriott on 15/03/2026

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
            break # Inputs are valid: End
        else:
            print("Please try again.") # Int number larger than string: Try again
    except ValueError:
        print("Please try again.") # Inputs are invalid: Try again