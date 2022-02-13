print("Table of Powers")
print()


numstart = int(input("Starting number:  "))
numstop = int(input("Stopping number:  "))

if numstop < numstart:
    print("please enter a number higher then starting number")
    numstart = int(input("Starting number:  "))
    numstop = int(input("Stopping number:  "))        
print()
print("      number    squared    cubed")
print("      ======    =======    =====")
for i in range(numstart, numstop + 1):
    print(f'\t{i}\t {i ** 2}\t    {i ** 3}')
