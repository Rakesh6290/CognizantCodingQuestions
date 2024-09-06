# To Find the GCD of Two Numbers
x=int(input())
y=int(input())
z=0
l=[]
if x>y:
    z+=y
else:
    z+=x  
for i in range(2,z+1):
    if x%i==0 and y%i==0:
        l.append(i)
print(max(l))        
        

'''
input:8
      32
output:8
'''