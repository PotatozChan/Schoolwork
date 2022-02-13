print("Letter Grade Converter")
print()

again = "y"

while again == "y":
    grade = int(input("Enter numerical grade:   "))
    if grade > 88:
        print("A")
    elif 80 <= grade < 88:
        print("B")
    elif 67 <= grade < 79:
        print("C")
    elif 60 <= grade < 66:
        print("D")
    else:
        print("F")
    print("Continue?")
    again = input("y/n:  ")

print("bye")
