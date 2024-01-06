def fibonacci(n):
    '''
    This func. uses recursion to find the nth elm.
    in the fibonacci sequence.

    args:
      n: The index of the element to find (starting from 1)

    returns:
      The nth element in the fibonacci sequence.
    '''

    if n <= 1:  # 2 base cases: if n is either 0 or 1, then just prt. it
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # 2x rec. call


# example usage:
n = 5
print(f"The {n}th element in the fibo. seq.: {fibonacci(n)}")

'''
1. fibo(5)
2. it calls fibo(4) + fibo(3)
3. fibo(4) calls fibo(3) + fibo(2)
4. fibo(3) calls fibo(2) + fibo(1)
5. Now, the base cases (n <= 1) are reached, and the rec.
   starts ret. val.
   fib(1) ret. 1
   fib(2) ret. 1
   fib(3) ret. 2 (1+1)
   fib(4) ret. 3 (2+1)
6. Finally, fib(5) ret. 5 (3+2).   
'''

'''
a1 a3 a9 a5 a4
Pattern we found: 'a' followed by a number, followed by a space 

Jose, Rolf, Charlie, Adam
Pattern we found: chars. followed by a comma, followed by a space

http://google.com
https://www.facebook.com
https://www.twitter.com
https://udemy.com
http://tecladocode.com

rolf@google.com
char.lie@twitter.com
anna@gmail.com
john43@icloud.me
some_one@example.net

"Getting" the REGEX is a matter of "seeing" the pattern(s). 
'''
