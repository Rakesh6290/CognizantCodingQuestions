
# To find the LCM of two numbers
x=int(input())
y=int(input())
z=0
if x>y:
    z+=y
else:
    z+=x  
while True:
    if z%x==0 and z%y==0:
        print("LCM of two numbers:",z)
        break
    z+=1    


'''
input:25
      90
LCM of two numbers: 450'''

 