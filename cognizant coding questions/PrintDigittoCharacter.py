
# To print Digit to character
x=input("Enter a digit:").split()
y=[]
for i in x:
    y.append(i +"-"+chr(int(i)))
print(*y)   


'''
Enter a digit:
65 67 68 69 70
OUTPUT: 65-A 67-C 68-D 69-E 70-F
'''