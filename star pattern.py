print("we are making a half pyramid")
n=int(input("Enter the numbers of rows you wnat:"))
for i in range(n):
    for j in range(i+1):
        print("* ",end="")
    print()