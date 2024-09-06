n=int(input())
arr=list(map(int,input().split()))
arr.sort()
ans=0
for i in range(1,n):
    ans+=arr[i]-arr[i-1]
print(ans)    

'''
input:3
      1 3 2 // 2-1=1 ,3-2=1 add 1+1 =2 
ouput:2
'''