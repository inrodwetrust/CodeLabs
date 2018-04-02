def fibo(n):
    print('n == {}' .fornat(n))
    if n== 1 or n==2:
        print('end rercursion')
        return 1
    print('start new recursion...')

return fibo(fibo(n-1) + fibo(n-2))

print(fibo(10))
