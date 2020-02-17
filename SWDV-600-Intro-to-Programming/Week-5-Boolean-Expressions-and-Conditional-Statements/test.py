inputString = input("Enter your String: ")
characterIndex = int(input("Enter the index of the character you want: "))
try:
    character = inputString[characterIndex]
    print("The character is", character)
except Exception as e:
    print("Out of bounds: ", e)
