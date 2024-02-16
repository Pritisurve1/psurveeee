#Simple Ascending Number Pyramid Pattern
def pattern(n):
     
    row = 1
    for i in range(0, n):
        row = 1
        for j in range(0, i+1):    
            print(row, end=" ")
            row = row + 1
        print("\r")
n = 5
pattern(n)

#Pyramid Number with Diamond Shape
row = 5
for i in range(1, row + 1):
    print(" " * (row - i), end="")
    for k in range(1, i * 2):
        print(k, end="")
    print()
