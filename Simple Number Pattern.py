#pyramid with ascending numbers
rows = 8
for i in range(1, rows+1):  
    for j in range(1, i + 1):  
        print(j, end=' ')  
    print('')  


# number pyramid with diamond shape
row = 15
for i in range(1, row + 1):
  print(" " * (row - i), end="")
    for k in range(1, i * 2):
        print(k, end="")
    print()
