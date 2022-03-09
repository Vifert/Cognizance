import pandas as pd
ser = pd.Series(['amrita', 'school', 'of', 'engineering', 'chennai' , 'campus'])
l = ""
s = ser.str.title()
i = 0
while i < len(ser):
    l = l + s[i]
    l = l + " "
    i = i + 1
print(l)

