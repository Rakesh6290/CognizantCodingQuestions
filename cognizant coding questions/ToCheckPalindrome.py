
# To Check the palindrome number
x=int(input())
if x<0:
    print("Invalid")
else:
    y=str(x)
    j=y[::-1]
    if j==y:
        print("Palindrome Number")
    else:
        print("Not a Palindrome")

'''
input: 232
       Palindrome Number
input: 678
       Not a Palindrome
'''