import pandas as pd
table = []

count = int(input("Enter number of students: "))

for i in range(0, count):
    print("Enter details of each student\n")
    table.append([])
    for j in range(0, 4):
        if j==0:
            print()
            print("Enter R.No.:")
            Enter_details = input()
        elif j==1:
            print()
            print("Enter Name:")
            Enter_details = input()
        elif j==2:
            print()
            print("Enter Marks format:")
            Enter_details = input()
        else:
            Enter_details = ''
        table[i].append(Enter_details)

df = pd.DataFrame(table, columns=["R.No.        ", "Name        ", "Marks        ", ""])
df = df.set_index(['R.No.        ', 'Name        ',  'Marks        '])
print()
print()
print('i)')
print(df)
print()
print('ii)')
print(df[1:2])
