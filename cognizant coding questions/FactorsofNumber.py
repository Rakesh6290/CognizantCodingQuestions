
#To find the factors of a number
n=int(input())
y=0
if n<0:
    y+=abs(n)
else:
    y+=n 
if y==0:
    print("No Factors")
else:
    l=[]
    for i in range(1,y+1):
        if y%i==0:
            l.append(i)
print(*l)  


'''
input:12
output:1 2 3 4 6 12
'''