def is_palindrome4(num):
    one = num // 1000
    two = num // 100 % 10
    three = num // 10 % 10
    four = num % 10
    if one == four and two == three:
        return(1)
    else:
        return(0)

A = int(input())
B = int(input())
for i in range(A, B + 1):
    if  is_palindrome4(i) == 1 :
        print(i, sep=',')

