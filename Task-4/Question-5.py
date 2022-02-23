#Question-5
n = int(input("Enter number of rows:"))
for i in range(n):
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(i + 1):
        print('* ', end='')
    print()
    