
# To print repeated value in the set of numbers 
# example : 1-40 numbers 3 is present in 3,13,23,....
n=int(input())
res=[]
for num in range(1,n+1):
    if num%10==3 or num//10==3:
    #if num%10==0 or num//10==0:
        res.append(num)
print(" ",*res)        

#40
#1 2 3 4 5 6 7 8 9 10 20 30 40
# input: 40
#output: 3 13 23 30 31 32 33 34 35 36 37 38 39