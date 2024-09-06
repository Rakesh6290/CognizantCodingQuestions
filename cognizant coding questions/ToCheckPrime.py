
# To print prime numbers upto given range 1-25
x=int(input())
y=int(input())
l=[]
while x<y+1:
    for i in range(2,x):
        if x%i==0:
            break
    else:
        l.append(x)
    x+=1
print(*l)        

'''
input:1
      25
output: 1 2 3 5 7 11 13 17 19 23
'''